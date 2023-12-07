# 制作数字、省份、英文字字母的png
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def WordToImg(word,name):
    image = np.zeros((80, 60, 3), np.uint8)  # 创建一个大小为80x60的图像
    image_pil = Image.fromarray(image)  # 将OpenCV图像转换为PIL图像
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype('zh-hans.ttf', 40)
    text_bbox = draw.textbbox((0, 0), word, font=font)
    x = (60 - text_bbox[2]) // 2
    y = (80 - text_bbox[3]) // 2
    draw.text((x, y), word, font=font, fill=(255, 255, 255))  # 将汉字绘制在图像中心位置
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'pic/{name}.png', image)

def NumToImg(num):
    Str = str(num)

    image = np.zeros((80, 60, 3), np.uint8)  # 创建一个大小为80x60的图像
    image_pil = Image.fromarray(image)  # 将OpenCV图像转换为PIL图像
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype('zh-hans.ttf', 40)  # simhei.ttf是黑体字，需要将此字体文件放在当前目录下
    text_bbox = draw.textbbox((0, 0), Str, font=font)
    x = (60 - text_bbox[2]) // 2
    y = (80 - text_bbox[3]) // 2
    draw.text((x, y), Str, font=font, fill=(255, 255, 255))  # 将汉字绘制在图像中心位置
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'pic/{Str}.png', image)
def CharToImg(char):
    image = np.zeros((80, 60, 3), np.uint8)  # 创建一个大小为80x60的图像
    image_pil = Image.fromarray(image)  # 将OpenCV图像转换为PIL图像
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.truetype('zh-hans.ttf', 40)  # simhei.ttf是黑体字，需要将此字体文件放在当前目录下
    text_bbox = draw.textbbox((0, 0), char, font=font)
    x = (60 - text_bbox[2]) // 2
    y = (80 - text_bbox[3]) // 2
    draw.text((x, y), char, font=font, fill=(255, 255, 255))  # 将汉字绘制在图像中心位置
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'pic/{char}.png', image)
provinces = ['皖', '闽', '甘', '粤', '桂', '黔', '琼', '冀', '豫', '黑', '鄂', '湘', '吉', '苏', '赣', '辽', '蒙', '宁',
             '青', '鲁', '晋', '陕', '沪', '川', '台', '津', '藏', '新', '滇', '浙']
n=1
for i in range(30) :

    name='0'+str(n)

    WordToImg(word=provinces[i],name=name)
    n+=1
for i in range(65,65+26):
    S=chr(i)
    CharToImg(S)
for i in range(10):
    NumToImg(i)

