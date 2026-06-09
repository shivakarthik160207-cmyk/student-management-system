from django.urls import path
from .views import home, edit_student, delete_student

urlpatterns = [
    path('', home),
    path('edit/<int:id>/', edit_student),
    path('delete/<int:id>/', delete_student),
]