# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:45:24 2023

@author: JC
"""

def importe_total_carro(request):
    total=0
    diccionario={}
    diccionaro_mandar={}
    if request.user.is_authenticated:
        
        if  'carro'in request.session.keys():
            
            
            for key, value in request.session["carro"].items():
                total=float(value['precio'])*float(value['cantidad'])+total
                diccionario[value['producto_id']]=float(value['precio'])*float(value['cantidad'])
        
    else:
        
        return diccionaro_mandar
    
    
    diccionario['importe_carro']=total
    diccionaro_mandar['diccionario']=diccionario
    return diccionaro_mandar