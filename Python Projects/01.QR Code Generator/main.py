import pyqrcode
data = list["Rudra", "Sandy", "Tekka", "Leo"]
qr = pyqrcode.create(data)
qr.png("githubID.png", scale=5)