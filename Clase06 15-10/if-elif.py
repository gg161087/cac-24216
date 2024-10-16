#admission < 4 age is free
#admission between 4 and 18 is $500
#admission > 18 and < 60 is $1000
#admission > 60 $750

age = input("Ingrese edad: ")

if age.isdigit():
    age = int(age)
    if age > 0: 
        if age < 4:
            price = 0
        elif age >= 4 and age < 18:
            price = 500
        elif age >= 18 and age < 60:
            price = 1000
        elif age >= 60:
            price = 750
        # else:
        #     price = 750
    
        print(f"Tu entrada cuesta ${price}")
    else:
        print("Valor no permitido!")
else:
    print("Valor no permitido!")