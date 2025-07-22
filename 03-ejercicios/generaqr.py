import qrcode

link = "https://systems-laboratory-control.onrender.com"
img = qrcode.make(link)
img.save("slc.png")