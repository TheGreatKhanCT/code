import random
print("odd numbers")
counting = 0
while counting < 10:
    #get a random number
    number = random.randint(1,999)
    if int(number/2) == number/2:
        #if its an even number, dont print it
        continue
    # otherwise, if odd, print and increment counter
    print(number)
    counting += 1
print("loop is done")

print("Numbers that aren't evenly divisible by 5")
counter = 0
while counter < 10:
# Get a random number
    number_one = random.randint(1,999)
    if int(number_one / 5) == number_one / 5:
# If it's evenly divisible by 5, bail out.
        break
# Otherwise, print it and keep going for a while.
    print(number_one)
# Increment the loop counter.
    counter += 1
print("Loop is done")



#answers = ["A", "C", "B", "D"]
#for answer in answers:
#    if answer == "":
#        print("Incomplete")
#        break
#    print(answer)
#print("Loop is done")

#answers_two = ["A", "C", "", "D"]   # here the break gets used, because there is a " " between c and d
#for answer in answers_two:
 #   if answer == "":
 #       print("Incomplete")
  #        break                   
  #  print(answer)
#print("Loop is done")

# nested loops
# outer loop
#for outer in ['first','second','third']:
#    print(outer)
    # inner loop
#    for inner in range(3):
#        print(inner+1)
#print('both loops are done')

#counter = 65
#while counter < 91:
#    print(str(counter)+"-"+chr(counter)) # The chr() function inside the loop displays the ASCII character for the counter
#    counter += 1
