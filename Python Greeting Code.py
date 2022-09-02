import random
import datetime






greeting = ['Hello', 'Sup', 'Hola', 'Hi', 'Greetings', 'Name']
mike = ["Hope you're having a greet week!", "Hope you're having a great day!", "Hope you're doing well!"]
#MAKING AN INPUT
name = input("> What is your name? ")

#CALLING THE RANDOM MODULE

value1 = random.choice(greeting)
value2 = random.choice(mike)

#CREATING A FUNCTION

def greet_user():
    print('> ' + value1 + ', ' + name + '! ')
    print('> ' + value2)
print(greet_user())

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
