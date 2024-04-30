import asyncio

def decorator_maker(decorator_arg1, decorator_arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {decorator_arg1}, {decorator_arg2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_maker("Hello", "World!")
def decorated_function(a, b):
    print(f"Function arguments: {a}, {b}")

decorated_function("one", "two")

class OpenTheFile:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with OpenTheFile('example.txt', 'w') as f:
    f.write('I will prevail at getting a job in software development!')

def simple_generator(n):
    for i in range(n):
        yield i * i

for num in simple_generator(5):
    print(num)


async def count_to_ten():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(count_to_ten(), count_to_ten())

asyncio.run(main())

class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['hello'] = lambda self: f"Hello, {name}!"
        return type.__new__(cls, name, bases, dct)

class everybody(metaclass=Meta):
    pass

obj = everybody()
print(obj.hello())  # Output: Hello, everybody!

my_list = [2, 3, 4, 5, 6]
squared_list = list(map(lambda x: x ** 2, my_list))
print(squared_list)  # Output: [4, 9, 16, 25, 36]

name = "Jaylon"
age = 28

# Using f-strings (available from Python 3.6)
greeting = f"Hello, {name}. You are {age} years old."

# Using the str.format method
greeting = "Hello, {}. You are {} years old.".format(name, age)

# Using %-formatting
greeting = "Hello, %s. You are %d years old." % (name, age)

print(greeting)
