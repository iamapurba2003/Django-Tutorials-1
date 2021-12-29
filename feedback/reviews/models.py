from django.db import models

# Create your models here.

class ReviewModel(models.Model):
    user_name = models.CharField(max_length=100)
    review_Text = models.CharField()
    rating = models.IntegerField()
