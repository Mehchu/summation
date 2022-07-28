i = int(input("Enter i: "))
j = int(input("Enter j: "))

total = int((j**2 - i**2 + j + i)/2)
print(total)
if str(total)[0:len(str(i))] == str(i) and str(total)[len(str(total)) - len(str(j)):] == str(j) and len(str(i)) + len(
        str(j)) <= len(str(total)):
    print(f'{i}-{j} = {total}')

