a=input(" enter the string")
count = 0;
#Counts each character except space
for i in range(0, len(a)):
 if(a[i] != ' '):
    count = count + 1;
#Displays the total number of characters present in the given string
print("Total number of characters in a string: " + str(count));
