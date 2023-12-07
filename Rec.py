import numpy as np
from sklearn import preprocessing
from Inputting import *


def Rec(TestImage: np.ndarray, EigenFaces: np.ndarray, ):
    # """
    #                  参数说明
    # :param TestImage:待检测图像
    # :param A: 中心化数据集
    # :param M: 数据均值
    # :param EigenFaces:特征脸集
    # """"
    TestBase = Inputting()
    m = np.mean(TestBase, axis=1)
    #m = np.reshape(m)
    A = preprocessing.scale(TestBase)
    ProjectedImages = []
    TrainNumber = A.shape[1]
    EigenFaces=np.ndarray(EigenFaces)
    print(f'EigenFaces size is {EigenFaces.shape}')
    for i in range(TrainNumber):
        temp = np.dot(EigenFaces, A[:, i])  # Projection of centered images into facespace
        ProjectedImages.append(temp)

    ProjectedImages = np.array(ProjectedImages)
    # Project the test image you selected into EigenFaces space
    # and calculate the test image feature vector.
    InputImage = TestImage
    temp = np.array(InputImage)
    row, col = temp.shape
    InImage = np.reshape(temp.T, row * col, 1)
    Difference = np.array(InImage, dtype=float) - m
    Projected_TestImage = np.dot(EigenFaces, Difference)  # Test image feature vector
    # Calculate Euclidean distances and find the index of image of minmum Euclidean distances.
    Euc_dist = []
    for i in range(TrainNumber):
        q = ProjectedImages[:, i]
        temp = np.sum((Projected_TestImage - q) ** 2)
        Euc_dist.append(temp)
    Recognized_index = np.argmin(Euc_dist)
    OutputName = str(Recognized_index) + '.jpg'
    return OutputName
