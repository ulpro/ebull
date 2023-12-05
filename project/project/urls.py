
from django.contrib import admin
from django.urls import path
from.import views

app_name='project'
urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('',views.index,name="index"),
    path('accueil',views.acceuil,name="accueil"),
    path('form/',views.import_data,name="import_data"),
     path('login',views.signin,name="login"),
    path('bulletin/',views.bull,name="bull"),
    path('etudiant/',views.etudiant,name="etudiant"),
    path('<int:etud_id>/',views.pdf,name="pdf"),
     path('test/', views.test, name='test'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
    path('searh/', views.searh, name='searh'),
    
]
