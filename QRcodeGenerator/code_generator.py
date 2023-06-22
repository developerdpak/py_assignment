import qrcode
"""
importing the library qr code
"""
# customize the box
features = qrcode.QRCode(version=1, box_size=40, border=3)

# data function , store the link of website while scanning the QR ocde

features.add_data('https://www.youtube.com/c/GeeksforGeeksVideos')
features.make(fit=True)
# give a variable name to store a strig,
# generate_image = qrcode.make("GeeksforGeeks")
generate_image = features.make_image(fill_color="black", black_color="white")
generate_image.save('image2.png')
# this creates and saves a png file in the same diretory


