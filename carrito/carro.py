# -*- coding: utf-8 -*-
class Carro():
    def __init__(self,request):
        self.request=request
        self.session=request.session
        self.carro=self.session.get('carro')        
        
        if not self.carro:
            self.carro=self.session['carro']={}
        
        
        
    def agregar(self,producto):
            
       if str(producto.id) not in self.carro.keys() :
           self.carro[producto.id]={
                    'producto_id':producto.id,
                    'nombre':producto.nombre,
                    'precio':str(producto.precio),
                    'cantidad':1,
                    
                                }

       else:
                
            self.carro[str(producto.id)]['cantidad']+=1  
            
        
       self.guardar_carro()
            
            
        
    def guardar_carro(self):
        self.session['carro']=self.carro
        self.session.modified=True
            
    def eliminar(self,producto):
            
        if str(producto.id)  in self.carro:
           del self.carro[str(producto.id)]
                
           self.guardar_carro()
        
        
    def restar(self,producto):
            
        if  str(producto.id) in self.carro:
   
           self.carro[str(producto.id)]['cantidad']-=1
        if self.carro[str(producto.id)]['cantidad']==0:
            del self.carro[str(producto.id)]
        
        self.guardar_carro()
                
                
    def limpiar(self):
         self.session['carro']={}
         self.carro=self.session['carro']
         self.guardar_carro()