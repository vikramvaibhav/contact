from django.db import models

# Create your models here.
class Username(models.Model):
    user_name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.user_name

class Contact(models.Model):
    friend_name   = models.CharField(max_length=70)
    contactnumber = models.CharField(max_length=10)
    username      = models.ForeignKey(Username, on_delete='CASCADE', related_name='usernames')

    def __str__(self):
        return self.friend_name
