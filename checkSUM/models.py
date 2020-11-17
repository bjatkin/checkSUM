from django.db import models

# Create your models here.

class User(models.Model):
    user_email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.CharField(max_length=10)
    birth_city = models.CharField(max_length=255)
    birth_state = models.CharField(max_length=255)

    def __str__(self):
        return self.user_email