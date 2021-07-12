# -------------------------------------------
def sum():
    print(12+13)
sum()

# -------------------------------------------------
def welcome():
    print("welcome to function")
welcome()

# -----------------------------------------------------
def even():
    if (12%2==0):
        print("even number")
    else:
        print("odd number")
even()


# ----------------------------------------------------------
def greet(*names):
    for name in names:
        print("welcome",name)
greet ("rinki","vishal","kartik","bijendar")



# -----------------------------------------------------------
def info(name,age):
    print(name+"is"+age+"years old")
info("sonu","16")
info("sana","17")
info("umesh","18")



# -----------------------------------------------------------------
def studentdetails(name,currentmilestone,mentorName):
   print("hello",name,"your",currentmilestone,"concept","is clear with the help of",mentorName)
studentdetails("neelam","loop","amla")