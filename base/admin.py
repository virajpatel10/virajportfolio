from django.contrib import admin
from .models import Project, Program_Language, Technology_Skills, Soft_Skills, Framework_Skills, Education, Experience
# Register your models here.

admin.site.register(Project)
admin.site.register(Program_Language)
admin.site.register(Technology_Skills)
admin.site.register(Soft_Skills)
admin.site.register(Framework_Skills)
admin.site.register(Education)
admin.site.register(Experience)