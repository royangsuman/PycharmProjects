'''
Program : Enemy Calculator
Author : Angsuman Roy
'''
import random

class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print(self.atkl)


    def getHp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40,20)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(50,70)     
enemy2.getAtk()       
enemy2.getHp()        