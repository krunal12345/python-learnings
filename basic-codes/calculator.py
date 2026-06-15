print("this is basic calculator app")


exit = False


def add(value1, value2):
    return value1 + value2


def substract(value1, value2):
    return value1 + value2


def multiply(value1, value2):
    return value1 * value2


def division(value1, values2):
    return value1 / values2


while not exit:
    # get user input and ssign in variable a.
    print("Enter value 1")
    val1 = input()
    val1 = int(val1)

    print("enetr values 2")
    val2 = input()
    val2 = int(val2)

    print(
        "what do you want to do with this two values or exit for exiting the calculator"
    )
    operation = input()

    output = 0
    match operation:
        case "add":
            output = add(val1, val2)
        case "substract":
            output = substract(val1, val2)
        case "multiply":
            output = multiply(val1, val2)
        case "division":
            output = division(val1, val2)
        case "exit":
            exit = True
        case _:
            print("No match opeartion found")
    print(f"output is {output}")
