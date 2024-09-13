# Завдання 2

# Створіть 2 класи мови, наприклад, англійська та іспанська. 
# В обох класів має бути метод greeting(). Обидва створюють різні привітання.
# Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції(функція hello_friend).

class English():
    def __init__(self):
        pass
    
    def greeting(self):
        print("Hello")


class Spanish():
    def __init__(self):
        pass
    
    def greeting(self):
        print("Hola")


english_hello = English()
spanish_hello = Spanish()


def hello_friend():
    english_hello.greeting()
    spanish_hello.greeting()

hello_friend()
