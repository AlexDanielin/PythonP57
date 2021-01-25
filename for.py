# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:29:11 2021

@author: alexp
"""
listasw=[]
listaro=[]
listaot=[]
lista=["R1",'R2','R3',
       'R4','R5',
       'S1','S2','S3',
       'TV','LAPIZ','HOJA']
for i in lista:
    if 'R' in i:
        listaro.append(i)
    elif "S" in i:
        listasw.append(i)
    else:
        listaot.append(i)
print("Routers: ",listaro,
      "Switches: ",listasw,
      "Otros: ",listaot)
  
    