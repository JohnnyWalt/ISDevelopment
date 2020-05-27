from django.db import models
from djchoices import DjangoChoices, ChoiceItem
import os

# Create your models here.
class MIS_Document(models.Model):
    courses = (
        ('ISD', 'Information System Development'),
        ('EAM', 'Enterprise Architecture Management'),
        ('MIS', 'Management Information Systems'),
        ('BPM', 'Business Process Management'),
        ('DAS', 'Data and Application Security'),
        ('DM', 'Data Management'),
        ('BS', 'Business Statistics'),
        ('IL', 'Innovation Lab'),
        ('ISM', 'Information Systems Modelling'),
        ('DI', 'Digital Innovation'),
        ('DS', 'Data Science'),
        ('DB', 'Digital Business'),
        ('EIT', 'Emerging IT Topics'),
        ('HCD', 'Human Centered Design'),
        ('RM', 'Research Methods'),
        ('RS', 'Research Seminar'),
        ('PS', 'Project Seminar'),
        ('MT', 'Master Thesis'),
        
    )
    
    def location(instance, filename):
        return os.path.join(instance.course, filename)
        
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=3, choices=courses, default='ISD')
    pdf = models.FileField(upload_to=location)


    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

