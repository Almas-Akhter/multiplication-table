num = int(input("Enter a positive number to print its multiplication table: "))
print("Multiplication Table of", num)
for i in range(1, 13):
    print(num, "x", i, "=", num * i)
