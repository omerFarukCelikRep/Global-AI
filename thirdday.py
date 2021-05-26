import random as rnd

if not True:
    print("I am Batman");
else:
    print("It's true");

secret = rnd.randint(1,100);
check = False;

#guess = int(input("Please enter your guess:  "));

for i in range(5):
    guess = int(input("Please enter your guess:  "));
    if guess == secret:
        print("Congrats!!!");
        check = True;
        break;
    elif guess < secret:
        print("Please enter a greater number!!!");
    else:
        print("Please enter a smaller number!!!");

if not check:
    print("Come on, you can do better. Let's try again");
    print(f"Secret number is {secret}");

    #Dictionaries

d = {};

print(d);
print(type(d));

d = { "python":1, "course":2};
print(d);


dic = {"machine":"learning", "artifical":"intelligence"};

print(dic);

dic["java"] = "programming";
dic["ruby"] = "programming";
print(dic);

dic["ruby"] = "language";
print(dic);

print(dic.keys());
print(dic.values());
print(dic.items());

for x in dic.keys():
    print(x);

for k,v in dic.items():
    print(f"Key: {k}, Value: {v}");

d["a"] = [1,2,3];

d.pop("python");
print(d);

print(d.get("a"));

del d["a"];

print(d.get("a"));

d["machine"] = "deep learning";

dCopy = d.copy();
print(dCopy);

dic2 = {
    "human":2,
    "cat":4,
    "spider":8
};

for i in dic2:
    legs = dic2[i];
    print("%s has %d legs " % (i,legs));
    print(str(i) + " has " + str(legs) + " legs.");

for i,leg in dic2.items():
    print(str(i) + " has " + str(leg) + " legs.");

districts = {
    "İstanbul":["Bostancı","Beşiktaş","Kadıköy"],
    "Ankara":["Çankaya", "Gölbaşı", "Kızılcahamam"],
    "İzmir":["Çeşme", "Bornova", "Foça"]
};

print(districts["İstanbul"]);

print(districts["İzmir"][2])

#creating a dictionary from a list

nums = list(range(9));

evenSquares = {x:x**2 for x in nums if x % 2 == 0};
print(evenSquares);


#Sets

setExample = {"python", 5,6,8,5,6,"abc","python","python","python"};
print(setExample);

empty = set();
print(type(empty)); #set

empty2 = {};
print(type(empty2)); #dictionary

set2 = set(["python",5,6,8,5,6,"abc","python"]);

print(set2);

word = set("pineapple");
print(word);
print(6 in word);

print(len(word));

set2.add("ai");
print(set2);

from math import sqrt

#import math 

print({x for x in list(range(10))});
print({sqrt(x) for x in list(range(10))});



#Tuples

tupl = (1,2,3,4,5);
print(tupl);
print(type(tupl));

tuple2 = ();
print(type(tuple2));

print(tupl[3]);
print(tupl[:3]);

tuple3 = ("asli", 4, 8, "eylül");
print(tuple3.index("asli"));

#Tuples can not changed 

#tuple3[3] = "cherry"   #işlem yapılamaz

tupleDic = {(x, x+1): x for in range(10)};
print(tupleDic);

tuple5 = (5,6);

print(tupleDic[tuple5]);