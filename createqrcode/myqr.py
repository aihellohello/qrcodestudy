import qrcode

my_str ='https://mp.weixin.qq.com/s/lAOxEG1TB6czHBMXcwpkjA' #'我爱你'#

# img = qrcode.make(my_str)
# img.save('simpleqrcode.jpg')



qr=qrcode.QRCode(version = 2,error_correction = qrcode.constants.ERROR_CORRECT_L,box_size=10,border=10,)
qr.add_data(my_str)
qr.make(fit=True)
img = qr.make_image()
# img.show()
img.save('gaoji2.jpg')