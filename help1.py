from PIL import Image


image = Image.open("назари.jpg")
while True:
    print("1.Показати зображення")
    print("2.Зберегти зображення")
    print("3.Зрбити ч\б")
    print("4.Поворот зображення")
    print("5.Відзеркалення зображення")
    print("6.Накладання контурів")
    print("7.Розмивання")
    print("8.Збільшення яскравомті")
    print("9.Тиснення")
    operation = input ("Введіть операцію")
    if operation == "1":
        image.show()
    elif operation == "2":
        name = input("введіть назву файлу")
        image.save(name)
    elif operation == "3":
        image = image.convert("L")
    elif operation == "4":
        img = img.transpose(Image.ROTATE_90)
    elif operation == "5":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif operation == '6':
        img = img.filter(ImageFilter.CONTOUR)
    elif operation == "7":
        img = img.filter(ImageFilter.BLUR)
    elif operation == "8":
        img = ImageEnhance.Brightness(img).enhance(1.5)
    elif operation == "9":
        img = img.filter(ImageFilter.EMBOSS)



