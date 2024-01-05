from django.db import models

class Services(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    icon = models.FileField( upload_to='Icons')
    img = models.ImageField( upload_to='Services',)

    def __str__(self):
        return self.title

class Itworks(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='works', default='image.png')

    def __str__(self):
        return self.desc[:8]  

# Create your models here.
