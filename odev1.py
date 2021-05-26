numbers = list(range(0,100));
evenNumbers = [];
oddNumbers = [];

for i in numbers:
    if i % 2 == 0:
        evenNumbers.append(i);
    else:
        oddNumbers.append(i);

print(oddNumbers);