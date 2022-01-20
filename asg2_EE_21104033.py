#question1
print("\nQuestion 1")
inputString = "Python is a case sensitive language"
    #part a.
print(len(inputString))
    #part b.
print(inputString[::-1])
    #part c.
newString = inputString[10:-9]
print(newString)
    #part d.
newString = inputString[0:10] + "object oriented" + inputString[-9:len(inputString)]
print(newString)
    #part e.
print(inputString.index('a'))
    #part f.
print(inputString.replace(" ",""))

#question2
print("\nQuestion 2")
studentName = "Ashutosh Taneja"
studentSID = 21104033
studentDeptName = "Electrical"
studentCGPA = 9.9
print("Hey, %s Here!"%studentName)
print("My SID is %d"%studentSID)
print("I am from %s department and my CGPA is %.1f"%(studentDeptName,studentCGPA))

#question3
print("\nQuestion 3")
a = 56
b = 10
    #part a.
print(a&b)
    #part b.
print(a|b)
    #part c.
print(a^b)
    #part d.
print(a << 2)
print(b << 2)
    #part e.
print(a >> 2)
print(b >> 4)

#question4
print("\nQuestion 4")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

maximumNumber = [a,b,c]
print("The maximum of the three numbers is %f"%max(maximumNumber))

#question5
print("\nQuestion 5")
inputString = input("Enter the string: ")
if "name" in inputString:
    print("Yes")
else:
    print("NO")

#question6
print("\nQuestion 6")
sideA = int(input("Enter length of side A:"))
sideB = int(input("Enter length of side B:"))
sideC = int(input("Enter length of side C:"))
if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print("Yes")
else:
    print("No")
    
    
