from django.db import models

# Create your models here.

# Model for the projects that will be displayed on the website
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.CharField(max_length=255, blank=True, default='')
    github_link = models.URLField(blank=True, null=True, default = 'Access to this GitHub repository is currently unavailable.')
    
    # Image Fields for the projects 
    image_1 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    #.. add more image fields if needed 

    def __str__(self):
        return self.title
