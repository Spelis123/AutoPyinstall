from os import system, remove
import shutil

path = input("Path to Script File: ")
filename = input("Filename: ")
windowed = "-w" if input("Is Windowed: (y/n)") == "y" else ""
icon = input("Icon: ")

system("pip install --upgrade pyinstaller && pip install --upgrade Pillow")
system(f"PyInstaller {path} -F -n {filename} {windowed} --distpath . -i {icon}")
shutil.rmtree("build")
remove(f"{filename}.spec")
