numOne = int(input("Write any number: "))
numTwo = int(input("Write another number: "))
symbol = input("Write any symbol (+, -, *, /, %): ")

if symbol == "+":
    print(numOne + numTwo)
elif symbol == "-":
    print(numOne - numTwo)
elif symbol == "*":
    print(numOne * numTwo)
elif symbol == "/":
    print(numOne / numTwo)
elif symbol == "%":
    print(numOne % numTwo)
else:
    print("You entered the wrong symbol.")
