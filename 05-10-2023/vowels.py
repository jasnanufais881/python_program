string=input("Enter a string:")
v="aeiou"
for char in string:
    if char.lower() in v:
        print(char)
    
