'''
Ask user to enter the number tell tha user whether the number is
positive,negative or zero
'''
user = int (input("Enter the Number:"))
if user>=1:
    print("positive")
elif user == 0:
    print("zero")
else :
    print("negative")

'''
display three strings "name","is","moorthy" as output is "name**is**moorthy"
'''
print("name","is",end = "**",sep = "**")
print("moorthy",sep = "**")

# display float number with 2 decimal place using print()

ph_rating = float(input("Enter the rating:"))
print("%.2f" % ph_rating)
