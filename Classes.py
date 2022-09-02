class Human():
    def __init__(self,name,gender,height) :
        self.p_name =name
        self.p_gender =gender
        self.n_height =height
        
    #Defining a method
    def talk(self) :
        if self.p_gender == "M" :
            pnoun = "He"
        elif self.p_gender =="f" :
            pnoun = "She"
            return "{} said mama""\n{} is a male""\n{} likes cooking". format(self.p_name,pnoun,pnoun)
        
first_human =  Human("adam ","f","6ft")
second_human = Human("Godwin ","f","5ft")
Third_human = Human("Ben ","f","6ft")

print (first_human.talk())
print (second_human.talk())
print (Third_human.talk())
