import numpy as np
import cv2
def CosineSimilarity(input_face):

    """计算输入的主成分脸和人脸数据库中所有人脸的余弦相似度，并返回与之最相似的人脸的标签和相似度值。
     参数：
    input_face: numpy.ndarray，输入的主成分脸，形状为(n,)，其中n为特征脸的数量。
    face_database: dict，人脸数据库，其中key为人脸标签，value为该人脸的特征向量，形状为(m,)，其中m为特征脸的数量。
     返回值：
    label: str，与输入的主成分脸最相似的人脸的标签。
    cosine_sim: float，最大的余弦相似度值。
    """
    from sklearn import preprocessing
    from sklearn.decomposition import PCA

    input_face = input_face.reshape(128 * 128, 1)
    input_face = preprocessing.scale(input_face)  # 调用sklean函数实现去中心化
    print(f'input_face size is {input_face.shape}')
    X_scaled=np.transpose(X_scaled)
    pca = PCA(n_components=10)
    pca.fit(X_scaled)
    # 获取主成分
    components = pca.components_
    components =components.reshape(128,128)
    cv2.imshow('components',components)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print(components)
    def decomposition(input_face, k):
        """
        U 是一个矩阵，它的列是数据集缩放后的主成分
        E 是对角线上的奇异值矩阵
        V 是数据集的右奇异向量。
        """
        U, E, V = np.linalg.svd(input_face)
        V=np.transpose(V)
        e=np.zeros(k*k).reshape(k,k)
        for i in range(k):
            e[i][i]=E[i]
        E=e
        EigenFace = np.dot(U[:,0:k],np.dot(E[0:k,0:k],V[0:k,:]))
        EigenFace = np.transpose(EigenFace)
        print(EigenFace.shape)
        return EigenFace

    EigenFace = decomposition(input_face, 10)
    EigenFace.reshape(128,128)
    cv2.imshow('EigenFace',EigenFace)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cosine_sim = 0
    # label = None
    # for face_label, face_vector in face_database.items():
    #     # 计算输入主成分脸和当前人脸向量之间的余弦相似度
    #     sim = np.dot(input_face, face_vector) / (np.linalg.norm(input_face) * np.linalg.norm(face_vector))
    #     # 记录最高的相似度值及其对应的人脸标签
    #     if sim > cosine_sim:
    #         cosine_sim = sim
    #         label = face_label
    # return label, cosine_sim
ImageArray = cv2.imread(r"D:\Matlab_Project\Camera\FaceRecognition\TestDatabase\3.jpg")

ImageArray = cv2.cvtColor(ImageArray,cv2.COLOR_BGR2GRAY)
#cv2.imshow('ImageArray',ImageArray)
CosineSimilarity(ImageArray)