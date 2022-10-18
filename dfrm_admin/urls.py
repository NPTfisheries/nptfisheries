# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('department/', views.division, name='department'),
    path('department/new/', views.division_new, name='department_new'),
    path('department/<int:pk>/edit/', views.division_edit, name='department_edit'),

    path('division/', views.division, name='division'),
    path('division/<int:pk>/', views.division_detail, name='division_detail'),
    path('division/new/', views.division_new, name='division_new'),
    path('division/<int:pk>/edit/', views.division_edit, name='division_edit'),

    path('project/', views.division, name='project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),

    path('facility/', views.facility, name = 'facility'),
    path('facility/<int:pk>/', views.facility_detail, name='facility_detail'),
    path('facility/new/', views.facility_new, name = 'facility_new'),
    path('facility/<int:pk>/edit/', views.facility_edit, name='facility_edit'),
    
    path('employee/', views.employee, name='employee'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
]