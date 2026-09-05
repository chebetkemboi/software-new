gender = input("Enter biological gender (male/female): ")
gender = gender.lower()

hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

else:
    print("Invalid gender.")
    