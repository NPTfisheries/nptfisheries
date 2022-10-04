# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('division/', views.division, name='division'),
    path('division/<int:pk>/', views.division_detail, name='division_detail'),
    path('division/new/', views.division_new, name='division_new'),
    path('division/<int:pk>/edit/', views.division_edit, name='division_edit'),

    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),

    path('office/', views.office, name = 'office'),
    path('office/<int:pk>/', views.office_detail, name='office_detail'),
    path('office/new/', views.office_new, name = 'office_new'),
    path('office/<int:pk>/edit/', views.office_edit, name='office_edit'),
    
    path('employee/', views.employee, name='employee'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
]