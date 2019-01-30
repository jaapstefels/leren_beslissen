from osgeo import gdal
import numpy as np
import PIL
from PIL import Image
import os
import shutil
import fnmatch

path = "/Users/Dennis/Desktop/leren_beslissen/sat_2"

for i in os.listdir(path):
    if i.endswith("tif"):
        file_in = i
        file_out = './amersfoort_3band.tif'
        print(i)

        tile = gdal.Open(file_in)

        print ("[ RASTER BAND COUNT ]: ", tile.RasterCount)

        for band in range( tile.RasterCount ):
            band += 1
            print ("[ GETTING BAND ]: ", band)
            srcband = tile.GetRasterBand(band)
            if srcband is None:
                continue

            stats = srcband.GetStatistics( True, True )
            if stats is None:
                continue

            print ("[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
                        stats[0], stats[1], stats[2], stats[3] ) )


        myarray = np.array(tile.ReadAsArray())
        myarray.reshape(1500,1500,4)
        # print(myarray.shape)  # (num_bands, y_size, x_size)
        # np.set_printoptions(threshold=np.nan)
        # print("Dit is de volledige array")
        print(myarray)


        value = 0.255

        # print("Dit laag 0")
        laag_0 = myarray[0,:,:]
        # print(laag_0)

        img_0 = PIL.Image.fromarray(laag_0) 
        img_0.mode = 'I'
        img_0.point(lambda i:i*(value)).convert('RGB').save('laag_0.{}.png'.format(i))


        # print("Dit laag 1")
        laag_1 = myarray[1,:,:]
        # print(laag_1)

        img_1 = PIL.Image.fromarray(laag_1) 
        img_1.mode = 'I'
        img_1.point(lambda i:i*(value)).convert('RGB').save('laag_1.{}.png'.format(i))

        # print("Dit laag 2")
        laag_2 = myarray[2,:,:]
        # print(laag_2)

        img_2 = PIL.Image.fromarray(laag_2) 
        img_2.mode = 'I'
        img_2.point(lambda i:i*(value)).convert('RGB').save('laag_2.{}.png'.format(i))

        # print("Dit laag 3")
        laag_3 = myarray[3,:,:]
        # print(laag_3)

        img_3 = PIL.Image.fromarray(laag_3) 
        img_3.mode = 'I'
        img_3.point(lambda i:i*(value)).convert('RGB').save('laag_3.{}.png'.format(i))

        #OPTIE BLEND
        im1 = Image.open("laag_1.{}.png".format(i))
        im2 = Image.open("laag_2.{}.png".format(i))
        im3 = Image.open("laag_3.{}.png".format(i))
        im4 = Image.open("laag_0.{}.png".format(i))
        blended = Image.blend(im1, im2, alpha=0)
        blended2 = Image.blend(im3, im4, alpha=0)
        blended3 = Image.blend(blended, blended2, alpha=0)
        blended3.save("tile_{}.png".format(i))
        print("Converting done")

for f in os.listdir(path):
    if f.endswith("png"):
        newname = f.replace(".tif","")
        os.rename(f, newname)
        # if "tile" in f:
        #     if "trainingsdata." in f:
        #         newnames = f.replace("traningsdata.", "")
        #         os.rename(f, newnames)

# for x in os.listdir(path):
#     if x.startswith("blended"):
#         shutil.move(path"/blended.trainingsdata.{}.png".format(i), "/Users/Dennis/Desktop/leren_beslissen/sat_png")
#     print("done")


# OPTIE 1
# def rescale(myarray):
#     arr_min = myarray.min()
#     arr_max = myarray.max()
#     return (myarray - arr_min) / (arr_max - arr_min)

# myarray[:,:,0] = red_arr
# myarray[:,:,1] = green_arr
# myarray[:,:,2] = blue_arr

# myarray = 255.0 * rescale(myarray)

# img_RGB = Image.fromarray(myarray.astype(int), 'RGB')
# img.save('img_RGB.png')

# OPTIE 2


# def rescale(myarray):
#     arr_min = myarray.min()
#     arr_max = myarray.max()
#     return (myarray - arr_min) / (arr_max - arr_min)

# red_arr = laag_0
# blue_arr = laag_1
# green_arr = laag_2

# red_arr_b = 255.0 * rescale(red_arr)
# green_arr_b = 255.0 * rescale(green_arr)
# blue_arr_b = 255.0 * rescale(blue_arr)

# # myarray[:,:,0] = red_arr_b
# # myarray[:,:,1] = green_arr_b
# # myarray[:,:,2] = blue_arr_b

# img_RGB = Image.fromarray(myarray.astype(int), 'RGB')
# img_RGB.save('img_RGB.png')

# #OPTIE 4
# myarray[..., 0] = laag_0*256
# myarray[..., 1] = laag_1*256
# myarray[..., 2] = laag_2*256
# img = Image.fromarray(myarray)
# img.save('myimg.png')


# Create tif image (but only 3 bands in order 3-2-1)
#  with the same metadata (projection and geotransform) as reference
# driver = gdal.GetDriverByName("GTiff")
# band = tile.GetRasterBand(1)
# arr = band.ReadAsArray()
# [cols, rows] = arr.shape

# out_data = driver.Create(file_out, xsize=rows, ysize=cols, bands=3, eType=gdal.GDT_UInt16, options=['COMPRESS=LZW'])
# out_data.SetGeoTransform(tile.GetGeoTransform())  # sets same geotransform as input
# out_data.SetProjection(tile.GetProjection())  # sets same projection as input
# out_data.GetRasterBand(1).WriteArray(myarray[2,:,:])
# out_data.GetRasterBand(2).WriteArray(myarray[1,:,:])
# out_data.GetRasterBand(3).WriteArray(myarray[0,:,:])
# out_data.FlushCache()  # saves to disk!!
