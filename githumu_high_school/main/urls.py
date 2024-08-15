from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('administration/', views.administration, name='administration'),
    path('teaching-staff/', views.teaching_staff, name='teaching_staff'),
    path('achievements/', views.achievements, name='achievements'),
    path('academics/', views.academics, name='academics'),
    path('academics/<int:holiday_id>/',views.holiday,name='holiday'),
    path('holiday/<int:grade_id>/',views.grades,name='grades'),
    path('grades/<int:assignment_id>/',views.assignments,name='assignments'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('search/', views.search, name='search'),
] 