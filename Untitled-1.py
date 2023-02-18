class Math():

    def addition(a,b):
        print(a+b)

    def multiplication(a,b):
        print(ab)

    def division(a,b):
        print(a/b)

    def subtraction(a,b):
        print(a-b)

    def start():
        a = float(input("Введите первое число -> "))
        b = float(input("Введите второе число -> "))
        c = input("Введите знак -> ")
        Math.variation(a,b,c)

    def variation(a = 0, b = 0, c = 0):
        if c == "+":
            Math.addition(a,b)
        elif c == "-":
            Math.subtraction(a,b)
        elif c == "":
            Math.multiplication(a,b)
        elif c == "/":
            Math.division(a,b)
        else:
            print("Вы ввели не верное значение в какой-то переменной")

Math.start()
