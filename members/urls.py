from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
       path('otherpage/', views.home, name='home'),
         path('', views.loginmain, name='loginmain'),

    path('memberdisplay/', views.displaymembers, name='showmembers'),
    path('adddata/', views.addmembersdata, name='addmembersdata'),
    #config page
        path('configpage2/', views.dataadmin, name='configdata'),
         path('configpage/', views.searchme, name='searchdata'),
         
         #EDIT MEMBERS
         path('editpage/<int:pk>', views.edit, name='editmembers'),
         #MARK AS DONE
          path('markdone/<int:pk>', views.markasdone, name='markasdonename'),
               #MARK AS UNDONE
          path('markundone/<int:pk>', views.markasundone, name='markasundonename'),
                #delete record
          path('delete/<int:pk>', views.deleterecord, name='deleterecord'),
           
                 #LOIGN PAGE
          path('loginpage/', views.login, name='loginpage'),

                 #reset ALL records
          path('reset/', views.reset, name='resetall'),
                    path('test/', views.reset, name='test'),
       path('archive/', views.archive, name='archive'),
] 

