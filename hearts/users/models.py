from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User,unique=True)

    def __repr__(self):
        return self.user.first_name + " " + self.user.last_name
