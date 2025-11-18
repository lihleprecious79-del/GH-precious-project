print("=== Even or Odd Checker ===")

try:
    number= int(input("enter an integer :"))
    if number % 2 == 0 :
        print(number, "is even.")
    else:
        print(number," IS ODD.")

except ValueError :
        print("error: please enter a valid interger !")

