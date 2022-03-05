from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
  name = models.CharField(max_length=64)
  # Foreign key is used to access a model inside of another table
  # models.CASCADE - This will delete all reviews made by the user if the user is deleted
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(default='')

# Dunder str allows us to view the name of the object
  def __str__(self):
     return self.name

  def get_absolute_url(self):
    return reverse('snack-detail', args=[str(self.id)])
