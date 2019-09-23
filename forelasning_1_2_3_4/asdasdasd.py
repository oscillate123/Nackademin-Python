# (a) capitalize()
# (b) join()
# (c) lower()
# (d) upper()
# (e) swapcase()
# (f) replace()
# (g) split()
# (h) rsplit()
# (i) title()
# (j) format()



txt = "apple, banana, cherry"
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)


myTuple = ("John", "Peter", "Vicky")
myTuple2 = ("smh",)
x = myTuple + myTuple2
x = " ".join(x)
x = x.replace("smh", "")
print(x)

txt2 = "My name is {0}, I'am {1}".format("John",36)
print(txt2)