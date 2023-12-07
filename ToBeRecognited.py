import tkinter as tk

import numpy as np
from PIL import Image, ImageTk
def Recognition(TestImage, RecognitionImage,N):
    root = tk.Tk()
    root.title("Face recognition")

    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)

    # 加载第一张图片
    def openImage1():
        img1 = Image.open(RecognitionImage)
        img1 = img1.resize((480, 360), Image.ANTIALIAS)  # 调整图片大小
        photo1 = ImageTk.PhotoImage(img1)
        label1 = tk.Label(canvas, image=photo1,text=N,compound=tk.TOP)
        label1.photo = photo1  # 防止图片被垃圾回收
        label1.grid(row=0, column=0)  # 将图片放在网格的第一行第一列
        openImage2()

    # 加载第二张图片
    def openImage2():
        # 假设你已经得到了图像的数字矩阵，存储在变量image_array中
        img2 = Image.fromarray(TestImage)  # 将数字矩阵转换为Image对象
        img2 = img2.resize((480, 360), Image.ANTIALIAS)  # 调整图片大小
        photo2 = ImageTk.PhotoImage(img2)  # 将Image对象转换为PhotoImage对象
        label2 = tk.Label(canvas, image=photo2,text='待识别对象',compound=tk.TOP)  # 创建一个Label，用于显示图片，修改这一行
        label2.photo = photo2  # 防止图片被垃圾回收
        label2.grid(row=0, column=1)  # 将图片放在网格的第一行第二列

    # 创建一个按钮，用于打开第一张图片
    button1 = tk.Button(root, text="开始识别", command=openImage1)
    button1.pack(side=tk.LEFT)
    root.mainloop()


