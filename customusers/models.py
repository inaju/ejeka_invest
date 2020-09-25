from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_student =  models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    username=models.CharField()

class Student(models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (
            color, name)
        return mark_safe(html)
