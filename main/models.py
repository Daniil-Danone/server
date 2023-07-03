from django.db import models
from main.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(blank=True, default=False)
    is_staff = models.BooleanField(blank=True, default=False)
    is_active = models.BooleanField(blank=True, default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("name", "surname")

    def __str__(self):
        return f'UserID {self.id}: {self.name} {self.surname} | {self.email}'


class Marks(models.Model):
    title = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    xpos = models.FloatField()
    ypos = models.FloatField()

    def __str__(self):
        return f'{self.id} ~ {self.title} | {self.description} | X: {self.xpos} - Y: {self.ypos}'


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    xpos = models.FloatField(blank=True, null=True)
    ypos = models.FloatField(blank=True, null=True)
    is_Active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} ~ {self.type} | {self.title} | {self.description} | {self.author.name}'
