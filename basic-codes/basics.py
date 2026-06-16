print("Hello World!", end=" ")
print("I will print on the same line.")


x = str(33.33)  # x will be '3'
y = int("31")  # y will be 3
z = float(30)  # z will be 3.0

print(x)
print(y, "this is y")
print(z)
print(y + z)

print(type(5))
print(type("121212"))
print(type({}))
print(type([4]))
print(type(12.121))


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


def myfunc():
    print("Python is " + a)


a = "dumb"
myfunc()


def myfunc1():
    global x2
    x2 = "fantastic"


myfunc1()
print(x2)
print("Python is " + x)
print(type(range(6)))
print(type(None))

txt = "The best things in life are free!"
print("free" in txt)


a = "Hello, World!"
print(type(a[1]))
print(len(a))
print(a[2:5])
print(a[::-1])
print(a.upper())
print(a.lower())

a = " Hello, World! "
print(a.strip())

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "I love apples, apple are my favorite fruit"

x = txt.count("")
a = len(txt)
print(x, a)


txt = "My name is Ståle"

x = txt.encode(encoding="base64")

print(x)
