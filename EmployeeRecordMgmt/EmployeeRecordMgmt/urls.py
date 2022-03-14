from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('emp_login/', emp_login, name='emp_login'),
    path('emp_home/', emp_home, name='emp_home'),
    path('profile/', profile, name='profile'),
    path('logout/', Logout, name='logout'),
    path('admin_login/', admin_login, name='admin_login'),
    path('my_experience/', my_experience, name='my_experience'),
    path('edit_experience/', edit_experience, name='edit_experience'),
    path('my_education/', my_education, name='my_education'),
    path('edit_myeducation/', edit_myeducation, name='edit_myeducation'),
    path('change_password/', change_password, name='change_password'),
    path('admin_home/', admin_home, name='admin_home'),
    path('change_passwordadmin/', change_passwordadmin, name='change_passwordadmin'),
    path('all_employee/', all_employee, name='all_employee'),
    path('delete_employee/<int:pid>', delete_employee, name='delete_employee'),
    path('edit_profile/<int:pid>', edit_profile, name='edit_profile'),
    path('edit_education/<int:pid>', edit_education, name='edit_education'),
    path('edit_experiencee/<int:pid>', edit_experiencee, name='edit_experiencee'),
    
]
