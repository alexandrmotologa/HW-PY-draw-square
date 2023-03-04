from os import system

system("cls")
width = int(input('Width: '))
height = int(input('Height: '))

print()

for i in range(height):
    for j in range(width):
        print("+ ", end="")
    print()
print()