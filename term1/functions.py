#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
#A lambda is a small anonymous function that can take any number of arguments, but can only have one expression. The expression is evaluated and returned.

def count(n):
    i = 0
    while i < n:
        yield i
        i += 1

for number in count(5) :
    print (number)  #this will print the numbers from 0 to 4

m = lambda x, y: x + y 
print(m(2,0)) #this will return 3



def yieds():
    yield 1
    yield 2
    yield 3
for value in yieds():
    print (value)




def my_function(*kids):
    print(type(kids))
    print(kids)
    return

my_function( "Kelvin", "Joel")



#function that adds 2 numbers and prints the result
def add_numbers(num1, num2):
    sum = num1 +num2
    print(sum)
    

add_numbers(2 , 3)

#function that asks for a user's name and greets them
def greet(name):
    print("Hello  " + name)

greet("Alice") 