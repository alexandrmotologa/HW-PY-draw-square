from os import system

system("cls")
size = int(input('size: '))
length = size * size
n = 1

print()

while n <= length:
    print("+ ", end= "")
    
    if n % size == 0:
        print()
    
    n += 1
print()