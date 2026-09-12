from PIL import Image

img= Image.open("digit.png")
print(img.size)   # No of pilxel * No of pixel in column

img=img.convert("L") 
img=img.resize((28,28))

img.save("digit_28x28.png") 

print(img.size)