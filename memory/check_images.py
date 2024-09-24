"""
check whether all images in the folder have the target size
"""
import os

from PIL import Image

TARGET = (500, 500)
BLACKLIST = {"probably_fun_memory_0.8.png"}

for fn in os.listdir("."):
    if (
        fn.endswith(".png")
        and fn not in BLACKLIST
    ):
        im = Image.open(fn)
        if im.size != TARGET:
            print(fn, im.size)
        