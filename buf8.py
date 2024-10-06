from PIL import Image

image = Image.open("назари.jpg")
image.show()

rotated_image = image.rotate(90)
rotated_image.show()
rotated_image.save("завантаження.jfif")
