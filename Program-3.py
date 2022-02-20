a = int(input("Enter a: "))

if a % 2 != 0:
    for x in range(1, a*2, 2):
        print(x, end=" ")
if a % 2 ==0:
    for x in range(1, (a-1)*2, 2):
        print(x, end=" ")
