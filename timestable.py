print("times table")
number = int(input("enter a number: "))
loop = int(input("hom many times? "))
for n in range(loop+1):
    print(f"{number} X {n} = {number * n}")
    