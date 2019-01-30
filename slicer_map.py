import os, gdal

in_path = '/Users/jaap/Desktop/leren_beslissen/'
input_filename = 'top10nl_wegvlak_amersfoort.tif'

out_path = '/Users/jaap/Desktop/leren_beslissen/map_data_1024_tif/'
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
        com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(in_path) + str(input_filename) + " " + str(out_path) + str(output_filename) + "_" + str(counter) + ".tif"
        os.system(com_string)
        counter += 1