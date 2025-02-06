age = int(input("Whats your age? "))
name = input("Introduce yourself: ")

if age > 120:
    print("Hi!")
    print("You should be dead instead of using this program")
    print("bye!")

elif age > 0 and age <= 50: # Cascadia Code
    print("Your not so old. fancy")
else:
    print( f"Hi {name} {age} 🦄" ) #f-strings