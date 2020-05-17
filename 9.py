import os
from idlelib.iomenu import encoding
from PIL import Image

try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(str(e))
# Yes the following is legal
try:
    x = 1
finally:
    print("finally")

# IOError can catch input/output errors
# ZeroDivisionError can catch if something is divided by zero (as the name suggests)

file = open("name.txt", "w", encoding="UTF16")
file.write("יואל")
file.close()

file_read = open("name.txt", "r", encoding="UTF16")
print(file_read.read())


def pic(color, width, height):
    color1, color2, color3 = color.split()
    img = Image.new("RGB", (width * 3, height), color1)
    img2 = Image.new("RGB", (width, height), color2)
    img3 = Image.new("RGB", (width, height), color3)

    img.paste(img2, (width, 0))
    img.paste(img3, (width * 2, 0))
    img.show()


pic("green white red", 100, 300)
