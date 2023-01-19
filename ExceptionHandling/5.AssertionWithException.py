try:
    num = int(input("enter a even number"))
    assert num%2==0, "you have entered a invalid input"
except ArithmeticError as obj:
    print(obj)

print("After the assertion")