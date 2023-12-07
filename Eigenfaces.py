import cv2
import numpy as np
from ToBeRecognited import Recognition
photo = []
label = []
for i in range(1,16):
        for j in range(4):
                label.append(i)
for i in range(1,61):
        path = r'D:/Matlab_Project/Camera/FaceRecognition/TrainDatabase/'+str(i)+'.jpg'
        photo.append(cv2.imread(path,0))

name={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'j','10':'k','11':'l','12':'m','13':'n','14':'o','15':'p'}
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(photo,np.array(label))
TestImage = cv2.imread(r"D:\Matlab_Project\Camera\FaceRecognition\TestDatabase\23.jpg",0)
label,confidence = recognizer.predict(TestImage)
RecognitionImage= r'D:/Matlab_Project/Camera/FaceRecognition/TrainDatabase/'+str(label*4-3)+'.jpg'
N = name[str(label)]
print(N)
Recognition(TestImage,RecognitionImage,N=N)


