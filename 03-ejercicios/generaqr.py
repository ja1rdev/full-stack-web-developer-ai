import qrcode

link = "https://computer-labs-management.onrender.com/"
img = qrcode.make(link)
img.save("csl.png")