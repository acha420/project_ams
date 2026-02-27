from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    

class Shows(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=200, unique=True)
        description = models.TextField()
        image = models.ImageField(upload_to='shows/')
        watch_link = models.URLField(blank=True)

        def __str__(self):
            return self.title