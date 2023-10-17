# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:41:46 2023

@author: hp
"""

import random


def inson():
    son = random.randint(1, 10)
    print("1 dan 10 gacha  son o'ylang va Enter tugmasini bosing men topishga harakat qilaman.")
    input()
    urunish1 = 0
    while True:
      
        biz = input(f"Siz {son} sonini o'yladingiz\nAgarda son to'g'ri bo'lsa To'g'ri (t) Katta(+)  Kichik(-) bosing>>> ")
        if biz == 't':
            print(f"Men {urunish1} urunishda topdim yutdim :( ")
            break
        elif biz == '+':
            son += 1
            urunish1 += 1
        elif biz == '-':
            son -= 1
            urunish1 += 1
        
           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            