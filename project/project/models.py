from django.db import models

     
#note= models.IntegerField(max_length=255)
    
     

class Ue(models.Model):
    mat_ue=models.CharField(max_length=255)
    nom_ue=models.CharField(max_length=255)

class Ec(models.Model):
    mat_ec=models.CharField(max_length=255)
    nom_ec=models.CharField(max_length=255,null=True)
    credit=models.CharField(max_length=255,null=True)
    note= models.IntegerField(null=True)
    ue= models.ForeignKey(Ue,  on_delete=models.CASCADE,null=True)

class Etudiant (models.Model):
     mat_etud=models.CharField(max_length=255)
     nom=models.CharField(max_length=255)
     ec=models.ManyToManyField(Ec,related_name='etudiant',blank=True)
     date_naiss=models.DateField(null=True)
     decision=models.CharField(max_length=255,null=True)    
class Excelfile(models.Model):
    file=models.FileField( upload_to="excel")

    


       
    
    

    
   
    
     