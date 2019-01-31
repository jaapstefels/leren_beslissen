import os, gdal

in_path = '/Users/robbertsierhuis/Desktop/nlr_uva/'
input_filename = 'output.png'

out_path = '/Users/robbertsierhuis/Desktop/leren_beslissen/sat_rgb/'
output_filename = 'tile'

tile_size_x = 1024
tile_size_y = 1024

ds = gdal.Open(in_path + input_filename)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize

counter = 0

for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        com_string = "gdal_translate -of PNG -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(in_path) + str(input_filename) + " " + str(out_path) + str(output_filename) + "_" + str(counter) + ".png"
        os.system(com_string)
        counter += 1