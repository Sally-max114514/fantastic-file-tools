# 📄 文件转换工具集

> DOCX ↔ PDF ↔ JPG 交互式转换工具，专为 Linux 环境设计。

基于 LibreOffice、Poppler-utils 和 ImageMagick 的交互式转换工具，支持批量或单次文档/图片格式转换。

---

## 📁 文件说明

- **`软件下载.py`** – 交互式依赖安装程序，支持一键安装 LibreOffice、Poppler-utils 和 ImageMagick，并提供跨平台下载 LibreOffice 安装包的功能（通过 wget 获取官方镜像）。
- **`文件转换器(shell).py`** – 核心转换工具，支持以下三种模式：
  - DOCX → PDF（基于 LibreOffice 无头模式）
  - PDF → JPG（基于 pdftoppm）
  - JPG → PDF（基于 ImageMagick 的 convert）

---

## ⚙️ 系统要求

- **操作系统**：Linux（脚本使用 `apt-get` 和 `sudo`，建议 Ubuntu/Debian 系）
- **Python 版本**：Python 3.x
- **依赖工具**（脚本会自动检测，但需手动安装）：
  - `libreoffice`（用于 DOCX → PDF）
  - `poppler-utils`（提供 `pdftoppm`，用于 PDF → JPG）
  - `imagemagick`（提供 `convert`，用于 JPG → PDF）

---
## 示例
```bash
请输入要转换的文件路径：/home/user/document.docx
请输入转换后的文件路径：/home/user/output.pdf
请你选择要转换的文件类型：
1.docx=>pdf
2.pdf=>jpg
3.jpg=>pdf
4.quit
请输入选项编号：1
程序将调用 LibreOffice 进行转换，并输出完成提示
```
