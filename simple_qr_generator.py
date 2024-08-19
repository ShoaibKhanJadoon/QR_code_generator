import qrcode as qr

img = qr.make("data")

img.save("myQRcode.png")
