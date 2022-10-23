# main/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

# define the router
router = routers.DefaultRouter()
# define the router path and viewset to be used
router.register(r'project', views.ProjectViewSet)
router.register(r'point', views.PointViewSet, basename='api_point')
router.register(r'linestring', views.LinestringViewSet, basename='api_linestring')
router.register(r'polygon', views.PolygonViewSet, basename='api_polygon')


urlpatterns = [
    path('', views.home, name='home'),

    path('department/', views.department, name = 'department'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/new/', views.department_new, name='department_new'),
    path('department/<int:pk>/edit/', views.department_edit, name='department_edit'),

    path('division/', views.division, name='division'),
    path('division/<int:pk>/', views.division_detail, name='division_detail'),
    path('division/new/', views.division_new, name='division_new'),
    path('division/<int:pk>/edit/', views.division_edit, name='division_edit'),

    path('project/', views.project, name='project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),

    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),

    path('facility/', views.facility, name = 'facility'),
    path('facility/<int:pk>/', views.facility_detail, name='facility_detail'),
    path('facility/new/', views.facility_new, name = 'facility_new'),
    path('facility/<int:pk>/edit/', views.facility_edit, name='facility_edit'),
    
    path('employee/', views.employee, name='employee'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),

    #APIs
    path('api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls')),
]