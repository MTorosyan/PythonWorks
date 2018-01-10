#Create a function that will print the numbers 1 to 100, however if the number is a multiple of 3 print fizz, if a multiple of 5 print buzz. If it is a multiple of 3 and 5 print FizzBuzz
#Print output to console and to a file

#Python 3.6
import os

#function to determine what to print
def fizzbuzzcheck(i):
    #Checks for multiple of both 5 and 3 first
    if i % 5 == 0 and i % 3 == 0:
        return "FizzBuzz"
    #Check for multiple of 5
    elif i % 5 == 0:
        return "Buzz"
    #Check for multiple of 3
    elif i % 3 == 0:
        return "Fizz"
    else:
        return i

filepath = os.getcwd()
filepath = os.path.join(filepath, "1.FizzBuzz", "Result.txt")
print("File will be written to: " + filepath)
#Overwrite file
fileVar = open(filepath, "w+")
fileVar.write("This is the output of the fizzbuzz program:")
fileVar.close()
fileVar = open(filepath, "a+")

for numCount in range(1, 101):
    functionout = fizzbuzzcheck(numCount)
    print(functionout)
    fileVar.write("\n")
    fileVar.write(str(functionout))

fileVar.close()
