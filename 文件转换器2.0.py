import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

SPEED = float(os.environ.get("TYPE_SPEED", "0.03"))


def type(text, speed=None):
    speed = SPEED if speed is None else speed
    if speed <= 0:
        print(text)
        return
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def run_cmd(desc: str, cmd: list[str]) -> int:
    type(desc)
    ret = subprocess.run(cmd, shell=False).returncode
    if ret == 0:
        type("转换完成！")
    else:
        type(f"转换失败（退出码 {ret}），请检查命令是否安装、路径是否正确。")
    return ret


def check_deps():
    required = {
        "libreoffice": "libreoffice",
        "pdftoppm": "poppler-utils",
        "convert": "imagemagick",
    }
    missing = [name for name in required if shutil.which(name) is None]
    if missing:
        type(f"缺少命令：{', '.join(missing)}")
        type("请安装对应软件包后再运行。")
        sys.exit(1)


def get_input_path(prompt: str, exts: tuple[str, ...] | None = None) -> Path:
    raw = input(prompt).strip().strip('"').strip("'")
    p = Path(raw).expanduser().resolve()
    if not p.exists():
        raise FileNotFoundError(f"路径不存在：{p}")
    if not p.is_file():
        raise IsADirectoryError(f"这不是一个文件：{p}")
    if exts and p.suffix.lower() not in exts:
        raise ValueError(f"文件类型应为 {exts}，实际为 {p.suffix}")
    return p


def get_output_dir(prompt: str) -> Path:
    raw = input(prompt).strip().strip('"').strip("'")
    p = Path(raw).expanduser().resolve()
    if p.suffix:  # 用户给的是文件路径
        p = p.parent
    if not p.is_dir():
        raise FileNotFoundError(f"输出文件夹不存在：{p}")
    return p


CONVERTERS = {
    1: {
        "desc": "docx => pdf",
        "src_ext": (".docx",),
        "cmd": lambda src, out_dir: [
            "libreoffice", "--headless", "--convert-to", "pdf",
            str(src), "--outdir", str(out_dir),
        ],
    },
    2: {
        "desc": "pdf => jpg",
        "src_ext": (".pdf",),
        "cmd": lambda src, out_dir: [
            "pdftoppm", "-jpeg", str(src), str(out_dir / src.stem),
        ],
    },
    3: {
        "desc": "jpg => pdf",
        "src_ext": (".jpg", ".jpeg"),
        "cmd": lambda src, out_dir: [
            "convert", str(src), str(out_dir / (src.stem + ".pdf")),
        ],
    },
}


def main():
    check_deps()

    type("欢迎使用文件转换器")
    print("注意：请确保你有权限访问目标文件夹，并已安装 libreoffice / poppler-utils / imagemagick\n")

    type("请选择要转换的文件类型：")
    for k, v in CONVERTERS.items():
        print(f"{k}.{v['desc']}")
    print("4.quit")

    try:
        choice = int(input("请输入选项编号：").strip())
    except ValueError:
        type("请输入数字。")
        sys.exit(1)

    if choice == 4:
        type("程序已退出。")
        sys.exit(0)
    if choice not in CONVERTERS:
        type("无效的选项。")
        sys.exit(1)

    conv = CONVERTERS[choice]

    try:
        src = get_input_path("请输入要转换的文件路径：", exts=conv["src_ext"])
        out_dir = get_output_dir("请输入输出文件夹（或输出文件路径）：")
    except Exception as e:
        type(f"错误：{e}")
        sys.exit(1)

    run_cmd(f"正在将 {conv['desc']} ...", conv["cmd"](src, out_dir))


if __name__ == "__main__":
    main()