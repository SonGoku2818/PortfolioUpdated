from django.db import models
import uuid
from .choices import  COLOR_CHOICES,EXPERIENCE_ICON
# Create your models here.
class BaseModel(models.Model):
    uid = models.CharField(max_length=100, default=uuid.uuid4)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True
        abstract
        
class Skill(BaseModel):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=0)
    color = models.CharField(max_length=20,choices=COLOR_CHOICES, default='info')
    
    def __str__(self):
        return self.name

class ProjectTag(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Project(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_img', null=True, blank=True)
    project_link = models.URLField(null=True,blank=True)
    github_link = models.URLField(null=True,blank=True)
    github_is_private = models.BooleanField(default=False)
    tags = models.ManyToManyField(ProjectTag, blank=True, related_name='projects')
    
    def __str__(self):
        return self.title
    
class Experience(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=50,choices=EXPERIENCE_ICON, default='briefcase')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Message(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'message'
        ordering = ['-created_at']
        verbose_name_plural = 'Messages'