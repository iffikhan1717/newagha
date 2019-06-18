from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    descp = models.TextField()
    img = models.ImageField(upload_to='bimages/')


    def __str__(self):
        return str(self.title)


