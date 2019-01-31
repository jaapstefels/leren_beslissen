from PIL import Image


for i in os.listdir("/sat_data"):
    if i.endswith(".tif"):
        file_in = i
        # file_out = './amersfoort_3band.tif'
        print(file_in)

def convert(i):
    col = Image.open("map_data_1024_png/tile_0.png")
    gray = col.convert('L')
    bw = gray.point(lambda x: 255 if x > 0 and x < 255  else 0, '1')
    bw.save("tile_0_bw.png")

if __name__ == "__main__":
    main()