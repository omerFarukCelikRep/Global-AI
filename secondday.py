#Lists

#Creating a list
myList = [3,5,6,7];
print(myList);

newList = [2,5,6,"İstanbul", 3.54, 5.0, [3,4,5]];
print(newList);

myList[2] = "Pyhton";
myList.append('course');  #append() adding some items end of the list
print(myList);

myList = [3,4,5,6,7];
myList.append('Python')
theLast = myList.pop();  #pop() removing the last item of the list

myList.append('Python')
myList.index('Python');  #index()  returns the index of the value


list2 = ["Python","Java", "C#", "C++", "JavaScript","Python", "Python"];
print(list2.count("Python"));  #count(parameter)  return number of value

list2.remove("JavaScript");  #remove()  remove the value inside of the list 

list2.sort();  #sort() srting the list A to Z or lower to grater

print(list2);
list2.reverse();  # reverse()  reverse the list

list3 = ["JavaScript", "HTML","CSS"];
list2.extend(list3);  #extend(list)  extend the list with another list
print(list2); 

list3.insert(3,"C");  #insert(x,y)  => adding x th index the y value but dont change the x th value,
print(list3);


numbers = list(range(8));  #range(0,8)  #range(start, stop, step)
print(numbers);

numbers[5:8] = [10,11,12];
print(numbers);

print(12 in numbers);

print([1,2,3] * 3);

list1 = [[1,2],3,[4,5,6,[7,8,9]]];
print(list1[2][3][1]);


#Conditional Statements

#if

num = int(input("Please enter a number : "));

if num < 0:
    num *= -1

print("Result : ", num);

#if-else

if num > 0:
    num = 2;
else:
    num = 11;

#if-elif-else

score = int(input("Please enter your score :  "));

if score <= 40:
    print("Very Bad, you should work hard..");
elif score <= 60:
    print("Nice but you should work hard..");
elif score <= 100:
    print("Congratulations!!!");
else:
    print("Do you think it's a score???");



#While Loop Structure

#While

num = 0;

while num < 9:
    print("Value {}".format(num));
    num+=1;

num2 = int(input("Please enter an integer value between 1 and 10 :  "));

while num2 < 1 or num2 > 10:
    print("Invalid Value!!!");
    num2 = int(input("Please enter an integer value between 1 and 10 :  "));

print("Congrats");

aList = [1,2,3,4,5,6,7];
i = 0;
while i < len(aList):
    print(f"{i} th item: {aList[i]}");
    i+=1;

while True:
    a = input("Enter a value");
    if a == "Exit":
        break;

#For Loop

a = [2,45,57];
for i in a:
    print(i);

list5 = list("Pyton");
print(list5);

for i in range(8):
    if i == 5:
        break;
    print(i);


for i in range(8):
    if i == 5:
        continue;
    print(i);


for i in "Python Course".split():
    print(i);

nums = list(range(8));
squares = [];

for i in nums:
    squares.append(i ** 2);
print(squares);

squares = [i**2 for i in nums]
print(squares);

evenSquares = [i**2 for i in nums if i % 2 == 0];

oddSquares = [i**3 for i in nums if i % 2 != 0];

myList2 = [3,5,12,7,65,35]

sum = 0;

for i in myList2:
    sum = sum + i;
    print(sum);


#built-in functions

list1 = [1,2,3];
list2 = [4,5,6];

list(zip(list1,list2));

list3 = [a + b for a,b in zip(list1,list2)];

print(list3);

#Find the max item of list

myList = [3,5,12,7,65,35];

maxValue=myList[0];

for i in myList:
    if i> maxValue:
        maxValue = i;
        print(f"Max Value {max}");
        print(f"i : {i}");
print(max);