# coding=utf-8
print((4+8)/2)

print(8 / 4)
print( 6 * 7.0 )
print (4 + 1.65)

print(1+2+3+4.0 + 5)

print( 2**6)
print( 9 ** (0))
print(8 ** (1/3))

print( 20 // 6)
print( 20 // 7)

print( 20 % 6)
print(1.25 % 0.5)

print( 9 // 2)
print(7% (5//2 ))

x=(3**2)
print(type(x))

# STIRNGS

print("Python is fun")
print('Python is fun')
#// 'I\'m'

print('characters can\'t be directly included in a string')

# new lines

print('One\nTwo\nThree')
# Similarly, \t represents a tab
print('One\tTwo\tThree')

print("""This
is a
multiline
text""")
#Concatenation

print("Spam" + 'eggs') #spameggs
print("2" + "2") #str Adding a string to a number produces an error, as even though they might look similar, they are two different entities.

#String Operations
#Strings can't be multiplied by other strings. Strings also can't be multiplied by floats, even if the floats are whole numbers.
print("spam" * 3) # ==> spamspamspam
print(4 * '2') # ==> 2222

# Variables переменные main/īgie

user = "Valerijs"
print(user)

age = 42
print(age)

# Variable Names
#Python is a case sensitive programming language. Thus, Lastname and lastname are two different variable names in Python.

this_is_a_normal_name = 7
print(this_is_a_normal_name)

#123abc = 7
#print(123abc)  ==> SyntaxError: invalid syntax

#Working with Variables

x = 7
print(x) # ==> 7
print(x + 3) # ==> 10
print(x) #==> 7

spam = "eggs"
print(spam * 3) # ==> eggseggseggs

x = "This is Sparta"
print(x + "!") # ==> This is Sparta!

x = 5
y = 7
print(x + y) #==> 12

# Input

#x = input()
#print(x) # input number 33 ==> result 33

#name = raw_input("Enter your name: ")
#print("Hello, " + name) #Python2

#Python 3
#name = input("Enter your name: ")
#print("Hello, " + name) # ==> WORK

#age = int(input()) #To convert it to a number, we can use the int() function:
#print(age)

#age = 32
#print("My age is " + str(age))

#You can convert to float using the float() function

#age = float(input())
#print(age)

x = "2"
y = "4"
z = int(x) + int(y)
print(z)

#name = input()
#age = input()
#print(name + " is " + age)

#In-Place operators

x = 2
print(x)
x += 4   # ==> x=x+4 ==> x += 3
print(x)

x = 4
x *= 3
print(x)

x = "spam"
print(x)
x += "eggs"
print(x)

x = "a"
x *= 3
print(x)

#Walrus operator

#num = int(input("Please enter number: "))
#print(num) #enter 22 ==> result 22

#print(int(input("Please enter number: ")))

spam = "7"
spam = spam + "0" # ==> "70"
eggs = int(spam) + 3 # ==> 70+3 = 73
print(float(eggs)) #==> 73.0


#age = int(input())
#print(age+8)

x = 5
y = x + 3
y = int(str(y) + "2")
print(y)

x = 3
num = 17
print(num % x)

#Simple Calculator
x = int(input())
y = int(input())
z = x + y
print(z)