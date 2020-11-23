from django.db import models

# Create your models here.

class User(models.Model):
    # Just heads up, It's usually bad practice to use the email as the primary key
    id = models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.CharField(max_length=10)
    birth_city = models.CharField(max_length=255)
    birth_state = models.CharField(max_length=255)

    def __str__(self):
        return self.user_email

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=10)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.user_email + "(" + self.token + ")"