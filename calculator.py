print("1 Addition")
print("2 subtraction")
print("3 multiplication")
print("4 division")

choice = input("enter you choice :")

num1 = float(input("enter number 1 :"))
num2 = float(input("enter number 2 :"))

if choice == "1":
     print(num1, "+", num2 , "=",(num1+num2))
elif choice == "2":
      print(num1, "-", num2 , "=",(num1-num2))
elif choice == "3":
      print(num1, "*", num2 , "=",(num1*num2))
elif choice == "4":
      if num2 ==0.0:
          print("divide by 0 error")
      else:print(num1, "/", num2 , "=",(num1/num2))
