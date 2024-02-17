from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    #thumbnail = 
    body = models.TextField()
    #slug = models.SlugField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    
class Program_Language(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.IntegerField(default=50)
    #body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    
class Technology_Skills(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.IntegerField(default=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    
class Framework_Skills(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.IntegerField(default=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    
class Soft_Skills(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.IntegerField(default=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.name
    

class Education(models.Model):
    collage = models.CharField(max_length=200,null=True)
    image = models.CharField(max_length=200,null=True)
    degree = models.CharField(max_length=200,null=True)
    major = models.CharField(max_length=200,null=True)
    date = models.CharField(max_length=200,null=True)
    gpa = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.collage
    

class Experience(models.Model):
    title = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True)
    start = models.CharField(max_length=200,null=True)
    end = models.CharField(max_length=200,null=True)
    detail = models.TextField()
    def __str__(self):
        return self.title