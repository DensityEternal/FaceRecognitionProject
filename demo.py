import cv2
import numpy as np
from sklearn.decomposition import PCA
#import umap
from Inputting import Inputting
from PCA import  PCA
from Rec import *
# Declare and assign the global variable image_array outside the main function
image_array = cv2.imread(r"D:\Matlab_Project\Camera\FaceRecognition\TestDatabase\3.jpg")
# image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
"""
现阶段做一个灰度的，下次掌握后在搞彩图
"""

def main():
    # No need to use global keyword here, because image_array is already a global variable
    TestBase = Inputting()
    EigenFaces = PCA(TestBase,30)
    ImageArray = cv2.imread(r"D:\Matlab_Project\Camera\FaceRecognition\TestDatabase\3.jpg")
    OutputName = Rec(ImageArray, EigenFaces)
    print(OutputName)
    # Recognition(image_array)


if __name__ == '__main__':
    main()
