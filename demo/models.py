from django.db import models



class Book(models.Model):

    title = models.CharField(max_length=36, unique=True, blank=False)
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)

    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)