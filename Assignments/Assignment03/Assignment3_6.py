from sys import getsizeof

print("Enter Variable")
Value=input()

print("Value                : ",Value)
print("Type of No           : ",type(Value))
print("Memory Address of No : ",id(Value))
print("Size in Bytes        : ",getsizeof(Value))