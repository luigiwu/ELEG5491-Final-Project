import tensorflow as tffrom tensorflow.examples.tutorials.mnist import input_dataimport numpy as npimport randomimport matplotlibmatplotlib.use('TkAgg')from matplotlib import pyplot as pltfrom skimage.io import imsaveimport osimport shutilimport my_mnist as mmyimg_height = 28img_width = 28def show_result(batch_res, fname,average_picture, grid_size=(8, 8), grid_pad=5):    #index - real number 0-7 1-3 2-4 3-6 4-1 5-2 6-5 7-0 8-9 9-8    label = [2,4,3,8,4,8,0,0,9,8,2,2,0,4,7,4,0,9,9,7,9,9,2,3,1,3,8,0,8,9,9,7,7,9,9,9,8,8,9,9,8,7,4,7,9,4,7,9,4,4,4,8,8,8,9,4,4,4,9,4,9,9,0,9]    #print(len(label))    batch_res = 0.5 * batch_res.reshape((batch_res.shape[0], img_height, img_width))+0.5        #print(batch_res.shape[0]," ",batch_res.shape[1]," ",batch_res.shape[2] )    #print(average_picture.shape[0]," ",average_picture.shape[1]," ",average_picture.shape[2] )    img_h, img_w = batch_res.shape[1], batch_res.shape[2]    grid_h = img_h * grid_size[0] + grid_pad * (grid_size[0] - 1)    grid_w = img_w * grid_size[1] + grid_pad * (grid_size[1] - 1)    img_grid = np.zeros((grid_h, grid_w), dtype=np.uint8)    for i, res in enumerate(batch_res):                if i >= grid_size[0] * grid_size[1]:            break        #print(i)        img = (res) * 255        img = img.astype(np.uint8)        row = (i // grid_size[0]) * (img_h + grid_pad)        col = (i % grid_size[1]) * (img_w + grid_pad)        alpha = 0.7        img_av = img.mean()        img_std = img.std()        avp_av = average_picture[label[i]].mean()        avp_std = average_picture[label[i]].std()        img_tmp = (img - img_av)/img_std        avp_tmp = (average_picture[label[i]]-avp_av)/avp_std        avp_tmp = average_picture[label[i]].reshape(img_height, img_width)        img_z = img_tmp*(1-alpha) + avp_tmp*alpha        img_r = img_z * img_std*1.5 + img_av        img_grid[row:row + img_h, col:col + img_w] = img_r        imsave(fname, img_grid)def get_pic():    x_gen_val = np.loadtxt("Data.txt")    average_picture = mmy.get_mnist(10000)    #print(x_gen_val.shape)    show_result(x_gen_val, "output/test_result2.jpg",average_picture)if __name__ == '__main__':    get_pic()