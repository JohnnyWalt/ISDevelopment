from django.db import models

# Create your models here.
class ISD_Document(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='ISD/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)