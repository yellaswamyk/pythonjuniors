def greeting(name):
  print("Hello, " + name)
import mymodule
mymodule.greeting("anish")
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
import mymodule
a = mymodule.person1["age"]
print(a)
import mymodule as mx
a = mx.person1["age"]
print(a)
import platform
x = platform.system()
print(x)
import platform
x = dir(platform)
print(x)
def greeting(name):
  print("Hello, " + name)
person1 = {
  "name": "anish",
  "age": 13,
  "country": "India"
}
from mymodule import person1
print (person1["age"])
