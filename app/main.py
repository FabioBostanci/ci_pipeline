def greet(name=None):
    return f"Hallo, {name}"

def is_even(number):
    return number % 2 == 0

def add(a,b):
    return a+b

if __name__ == '__main__':
    print(greet())
    print("10 ist gerade:",is_even(10))
    print("2 + 3 =",add(2,3))