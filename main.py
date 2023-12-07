import cv2

from Rec import *

# Declare and assign the global variable image_array outside the main function
ImageArray = cv2.imread(r"D:\Matlab_Project\Camera\FaceRecognition\TestDatabase\3.jpg")
# image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
"""
现阶段做一个灰度的，下次掌握后在搞彩图
"""


def PCA(TestBase):
    from sklearn import preprocessing
    from sklearn.decomposition import PCA
    import matplotlib.pyplot as plt
    X_scaled = preprocessing.scale(TestBase)  # 调用sklean函数实现去中心化
    X_scaled = np.transpose(X_scaled)
    print(X_scaled.shape)
    # 使用PCA拟合数据
    pca = PCA(n_components=15)
    pca.fit(X_scaled)
    # 获取主成分
    components = pca.components_
    print(components.shape)
    [m, n] = TestBase.shape
    # 绘制前十个主成分脸
    fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(15, 6), subplot_kw={'xticks': [], 'yticks': []})
    for i, ax in enumerate(axes.flat):
        ax.imshow(components[i].reshape(128, 128), cmap='gray')  # 修改了 reshape 函数的参数
        ax.set_title("Component {}".format(i + 1))
    plt.show()
    plt.close()


def main():
    # No need to use global keyword here, because image_array is already a global variable
    TestBase = Inputting()
    EigenFace = PCA(TestBase=TestBase)
    print(EigenFace)
    # OutputName = Rec(ImageArray,EigenFace)
    # Recognition(ImageArray)
    # print(OutputName)


if __name__ == '__main__':
    main()
