from PIL import Image
import qrcode
from qrcode.constants import ERROR_CORRECT_H

my_str ='https://mp.weixin.qq.com/s/lAOxEG1TB6czHBMXcwpkjA'

qr = qrcode.QRCode(version=20,
                   error_correction=ERROR_CORRECT_H,
                   box_size=3, border=2)


# 添加自定义文本信息
qr.add_data(my_str)
qr.make(fit=True)


img = qr.make_image()
img = img.convert("RGB")#加上彩色logo


imgW, imgH = img.size
w1, h1 = map(lambda x: x // 4, img.size)
# 要粘贴的自定义图片，生成缩略图

icon = Image.open("logo.jpg")
imW, imH = icon.size
icon_w = w1 if w1 < imW else imW
icon_h= h1 if h1 < imH else imH
icon = icon.resize((w1, h1))
icon=icon.convert("RGB")#加上彩色logo 同一种格式

w = int((imgW - icon_w)/2)
h = int((imgH - icon_h)/2)

img.paste(icon,(w,h))
#img.show()
img.save('createlogo.jpg')