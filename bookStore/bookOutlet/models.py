from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls.base import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(null = True, max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    isBestSelling = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    

    # def __str__(self):
    #     return f"{self.title} ({self.rating}) -- {self.isBestSelling} -- {self.author}"