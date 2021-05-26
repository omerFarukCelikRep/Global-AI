cost = 79;
tax = cost * 0.08;
tip = cost * 0.1;
total = cost + tax + tip;

print("The tax is {} Eur, the tip is {} Eur, making the total {} Eur".format(tax, tip,format(total,".2f")));


salary = float(input("Please enter your salary : "));

if salary < 0 :
    print("Invalid Value!!!");
elif salary <=1000:
    salary += salary*0.15;
elif salary <=2000:
    salary += salary*0.1;
elif salary <=3000:
    salary += salary*0.05;
else:
    salary += salary*0.025;    

print(f"Your raised salary is {salary}"); 

stop_number = int(input("Please enter a stop number : "));
result = 0;

for i in range(0,stop_number):
    result += i;
    print(result);
print(result);

start_number = int(input("Please enter a start number : "));
stop_number = int(input("Please enter a stop number : "));

for i in range(start_number,stop_number):
    result += i;
    print(result);
print(result);


start_number = int(input("Please enter a start number : "));

if 0 <= start_number <= 100:
    stop_number = int(input("Please enter a stop number : "));

    if start_number <= stop_number <= 100:
        result = 0;
        for i in range(start_number, stop_number):
            result += i;
        print(result);
    else:
        print("Invalid stop number");
else:
        print("Invalid start number");