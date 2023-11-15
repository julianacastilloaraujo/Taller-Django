from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#PERFIL DE USUARIO PARA EL PROYECTO DE SISTEMA DE GESTION ESCOLAR ENFOCADO A ESTUDIANTES 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Image de perfil')
    address = models.CharField(max_lenght=150, null=True, blank=True, verbose_name='Direccion')
    location = models.CharField(max_lenght=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_lenght=150, null=True, blank=True, verbose_name='Telefono')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = [-id]

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)