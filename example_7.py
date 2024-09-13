# example_7.py
from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Conus(Shape):
    def draw(self):
        self.draw1.ellipse((153, 250, 347, 350),
                        fill='white', outline=(255, 255, 255))

        self.draw1.polygon(
            [(250, 100), (150, 300), (350, 300)], fill=(255, 255, 255))
        
    def erase(self):
        self.draw1.ellipse((153, 250, 347, 350), fill=self.back_color)
        self.draw1.polygon([(250, 100), (150, 300), (350, 300)], fill=self.back_color)


    def save(self):
        print("Image with conus was created")
        return self.im.save('draw-conus.png', quality=95)


class Paraboloid(Shape):
    def draw(self):
        # Основание конуса (эллипс)
        self.draw1.ellipse((153, 240, 347, 350),
                           fill='white', outline=(255, 255, 255))
        self.draw1.ellipse((155, 240, 347, 303),
                           fill='black', outline=(255, 255, 255))
        
    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)
        self.draw1.polygon(
            [(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with Paraboloid was created")
        return self.im.save('draw-Paraboloid.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                          '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t''8. Cтворити конус\n\t''9. Cтворити параболоид\n\t'
                          '0. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                con = Conus()
                work_with_obj(con)
            case 9:
                par = Paraboloid()
                work_with_obj(par)
            case 0:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
