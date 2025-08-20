from django.db import models


# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(verbose_name='title', max_length=300)
    email = models.EmailField(verbose_name='email', max_length=300)
    full_name = models.CharField(verbose_name='full name', max_length=300)
    massage: str = models.TextField(verbose_name='massage', null=True)
    created_date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    response = models.TextField(verbose_name='response', null=True, blank=True)
    is_ready_by_admin = models.BooleanField(verbose_name='read by admin', default=False)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'list Contact Us'

    def __str__(self):
        return self.title
