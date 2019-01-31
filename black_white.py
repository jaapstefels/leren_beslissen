from PIL import Image
import os
import shutil

for i in os.listdir("/Users/jaap/Desktop/leren_beslissen/map_data_1024_png"):
    if i.endswith(".png"):
        file_in = i
        # file_out = './amersfoort_3band.tif'
        print(file_in)

        col = Image.open(i)
        gray = col.convert('L')
        bw = gray.point(lambda x: 255 if x > 0 and x < 255  else 255, '1')
        bw.save("bw_{}".format(i))