
import os
import time
from asgiref.sync import sync_to_async
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,get_object_or_404
from .models import Etudiant,Ue,Ec,Excelfile
import pandas as pd
from threading import Thread
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View


from xhtml2pdf import pisa
from django.template.loader import get_template
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def index(request):
     
    return render(request,"login.html")
#chargement des données dans la base de donnée

def import_data(request):
    if request.method=='POST' :
        file= request.FILES['files']
        obj =Excelfile.objects.create(
            file=file
        )
        #path=file.file
        path=str(obj.file)
        df=pd.read_excel(path)
        df.fillna("0",inplace=True)
        
        #introduction des données dans la base de donnée
        #Ue
        
        df_ec=df.iloc[4].tolist()
        #df1=df_id.iloc[0].to_list()
        #df2=df_id.iloc[1].to_list()
        
       #fonction d'ajout
        col=[]  
        df_ec=df.iloc[4].tolist() #conversion en liste
        ec=df_ec[3:len(df_ec)-1]
        
        
        
        for i in range(5,len(df)):
            df2=df.iloc[i].to_list()
            
            etudiant=Etudiant()
            etudiant.mat_etud=df2[1]
            etudiant.nom=df2[2]
               # mat_etud=,
               # nom=df2[2],
                #decision=df2[len(df2)]
            #)
            etudiant.save()
            
                
                
            
        
            def proces_one():
                
                
            
                for  i in ec:
                    col.append(i)

                    time.sleep(0.01)
                    
            def proces_two():
                
            
                for u in df2[3:len(df2)-1]:  
                    col.append(u)
                   
                    time.sleep(0.01)
            th1=Thread(target=proces_one)
            th2=Thread(target=proces_two)
            th1.start()
            th2.start()
            th1.join()
            th2.join()
            col1=0
            col2=0
            for i in range(0,len(col)-1):
                
                if type(col[i])==str:
                    
                    col1=col[i]
                else:
                    
                    col2=col[i]
                    note=Ec.objects.create(
                         mat_ec=col1,
                         note=col2
                    )
                    note.save()
                    etudiant.ec.add(note)         
        etudiant = Etudiant.objects.all()
        context={
        'etudiant':etudiant,
         } 
     
    return render(request, 'corp/etudiant.html',context)
#generer pdf


def pdf(request,etud_id):
    etudiant= get_object_or_404(Etudiant, pk=etud_id)
    ec=etudiant.ec.all()
   
        
    template_path = 'pdf.html'

    context={
        'etudiant':etudiant,
        'ec' :ec ,
        
             
    }

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
        
def searh(request):
    query = request.GET.get('query')  # ici on recupere le query
    if not query:
        etudiant = Etudiant.objects.all()  # permet de tout afficher

    else:
        etudiant = Etudiant.objects.filter(
            nom__icontains=query)  # permet de comparer la valeur du query avec le title que celui ci qui prendre en compte lorsque on prend la majuscule et les mots a moitié
        if not etudiant.exists():
            etudiant = Etudiant.objects.filter(mat_etud__icontains=query)

    title = "resultat pour la requete %s" % query
    context = {
        'etudiant':etudiant,
        'title': title
    }
    return render(request, 'corp/etudiant.html', context)
def bull(request):
    return render(request, 'corp/bulletin.html')
def etudiant(request):
     etudiant = Etudiant.objects.all()
     context = {
        'etudiant':etudiant,
        
    }
     return render(request, 'corp/etudiant.html', context)
def test(request):
     return render(request,'pdf.html')
 
def signin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        #user1 = User.objects.filter(username=name, password=password)

        if user is not None:
             login(request, user)
            
           
             return render(request, 'index.html')
          
        else:
            
              return render(request, 'login.html') 
     
    
def acceuil(request):
    return render(request,'index.html')
def deconnexion(request):
    logout(request)
    messages.success(request, 'logout successfully!')
    return render(request,'login.html')