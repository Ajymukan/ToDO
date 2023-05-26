from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    title = models.CharField(max_length=100, verbose_name='Тема')
    description = models.TextField(verbose_name="Описание" , blank=True)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-create_data']
        

class Elected(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    title = models.CharField(max_length=100, verbose_name='Тема')
    description = models.TextField(verbose_name="Описание" , blank=True)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-create_data']