import datetime as dt
datelist = []                               #create empty list for dates
datelist.append(dt.date(2020,12,31))        #append dates one at the time so code is easier to read
datelist.append(dt.date(2019,1,31))
datelist.append(dt.date(2018,2,28))
datelist.append(dt.date(2020,1,1))
datelist.sort()                             #sort the dates (earliest to latest) and show formatted in mm/dd/YYYY
for date in datelist:
    print(f"{date:%m/%d/%Y}")

# Create a list of strings.
grades = ["C", "B", "A", "D", "C", "B", "C"]
# Decide what to look for
look_for = "F"
# See if the item is in the list.
if look_for in grades:
# If it's in the list, get and show the index.
    print(str(look_for) + " is at index " + str(grades.index(look_for)))
else:
# If not in the list, don't even try for index number.
    print(str(look_for) + " isn't in the list.")
print(grades)
grades.sort()
print(grades)

names = ["Zoltan", "Geralt", "Mortal", "Cait", "Xena"]  #list of strings
copy_names = names.copy()                               #copy and reverse the list
copy_names.reverse()
print(names)
print(copy_names)
