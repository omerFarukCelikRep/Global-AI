#Functions

def hello():
    print("Hello, I am Batman");

hello();  #calling the functions the functions don't have any parameters

def sayHello(name):
    print("Hello ",name);

sayHello("Ömer");

def func_in_func(name):
    return sayHello(name);

func_in_func("Ömer");

def sumofValues(a,b):
    sumValues = a+b;
    print(sumValues);

sumofValues(2,3);

x = sumofValues(5.8,6.5);

def func(x,y):
    summ = x + y;
    multip = x * y;
    return (summ,multip);

t,c = func(25,62);

print("Sum of the values: " + str(t) + ", Multiplying of the values: " + str(c));


def sqr(x):
    if x== 5:
        return 5;

    result = x**2;
    return (result);

d = sqr(5);

print(d);


def signOfNumber(number):
    if number > 0:
        return ("Positive");
    elif number < 0:
        return ("Negative");
    else:
        return ("Zero");

print(signOfNumber(8));

def factorial(number):
    factorial = 1;
    if not (number == 0 or number == 1):
        while (number >= 1):
            factorial *= number;
            number -= 1; 
    print("Factorial: ", factorial);

factorial(5);

def factorialV2(number):
    factorial = 1;
    for i in range(1, number + 1):
        factorial *= i;

    return factorial;

print(factorialV2(5));

def factorialV3(number):
    factorial = 1;
    if not (number == 0 or number == 1):
        for i in range(factorial, number + 1):
            factorial *= i;
    print("Factorial: ", factorial);

factorialV3(5);

def sayHelloV2(name, capLetter = False):
    if capLetter:
        print("Hello ", name.upper());
    else:
        print("Hello ", name);

sayHelloV2("ömer Faruk",True);


#Lambda function

print((lambda x:x+1)(2));

fullName = lambda first,last:f'Full Name: {first.title()} {last.title()}';
print(fullName("Ömer","Faruk"));


#args and kwargs 

#args (Non Keyword Arguments)
#kwargs(Keyword Arguments)

def multp(*args):
    result = 1;
    for i in args:
        result *= i;
        print(result);


#*args keeps the data as tuple type 

multp(4,5,6,7,8);
multp([4,5,6,7,8]);

def func_kwargs(**kwargs):
    print(kwargs);

func_kwargs(name="Murat", name2 = "Ömer", number=13234);

def salaryCalculate(salary):
    if salary < 0:
        return ("Invalid Value");
    elif salary <=1000:
        salary += salary*0.15;
    elif salary <=2000:
        salary += salary*0.1;
    elif salary <=3000:
        salary += salary*0.05;
    else:
        salary += salary*0.025;

    return ("New Salary: ",salary);

print(salaryCalculate(800));


import random as rnd

words = ["artificial","intelligence","machine","learning","python","programming"];

def randomWord(words):
    index = rnd.randint(0,len(words));
    return words[index];


#Local and Global Variables
x = 5;  #Global Variables

def display():
    x = 4;  #Local Variavble
    return x;


#Methods

list1 = [1,2,3,4,5];

list1.remove(4);  #it does not return any value

maxElement = max(list1); #return the index of the element with the highest value in a given list



#Exceptions 

#print "Hello World!!!";   => SyntaxError


#Exception Handling

x = 'Alan Turing';

try:
    int(x);
except ValueError as error:
    print("Please enter an Integer Value ", error);
finally:
    print("This is always executed");


def reverse(s):
    if(type(s) != str):
        raise ValueError("Please enter a String type");
