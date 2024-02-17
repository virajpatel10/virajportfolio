from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage, name="home"),
    path('about',views.about, name="about"),
    path('projects',views.projects, name="projects"),
    path('skills',views.skills, name="skills"),
    path('education',views.education, name="education"),
    path('experience',views.experience, name="experience")
]
