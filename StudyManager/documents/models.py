from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from django.contrib.auth.models import User

import os

# Create your models here.
class MIS_Document(models.Model):
    # Creating the choices for the courses
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

    # Define upload path, depending on the selected Course from the "course Charfield"
    def location(instance, filename):
        return os.path.join(instance.course, filename)

    # Define objects of the model:
    title = models.CharField(max_length=100)
    # Charfield with choices
    course = models.CharField(max_length=3, choices=courses)
    # Setting upload path
    pdf = models.FileField(upload_to=location)
    # Author as ForeignKey, to get the user id. -> CASCADE to also delete all the object who have referenced it.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Like field, to like a document
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    # Return pdf title
    def __str__(self):
        return self.title

    # function to count the likes
    @property
    def num_likes(self):
        return self.liked.all().count()

    # Delete function, to delete the corresponding document, if delete button is pressed
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

# Set the choices for like/unlike
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
# New class for Likes.
# User as FK from User
# document as FK from the MIS_Document class, to link it to the corresponing document
# Value for the Like/Unlike function
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(MIS_Document, on_delete=models.CASCADE, related_name='document')
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    # Return document string
    def __str__(self):
        return str(self.dcument)

