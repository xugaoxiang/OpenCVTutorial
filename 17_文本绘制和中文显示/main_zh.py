import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':

    img_OpenCV = cv2.imread('lenna.png')

    # 将opencv图像格式转换成PIL格式, 数据类型是PIL.Image.Image
    img_PIL = Image.fromarray(cv2.cvtColor(img_OpenCV, cv2.COLOR_BGR2RGB))

    # 字体，linux中的默认的路径/usr/share/fonts，也可以使用其它可以显示中的字体文件，如示例中的simhei.ttf
    font = ImageFont.truetype('simhei.ttf', 26)

    # 字体颜色
    fillColor = (0, 0, 255)

    # 文字输出位置
    position = (50, 50)

    # 输出内容
    str = '你好，OpenCV-Python!'

    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, str, font=font, fill=fillColor)

    # 转换回OpenCV格式
    img_OpenCV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)

    cv2.imshow("dst", img_OpenCV)

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    cv2.destroyAllWindows()