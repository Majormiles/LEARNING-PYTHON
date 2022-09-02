import random

name_list =['Seth Mawunya', 'Sylvia Azuma', 'Okyere Prosper']

already_selected = ['Sitty Collins','Ekpe Federick',
              'Kpanazo Godwin','Edor Ignatus',
              'Isaac','Precious']

person = random.choice(name_list)
if person in already_selected:
    name_list.remove(person)
    print("Hello!" + person+", you've already lead us.")

else:
    print("Hello! " + person+ ", you're leading us today.")
