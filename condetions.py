x= 25
if x >= 18:
    print("eligible for liences")
else :
    print(" not eligible for liences")



# x = input("enter your level: ")
# if x == "a":
#     print("Have secondary school")
# elif x == "b":
#     print("Have university")
# elif x == "c":
#     print("Have master")
# else:
#  print("Non educational")



x= int(input("whats your age?"))
y= input("is it weekend or weekday?")

if y == "weekend":
    print ("The moive in weekend")
    if x > 12:
        print("your payment is 10$")
    else:
        print("your payment is 15$")
else:
    print ("The moive in weekday")
    if x >= 12:
        print("your payment is 8$")
    else:
        print("your payment is 12$")