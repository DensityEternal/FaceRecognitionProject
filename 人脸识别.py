# %%
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
from datetime import datetime


class FaceRecognition:
    def __init__(self, window):
        self.window = window
        self.window.title("人脸识别程序")
        self.cap = cv2.VideoCapture(0)

        # 初始化级联分类器
        casc_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(casc_path)

        # 创建画布并显示
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.pack()

        # 添加拍照按钮
        self.btn_capture = tk.Button(self.window, text="SnapShot", command=self.capture)
        self.btn_capture.pack()

        # 关闭窗口时释放相机
        self.btn_close = tk.Button(self.window, text="CloseAllWindows", command=self.__del__)
        self.window.protocol('WM_DELETE_WINDOW', self.__del__)
        self.btn_close.pack()
    def capture(self):
        ret, frame = self.cap.read()
        if not ret:
            print("获取图片失败！")
            return

        # 识别人脸并在画面上用矩形框标出
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 将OpenCV格式的图片转换为Tkinter格式
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # 在画布上显示图片
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # 将截图保存到本地
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Result_{now}.jpg"
        cv2.imwrite(filename, frame)
        cv2.destroyAllWindows()

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.window.destroy()

    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    window = tk.Tk()
    app = FaceRecognition(window)
    app.run()



