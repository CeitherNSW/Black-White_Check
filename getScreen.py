from PIL import Image, ImageGrab
# from matplotlib import pyplot as plt
import numpy as np



def getScreen():
    img = ImageGrab.grab()
    img = img.convert('RGB')
    img_arr = np.array(img)
    # print(type(img))
    # print(img.size)
    # print(img.mode)
    # print(img_arr[0])
    # plt.imshow(img)
    # plt.show()
    return [img_arr, img.size[0], img.size[1]]
    # return img_arr

# temp = getScreen()
# img = temp[0]
# width = temp[1]
# height = temp[2]
# plt.imshow(img)
# plt.show()
# print(width, height)
# def getSize(imgByteArr):
#     img = Image.open(io.BytesIO(imgByteArr))
#     return img.size
