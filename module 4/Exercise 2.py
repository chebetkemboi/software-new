cabin_class = input("Enter the cabin class  (LUX, A, B, or C): ")
print("cabin_class")

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("cabin above the car deck with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("invalid cabin class.")
    
