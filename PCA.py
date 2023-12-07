
def PCA(TestBase,k):
    from sklearn import preprocessing
    import numpy as np
    from sklearn.decomposition import PCA
    import matplotlib.pyplot as plt
    X_scaled = preprocessing.scale(TestBase)  # 调用sklean函数实现去中心化
    def decomposition(ProceedData, k):
        """
        U 是一个矩阵，它的列是数据集缩放后的主成分
        E 是对角线上的奇异值矩阵
        V 是数据集的右奇异向量。
        """
        U, E, V = np.linalg.svd(ProceedData)
        V=np.transpose(V)
        e=np.zeros(k*k).reshape(k,k)
        for i in range(k):
            e[i][i]=E[i]
        E=e
        print(U.shape,E.shape,V.shape)
        EigenFace = np.dot(U[:,0:k],np.dot(E[0:k,0:k],V[0:k,:]))
        EigenFace = np.transpose(EigenFace)
        print(EigenFace.shape)
        return EigenFace


    def EigenfaceCore(EigenFace):
        fig, axes = plt.subplots(nrows=9, ncols=5, figsize=(15, 6),
                             subplot_kw={'xticks': [], 'yticks': []})
        for i, ax in enumerate(axes.flat):
            ax.imshow(EigenFace[i].reshape(128, 128), cmap='gray')
            ax.set_title("EigenFace {}".format(i + 1))
        plt.show()
        plt.close()

    EigenFace = decomposition(X_scaled, k)
    return EigenfaceCore(EigenFace),EigenFace



