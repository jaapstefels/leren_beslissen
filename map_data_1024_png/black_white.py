from PIL import Image
import os
import shutil

for i in os.listdir("/Users/jaap/Desktop/leren_beslissen/map_data_1024_png"):
    if i.startswith("tile"):
        print(i)
        col = Image.open(i)
        gray = col.convert('L')
        bw = gray.point(lambda x: 255 if x > 0 and x < 255 else 0, '1')
        bw.save("bw_{}".format(i))
    else:
        continue