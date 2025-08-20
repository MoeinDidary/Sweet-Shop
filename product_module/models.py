from django.conf import settings
from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True, verbose_name='Product Category Image')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='URL Title')
    is_active = models.BooleanField(verbose_name='Active / Inactive')
    is_delete = models.BooleanField(verbose_name='Deleted / Not Deleted')

    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='Product Name')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='Categories')
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True, verbose_name='Product Image')
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='Short Description')
    description = models.TextField(verbose_name='Main Description', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='Slug')
    is_active = models.BooleanField(default=False, verbose_name='Active / Inactive')
    is_delete = models.BooleanField(verbose_name='Deleted / Not Deleted')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


from django.contrib.auth.models import User
from django.db import models


class ProductComment(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="comments", verbose_name="Product")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product_comments")
    text = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    is_active = models.BooleanField(default=True, verbose_name="Active / Inactive")

    def __str__(self):
        return f"Comment by {self.user} on {self.product}"

    class Meta:
        verbose_name = "Product Comment"
        verbose_name_plural = "Product Comments"
