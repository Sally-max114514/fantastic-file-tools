import os 
import sys
import time 

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("这个程序是下载文件转换器的所需要的依赖程序\n请确保你有权限访问要转换的文件的文件夹\n")
print("1.安装libreoffice套件\n2.安装poppler-utils套件\n3.安装ImageMagick套件\n4.退出程序\n5.跨平台下载libreoffice套件")
try:
    choice = int(input("请输入选项编号："))
except Exception as e:
    print(f"错误：{e}")
else:
    if choice == 1:
        print("正在安装libreoffice套件...")
        os.system('sudo apt-get install libreoffice')
        print("安装完成！")
    elif choice == 2:
        print("正在安装poppler-utils套件...")
        os.system('sudo apt-get install poppler-utils')
        print("安装完成！")
    elif choice == 3:
        print("正在安装ImageMagick套件...")
        os.system('sudo apt-get install imagemagick')
        print("安装完成！")
    elif choice == 4:
        print("程序已退出。")
        sys.exit()
    elif choice == 5:
        print("1.windows\n2.linux(deb)\n3.check your computer's opreating system")
        print("注意：以上的程序都是基于64位x86架构！")
        xuanxiang = int(input("please choose your computer's platfrom:"))
        if xuanxiang == 1:
            os.system("wget https://linux.domainesia.com/applications/tdf/libreoffice/stable/26.2.5/win/x86_64/LibreOffice_26.2.5_Win_x86-64_helppack_zh-CN.msi")
            print(":)")
        elif xuanxiang == 2:
            os.system("wget https://linux.domainesia.com/applications/tdf/libreoffice/stable/26.2.5/deb/x86_64/LibreOffice_26.2.5_Linux_x86-64_deb_langpack_zh-CN.tar.gz")
            print(":)")
        elif xuanxiang ==3:
            print(sys.platform)
        else:
            print("you can't do this,please retry again!")
    else:
        print("无效的选项，请重新运行程序并选择有效的选项。")