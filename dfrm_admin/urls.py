# main/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

# define the router
router = routers.DefaultRouter()
# define the router path and viewset to be used
router.register(r'employee', views.EmployeeViewSet, basename="api_employee")
#router.register(r'facility', views.FacilityViewSet, basename="api_facility")
router.register(r'department', views.DepartmentViewSet, basename="api_department")
router.register(r'division', views.DivisionViewSet, basename="api_division")
#router.register(r'project', views.ProjectViewSet, basename="api_project")
router.register(r'subproject', views.SubprojectViewSet, basename="api_subproject")
router.register(r'task', views.TaskViewSet, basename="api_task")

facility_list = views.FacilityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

facility_detail = views.FacilityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

all_facility_points = views.FacilityViewSet.as_view({
    'get': 'all_points'
})

facility_points = views.FacilityViewSet.as_view({
    'get': 'points'
})

project_list = views.ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_detail = views.ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

project_subprojects = views.ProjectViewSet.as_view({
    'get': 'subprojects'
})

project_tasks = views.ProjectViewSet.as_view({
    'get': 'tasks'
})

project_points = views.ProjectViewSet.as_view({
    'get': 'points'
})

project_linestrings = views.ProjectViewSet.as_view({
    'get': 'linestrings'
})

project_polygons = views.ProjectViewSet.as_view({
    'get': 'polygons'
})

urlpatterns = [
    path('', views.home, name='home'),


    path('department/list/', views.department_list, name = 'department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/new/', views.department_new, name='department_new'),
    path('department/<int:pk>/edit/', views.department_edit, name='department_edit'),

    path('division/', views.division, name='division'),
    path('division/list/', views.division_list, name='division_list'),
    path('division/<int:pk>/', views.division_detail, name='division_detail'),
    path('division/new/', views.division_new, name='division_new'),
    path('division/<int:pk>/edit/', views.division_edit, name='division_edit'),

    path('project/', views.project, name='project'),
    path('project/list/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),

    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),

    path('facility/', views.facility, name = 'facility'),
    path('facility/list/', views.facility_list, name = 'facility_list'),
    path('facility/<int:pk>/', views.facility_detail, name='facility_detail'),
    path('facility/new/', views.facility_new, name = 'facility_new'),
    path('facility/<int:pk>/edit/', views.facility_edit, name='facility_edit'),
    
    path('employee/list/', views.employee_list, name='employee_list'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),

    #APIs
    path('api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls')),
    
    path('api/facility/', facility_list, name='api_facility'),
    path('api/facility/<int:pk>/', facility_detail, name='api_facility_detail'),
    path('api/facility/points/', all_facility_points, name='api_all_facility_points'),
    path('api/facility/<int:pk>/points/', facility_points, name='api_facility_points'),


    path('api/project/', project_list, name='api_project'),
    path('api/project/<int:pk>/', project_detail, name='api_project_detail'),
    path('api/project/<int:pk>/subprojects/', project_subprojects, name='api_project_subprojects'),
    path('api/project/<int:pk>/tasks/', project_tasks, name='api_project_tasks'),
    path('api/project/<int:pk>/points/', project_points, name='api_project_points'),
    path('api/project/<int:pk>/linestrings/', project_linestrings, name='api_project_linestrings'),
    path('api/project/<int:pk>/polygons/', project_polygons, name='api_project_polygons'),

]