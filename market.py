number1 = int(input("Masukkan angka ke 1: "))
number2= int(input("Masukkan angka ke 2: "))
def addition(a,b):
    global result
    result = a + b
    print(f" {a} + {b} = {result}")
addition (number1, number2)
print (result)