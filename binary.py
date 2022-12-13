#number = int(input ("enter your decimal number: " ))


def decToBinary(decimalNumber):
	binary = bin(decimalNumber).replace("0b","")
	print(f"{decimalNumber} = {binary}")

decToBinary(250)
decToBinary(256)
decToBinary(138)

def bintodecimal(binarynumber):
    print(f"{binarynumber} = {int(binarynumber,2)}")

bintodecimal("100111")
bintodecimal("101100")
bintodecimal("001001")

