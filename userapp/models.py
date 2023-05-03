from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserModel(models.Model):
    username = models.CharField('Name', max_length=50, unique=True, null=False,
                                help_text=(
                                    "Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."
                                ),
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                })
    email = models.EmailField('Email', max_length=100, unique=True, null=False)
    password = models.CharField('Password', max_length=128, unique=True, null=False)
    image = models.ImageField('Image', upload_to='usersImages/')
