from django.shortcuts import render
from .models import Project, Program_Language, Technology_Skills, Soft_Skills, Framework_Skills, Education, Experience
import os
# Create your views here.

def homePage(request):
    projects = Project.objects.all()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'index.html')
    return render(request, template_path)
    

def about(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'about.html')
    return render(request, template_path)
    

def projects(request):
    projects = Project.objects.all()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'projects.html')
    return render(request, template_path,{'projects':projects})
    

def skills(request):
    Program_language = Program_Language.objects.all()
    Technology = Technology_Skills.objects.all()
    Soft_skills = Soft_Skills.objects.all()
    Framework = Framework_Skills.objects.all()

    Program_language_list = list(Program_language)
    Program_language_list_count = (len(Program_language_list)+1)//2
    Program_language_list_1 = Program_language_list[:Program_language_list_count]
    Program_language_list_2 = Program_language_list[Program_language_list_count:]

    Technology_list = list(Technology)
    Technology_list_count =(len(Technology_list)+1)//2
    Technology_list_1 = Technology_list[:Technology_list_count]
    Technology_list_2 = Technology_list[Technology_list_count:]

    Soft_skills_list = list(Soft_skills)
    Soft_skills_list_count = (len(Soft_skills_list)+1)//2
    Soft_skills_list_1 = Soft_skills_list[:Soft_skills_list_count]
    Soft_skills_list_2 = Soft_skills_list[Soft_skills_list_count:]

    Framework_list = list(Framework)
    Framework_list_count = (len(Framework_list)+1)//2
    Framework_list_1 = Framework_list[:Framework_list_count]
    Framework_list_2 = Framework_list[Framework_list_count:]

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'skills.html')
    return render(request, template_path,{'Program_language_list_1': Program_language_list_1,'Program_language_list_2':Program_language_list_2,
                                               'Technology_list_1':Technology_list_1,'Technology_list_2':Technology_list_2,
                                               'Soft_skills_list_1':Soft_skills_list_1,'Soft_skills_list_2':Soft_skills_list_2,
                                               'Framework_list_1':Framework_list_1,'Framework_list_2':Framework_list_2})


def education(request):
    education = Education.objects.all()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'education.html')
    return render(request, template_path, {'education':education})
    

def experience(request):
    experiences = Experience.objects.all()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'experience.html')
    return render(request, template_path, {'experiences':experiences})
    
