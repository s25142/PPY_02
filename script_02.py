

while bool(1):

    num1 = float(input("Podaj pierwsza liczbe: "))
    num2 = float(input("Podaj druga liczbe: "))
    operator = input("podaj operator: ")

    # Napisz skrypt kalkulator, który pobierze od użytkownika 2 liczby a następnie po podaniu
    # odpowiedniego operatora wykona adekwatną operację i wyświetli wynik.


    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if(num2 == 0):
            print("nie mozna dzielic przez 0")
        else:
            print(num1 / num2)
    elif operator == "//":
        if (num2 == 0):
            print("nie mozna dzielic przez 0")
        else:
            print(num1 // num2)
    elif operator == "%":
            print(num1 % num2)
    elif operator == "**":
        print(num1 ** num2)
    else:
        print("nie ma takiego operatora", "\n")