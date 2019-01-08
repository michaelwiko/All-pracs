out_file = open ("name.txt", "w")
name = input("What is your name? ")
out_file.write(name)
out_file.close()

in_file = open("name2.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt, "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

in_file = open("numbers2.txt, "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()