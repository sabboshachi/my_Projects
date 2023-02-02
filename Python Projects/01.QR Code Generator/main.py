import pyqrcode
data = "sabboshachi.github.io"
qr = pyqrcode.create(data)
qr.png("githubID.png", scale=5)