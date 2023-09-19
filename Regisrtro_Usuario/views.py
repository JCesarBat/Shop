from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

class VRegistro(View):
    
    def get(self,request):
        form=UserCreationForm()
        
        return render(request,'Regisrtro_Usuario/Plantillas/Formulario_Registro.html',{'form':form,'llave':'Registro'})
    
    def post(self,request):
        
        form=UserCreationForm(request.POST)
        if form.is_valid():
            
            usuario=form.save()
            login(request,usuario)
            return redirect('home')
        else:
          for msg in form.error_messages:
              messages.error(request,form.error_messages[msg])
         
              
        return render(request,'Regisrtro_Usuario/Plantillas/Formulario_Registro.html',{'form':form,'llave':'Registro'})

def cerrar_session(request):
    logout(request)
    
    return redirect('home')

def logear(request):
    form=AuthenticationForm()
    if request.method=='POST' :
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre=request.POST.get('username')
            contra=request.POST.get('password')
            
            usuario=authenticate(username=nombre,password=contra)
            
            if usuario is None:
                for msg in form.error_messages:
                    messages.error(request,form.error_messages[msg])
                    return render(request,'Regisrtro_Usuario/Plantillas/Formularilogin.html',{'form':form,'llave':'Iniciar Session'})
            else:
                login(request, usuario)
                return  redirect('home')

    return render(request,'Regisrtro_Usuario/Plantillas/Formularilogin.html',{'form':form,'llave':'Iniciar Session'})