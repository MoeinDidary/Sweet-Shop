from django.db import models


# Create your models here.

class AboutUS(models.Model):
    title = models.CharField(verbose_name='title company', max_length=300)
    description = models.TextField(verbose_name='description', db_index=True)
    email = models.EmailField(verbose_name='email company', db_index=True)
    phone = models.CharField(verbose_name='phone company', max_length=50)
    fax = models.CharField(verbose_name='fax company', max_length=50)
    address = models.CharField(verbose_name='address', max_length=360)
    poster = models.ImageField(verbose_name='poster', upload_to='images/poster', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About US'
