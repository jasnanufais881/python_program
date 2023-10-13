d={'a':100,'b':200,'c':500,'d':4}
print("Initial dictionary")
print(d)
key=input("Enter the key to delete:")
if key in d:
    del d[key]
else:
     print("key not found")
     exit(0)
print("updated dictionary")
print(d)
