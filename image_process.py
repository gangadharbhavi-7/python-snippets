from PIL import Image, ImageFilter

image = Image.open('example.jpg')
image_blur = image.filter(ImageFilter.BLUR)
image_blur.show()
