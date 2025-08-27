#Unit converter
def length_converter(value,old_unit,new_unit):
    units = {"m" : 1,"cm" : 0.01,"km":1000}
    return value* units[old_unit]/units[new_unit]
def weight_converter(value,old_unit,new_unit):
    units = {"g": 1,"kg" : 1000}
    return value* units[old_unit]/units[new_unit]
def temperature_converter(value,old_unit,new_unit):
    if old_unit == "C" and new_unit == "F":
        return (value* 9/5)+32
    elif old_unit == "F" and new_unit == "C":
        return (value-32)*5/9
    elif old_unit == "C" and new_unit == "K":
        return (value)+273
    elif old_unit == "K" and new_unit == "C":
        return (value)-273
    elif old_unit == "F" and new_unit == "K":
        return (value-32)*5/9 +273
    elif old_unit == "K" and new_unit == "F":
        return (value-273)*9/5 +273
    else:
        return value

print("WELCOME TO UNIT CONVERTER!")
category = input("Enter category (length/weight/temperature):").lower()
if category == "length":
    value = float(input("Enter value:"))
    old_unit = input("From (m/cm/km):").lower()
    new_unit = input("To (m/cm/km):").lower()
    print("Converted:",length_converter(value,old_unit,new_unit))

elif category =="weight":
    value = float(input("Enter value:"))
    old_unit = input("From (g/kg):").lower()
    new_unit = input("To (g/kg):").lower()
    print("Converted:",weight_converter(value,old_unit,new_unit))

elif category == "temperature":
    value = float(input("Enter value:"))
    old_unit = input("From (K/F/C):").upper()
    new_unit = input("To (K/F/C):").upper()
    print("Converted:",temperature_converter(value,old_unit,new_unit))
else:
    print("Invalid category.")