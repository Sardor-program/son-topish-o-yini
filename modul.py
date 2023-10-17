# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:40:45 2023

@author: hp
"""


import random 

def computer():
    son = random.randint(1, 10)
    print("Men 1 dan 10 gacha son o'yladim topishga harakat qilib ko'ring\n  ")
    urunish = 0
    while True:
        inp = int(input(">>> "))
       
        if inp == son:
            print(f"Tabriklayman men o'ylagan son {son} soni edi. {urunish} urunishda topdingiz. ")  
            break
        elif son > inp:
            print(f"Men o'ylagan son {inp} dan katta")
            urunish += 1
        elif son < inp:
            print(f"Men o'ylagan son {inp} dan kichik")
            urunish += 1