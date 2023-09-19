# -*- coding: utf-8 -*-
class Session():
        def __init__(self):
            self.diccio={}
            
               
        
        def get(self,valor):
            if valor in self.diccio.keys() :
                return self.diccio[valor]
            
            return None
        
        
        
        

session=Session()




class Carro :
    def __init__(self):
        
        self.carro=session.get('carrito')
        if self.carro==None:
            self.carro=session.diccio['carrito']={}
            
    def agregar(self,valor):
        self.carro[str(valor)]={
            'r1':4
            }
            


carro=Carro()

carro.agregar('prueva')
        


print(carro.carro)