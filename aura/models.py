from django.db import models
from accounts.models import Client,Psychiatrist

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

class Meeting(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    pychiatrist = models.ForeignKey(Psychiatrist, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    meetingID = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return f"{self.client} meets {self.pychiatrist}"