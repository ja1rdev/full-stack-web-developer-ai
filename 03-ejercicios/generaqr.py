import qrcode

link = "https://control-of-systems-laboratories.onrender.com/"
img = qrcode.make(link)
img.save("csl.png")