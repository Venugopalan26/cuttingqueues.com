from PIL import Image
im = Image.open("logo.png")
print("Creating favicon.png")
im.resize((64, 64)).save("favicon.png")