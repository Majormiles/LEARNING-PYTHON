
import random 

name_list = ['Asigbey Ezekiel Kofi','Kpotor Seth Mawunya',
            'Atali Edwin Edudzi','Atula Sylvia',
            'Kpanazo Godwin','Atsyatsya Samuel',
            'Agroh Felix','Tsonyake Elikplim',
            'Okyere Prosper','Akoto Ernest',
            'Obeng clinton','Paa Kwesi Bartels',
            'Akakpo Ernest K.M','Akotey Precious',
            'Enoch kwame','Agbozo Theodore',
            'Emmanuel Tokoli','Nabil Ablorh',
            'Tettevia Sonidhi Sefakor','Nubor Kwame Eric',
            'Israel Setugah','Letsu Emmanuel Joe','Sitty Collins']
already_selected = ['Sitty Collins','Ekpe Federick',
              'Kpanazo Godwin','Edor Ignatus',
              'Isaac','Precious']


##x = random.choice(FirstNames)
##
##
##def SecondNames():
##    return none;
##print()
##print()
##print("!!..........PYTHON PROGRAMMING CLASS........!!")
##print()
##print("Hello! "+x+", You would be leading us in Today's Python programming exercise. Thanks!")


person = random.choice(name_list)
if person in already_selected:
    name_list.remove(person)
    print("Hello!" + person+", you've already lead us.")

else:
    print("Hello! " + person+ ", you're leading us today.")



