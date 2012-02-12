from django.db import models

# Create your models here.
class ArtObject(models.Model):
  title = models.CharField(max_length=255)
  technique = models.CharField(max_length=255)
  dimensions = models.CharField(max_length=255)

  def __unicode__(self):
    return self.title