import qrcode

link = "https://web-production-6471c.up.railway.app/"
img = qrcode.make(link)
img.save("ias.png")