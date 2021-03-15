from django.urls import include, path
from app.views import PrivilegeApi, PrivilegeDetailApi, RoleApi, RoleDetailApi, PersonApi, PersonDetailApi, \
DataApi, DataDetailApi, ExampleApi, ExampleDetailApi


privilege_patterns = [
    path('', PrivilegeApi.as_view()),
    path('<int:pk>/', PrivilegeDetailApi.as_view()),
]

role_patterns = [
    path('', RoleApi.as_view()),
    path('<int:pk>/', RoleDetailApi.as_view()),
]

person_patterns = [
    path('', PersonApi.as_view()),
    path('<int:pk>/', PersonDetailApi.as_view()),
]

data_patterns = [
    path('', DataApi.as_view()),
    path('<int:pk>/', DataDetailApi.as_view()),
]

example_patterns = [
    path('', ExampleApi.as_view()),
    path('<int:pk>/', ExampleDetailApi.as_view()),
]
