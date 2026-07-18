print("---------------------------------------------------")
print("--------------Ticket Pricing Software--------------")
print("---------------------------------------------------")

print("Please Enter your Age")
Age=int(input())

if (Age <= 5):
    print("Free Entry")
elif(Age>5 and Age <= 18):
    print("Ticket price is:900")
elif(Age>18 and Age <= 40):
    print("Ticket Price is:1200")
else:
    print("Ticket Prie is:500")