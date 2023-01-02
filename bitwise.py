fruits = ["apple", "banana", "cherry", "melon", "starfruit", "jackfruit", "durian", "dragonfruit"]
print(fruits[:7:2])

if "apple" in fruits:
    print("yes")

fruit = input ("what fruit do you want to check?")
if fruit in fruits:
    print(f"there is {fruit} in fruits list")
else:
    print(f"there is no {fruit} in fruits list")
