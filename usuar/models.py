from django.db import models
from usuario import settings


# Create your models here.

class Postulante(models.Model):
    nombres = models.CharField(max_length=100, unique=True)
    apellidos = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    telefonos = models.CharField(max_length=10, blank=False,null=False)
    archivo = models.FileField(upload_to='usuar/media', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombres)

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulante"
        ordering = ('nombres',)

    def get_archivo(self):
        if self.archivo:
            return '{}{}'.format(settings.MEDIA_URL, self.archivo)
        return '{}{}'.format(settings.STATIC_URL, 'usuar/media')


class Empresa(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Empresa',unique=True)
    contacto=models.CharField(max_length=10, blank=False,null=False)
    correo =  models.EmailField(max_length=100, blank=True, null=True, )
    logo = models.FileField(upload_to='logo/empresa', blank=True, null=True)
    promo= models.FileField(upload_to='logo/empresa', blank=True, null=True)
    promo1= models.FileField(upload_to='logo/empresa', blank=True, null=True)
    promo2= models.FileField(upload_to='logo/empresa', blank=True, null=True)



    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Empresa'
        ordering = ('nombre',)


    def get_image(self):
        if self.logo:
            return '{}{}'.format(settings.MEDIA_URL, self.logo)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

    
    def get_promo(self):
        if self.promo:
            return '{}{}'.format(settings.MEDIA_URL, self.promo)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

    
    def get_promo1(self):
        if self.promo1:
            return '{}{}'.format(settings.MEDIA_URL, self.promo1)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

    
    def get_promo2(self):
        if self.promo2:
            return '{}{}'.format(settings.MEDIA_URL, self.promo2)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')
    

