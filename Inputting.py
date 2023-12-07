def Inputting():
    import os
    import numpy as np
    import cv2

    path = r"D:\Matlab_Project\Camera\FaceRecognition\TestDatabase"
    img_list = os.listdir(path)  # 获取 images 文件夹中的所有文件名
    img_list.sort(key=lambda x: int(x[:-4]))  # 按照文件名中的数字进行升序排序，假设文件名是数字加.jpg
    TestBase = []  # 创建一个空的列表
    for i in range(len(img_list)):
        img = cv2.imread(os.path.join(path, img_list[i]), cv2.IMREAD_GRAYSCALE)  # 使用 cv2.imread 函数读取图片并转换为灰度图
        col = img.reshape(128 * 128, 1)  # 使用 reshape 函数将图片转换为列向量

        TestBase.append(col)  # 使用 append 函数将列向量添加到列表中

    TestBase = np.array(TestBase).squeeze().transpose()  # 使用 array 函数将列表转换为数组，并去掉多余的维度，然后转置数组，使得每一列对应一张图片

    return TestBase


"""
    把图像转化为矩阵并垂直连接，每一行都是一个人脸图像，大小为（128*128,45）
"""

