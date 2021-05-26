print("Hello World")

#string
hello = "I am Batman";

print(hello);

#yorum için '#' işareti kullanılır

'''Çoklu
Satırlı 
Yorum
Satırı'''

#type() içerisine girilen değerin tipini verir
print(type(hello));
print(type("hello"));

#integer
int_value = 5;
print(int_value);
print(type(int_value));

#float
float_value = 3.14;
print(float_value);
print(type(float_value));

#Boolean
bool_value = True;
print(bool_value);
print(type(bool_value));

#swapping
data1 = 12;
data2 = 23;
data3 = 7;
data4 = 33;

data1,data2,data3,data4 = data4,data1,data2,data3;
print(data1,data2,data3,data4);

print("data1:",data1, "data2:",data2,"data3:",data3,"data4:",data4);

#len() içerisine yazılan str ifadenin uzunluğunu verir
print(len("Turkish AI Hub"));

#F-string
print(f"Hello {hello}");
print("Hello" ,hello);
print("Hello {}".format(hello));
print("Hello {} {}".format(hello,data4));
print("Hello {1} {0}".format(hello,data4));

print(str(data1));
print(type(str(data1)));

#Matematiksel İşlemler
print(5**2);


x=2;
print(x+2);
print(x-2);
print(x/2);
print(x//2);
print(x+2);
print(x%2);
print(x**2);


#Logical Operations
bool_value2 = False;
print(bool_value); #true
print(bool_value2); #false
print(bool_value or bool_value2); #true
print(bool_value and bool_value2); #false
print(not bool_value); #false
print(bool_value != bool_value2);
print(bool_value == bool_value2);

print("Hello" + "\n" + "World");
world = '%s %d' % (hello, len(hello));  #%s => string  %d => double

print(world);

#Type Conversion
print(float(5));
print(float("6.5"));
print(int(float(5)));

#string değer floata çevrilemez

print(int(6.7));

#Indexing and Slicing
print(hello[0]);
print(hello[1]);
print(hello[2]);
print(hello[3]);
print(hello[4]);
print(hello[5]);
print(hello[8]);
print(hello[9]);
print("----------");

print(hello[-1]);
print(hello[-2]);

print(hello[5:11]);
print(hello[5:]);
print(hello[:]);
print(hello[:-1]);

print(hello[5:len(hello)]);

print(hello[0:len(hello):3]);

city = "İstanbul";
print(city[0:6:2]);

print("a" in city);

print("r" in city);

print("anb" in city);

ai = "artificial" + " " + "intelligence";
print(ai);

words = "machine learning";
print(words.capitalize());
print(words.upper());
print(words.strip());

print(words.replace("machine","artifical"));

newInput = input("Lütfen Bir Değer Giriniz");
print(f"Girilen Değer : {newInput}");

x = int(input("Lütfen bir integer değer giriniz"));

print(x);

month = 12;
day = 365;

print("Bir Yıl", month, "ay ve", day, "gündür", sep=" ");
#sep ifadeler arasına belirttiğimiz değeri koymamızı sağlar

print(type("12"*(12%11)))

print("Hello"[0])

print("artificial inteligence".strip("e"))

x= 2;
y=1;
x *= y+1;
print(x);
