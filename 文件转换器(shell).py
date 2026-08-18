import os
import sys
import time

def type(text,speed=0.05):  #定义一个函数，参数为文本和速度
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

type("欢迎使用文件转换器")
print("注意：请确保你有权限访问要转换的文件的文件夹\n确保电脑上已经安装好了libreoffice套件\n")
type("如果你的电脑上没有安装libreoffice套件，请先安装它。\n 官方的下载地址：https://www.libreoffice.org/download/\n")

try:
    file_path = input("请输入要转换的文件路径：")
    if not os.path.isfile(file_path):
        raise FileNotFoundError("文件不存在，请检查路径是否正确。")
    file_output = input("请输入转换后的文件路径：")
    if not os.path.isdir(os.path.dirname(file_output)):
        raise FileNotFoundError("输出文件夹不存在，请检查路径是否正确。")
except (FileNotFoundError,Exception) as e:
    type(f"错误：{e}")
else:
    type("请你选择要转换的文件类型：")
    print("1.docx=>pdf\n2.pdf=>jpg\n3.jpg=>pdf\n4.quit")
    choice = int(input("请输入选项编号："))
    if choice in (1,2,3):
        if choice == 1:
            type("正在将docx文件转换为pdf文件...")
            os.system(f'libreoffice --headless --convert-to pdf "{file_path}" --outdir "{os.path.dirname(file_output)}"')
            type("转换完成！")
        elif choice == 2:
            type("正在将pdf文件转换为jpg文件...")
            os.system(f'pdftoppm -jpeg "{file_path}" "{os.path.splitext(file_output)[0]}"')
            type("转换完成！")
        elif choice == 3:
            type("正在将jpg文件转换为pdf文件...")
            os.system(f'convert "{file_path}" "{file_output}"')
            type("转换完成！")
    elif choice == 4:
        type("程序已退出。")
        sys.exit()
    else:
        type("无效的选项，请重新运行程序并选择有效的选项。")
        sys.exit()
