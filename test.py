import face_recognition
import cv2
from PIL import Image,ImageDraw
import numpy as np
#knownImage = r"D:\Developer environment\FaceRecognition\ImgTest\S5\1.jpg"
knownImage2Path = r"D:\Developer environment\FaceRecognition\ImgTest\S2\1.jpg"
knownImage2 = face_recognition.load_image_file(knownImage2Path)

# unKnownImagePath = r"D:\Developer environment\FaceRecognition\ImgTest\S5\5.jpg"
# unKnownImage = face_recognition.load_image_file(unKnownImagePath)
#
# #encodingKnowImage = face_recognition.face_encodings(face_recognition.load_image_file(knownImage))[0]
#
#
# encodingKnowImage2 = face_recognition.face_encodings(knownImage2)
# encodingUnknownImage = face_recognition.face_encodings(unKnownImage)[0]
# # # encodings = [encodingUnknownImage,encodingKnowImage2]
# match = face_recognition.compare_faces(encodingKnowImage2,encodingUnknownImage)
# distance = face_recognition.face_distance(encodingKnowImage2,encodingUnknownImage)
# print(match)
# print(distance)

positions = face_recognition.face_locations(knownImage2)
Img = Image.fromarray(knownImage2)
for position in positions:
    top, right, bottom, left = position

    draw = ImageDraw.Draw(Img)
    draw.rectangle((top, right, bottom, left),outline="red")
    Img.show()