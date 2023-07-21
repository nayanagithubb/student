from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.addstudent,name='addstudent'),
    path('addstudentdetails',views.addstudentdetails,name="addstudentdetails"),
    path('showstudent',views.showstudent,name="showstudent"),
    path('showstudentdetails/<int:pk>',views.showstudentdetails,name='showstudentdetails'),
    path('editstudentpage/<int:pk>',views.editstudentpage,name="editstudentpage"),
    path('editstudentdetails/<int:pk>',views.editstudentdetails,name="editstudentdetails"),
    path('deletepage/<int:pk>',views.deletepage,name="deletepage"),
    path('studentcard',views.studentcard,name="studentcard")
]
   
