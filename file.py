print("hello world")
print(7)
print("Bye")

name= "sakshi"
friend= "shatakshi"
anotherfriend='divya'
apple='''He said,
hey sakshi
i am good
"I want to eat apple'''
print("Hello," +name)
#print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

names=("Sakshi,divya")
print(name[0:6])

fruit="Mango"
mangolen=len(fruit)
print(mangolen)
print(fruit[0:5])
print(fruit[:4])
print(fruit[-3:-1])

a="!!!Harry!! !!!!!!!!! Harry "
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))
blogHeading="introduction to js"
print(blogHeading.capitalize())

str1="welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1="welcome to the console!!!"
print(str1.endswith ("!!!"))
str1="welcome to the console !!!"
print(str1.endswith("+",4,10))
str1="He's name is Dan.He is an honest man."
print(str1.find("ishh"))
#print(str.index("ishh"))
str1="WelcomeToTheConsole"
print(str1.isalnum())
str1="welcome"
print(str1.isalpha())
str1="hello world"
print(str1.islower())
str1="we wish you a merry christmas\n"
print(str1.isprintable())
str1="  " #using spacebar
print(str1.isspace())
str2="  " #using tab
print(str2.isspace())
str1="World Health Organization"
print(str1.istitle())
str2="To kill a Mocking bird"
print(str2.istitle())
str1="Python is a Interpreted Language"
print(str1.startswith("Python"))
str1="Python is a Interpreted Language"
print(str1.swapcase())
str1="His name is Dan. Dan is a honest man."
print(str1.title())