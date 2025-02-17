from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="users_image", blank=True, null=True, verbose_name='Аватар') 
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Номер телефона')
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Ползователь'   
        verbose_name_plural = 'Ползователи'   
        
    def __str__(self):
        return self.username 
    