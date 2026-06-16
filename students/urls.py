from django.urls import path
from .views import signup, home, edit_student, delete_student

urlpatterns = [
    path('', signup, name='signup'),
    path('home/', home, name='home'),
    path('edit/<int:id>/', edit_student),
    path('delete/<int:id>/', delete_student),
]