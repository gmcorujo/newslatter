from django.db import models

# Create your models here.


class NewslatterUser(models.Model):
    email = models.EmailField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Newslatter(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    email = models.ManyToManyField(NewslatterUser)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name