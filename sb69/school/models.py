from django.db import models

# Create your models here.

class ExamCenter(models.Model):
    cname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class ProxyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['cname']