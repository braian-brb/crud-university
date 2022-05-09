from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('registerCourse/', views.registerCourse),
    path('deleteCourse/<code>', views.deleteCourse),
    path('courseEdition/<code>', views.courseEdition),
    path('editCourse/', views.editCourse),
]