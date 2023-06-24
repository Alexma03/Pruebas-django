from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    #sirve para el nombre en el panel de administracion
    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name + ' | ' + self.project.name