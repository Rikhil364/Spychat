from Startchat import start_chat
from Spydetails import spy


print "Lets get started"
print "Do you want to continue as " + spy.salutation + " " + spy.name
existing_user = raw_input("enter y/n")
if(existing_user.upper() == "Y"):
    spy.name = spy.salutation + " " + spy.name
    print "Welcome Back " +" " +spy.name
    print "%s is your spy rating" % (spy.rating)
    print "Your age is : %s" % (spy.age)
    start_chat(spy.name,spy.age,spy.rating,spy.spy_is_online)

elif(existing_user.upper() == "N"):
    spy.name = raw_input("Welcome to spy chat, you must enter your name here: ")
    if len(spy.name)>0:
        spy.salutation = raw_input("should I call you Mr. or Mrs. :")
        spy.age = raw_input("What is your age")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating")
        spy.rating = float(spy.rating)

        spy_is_online = True
        print "Your authentication is verified %s %s\n Your seem to be a very young spy with an age of %s \n " % (spy.salutation,spy.name,spy.age)
        start_chat(spy.name,spy.age,spy.rating,spy.spy_is_online)
else:
    print 'wrong choice..!!'