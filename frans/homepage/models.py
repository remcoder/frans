from django.db import models

class HomepagePhoto(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to="homepage")

  def __unicode__(self):
    return self.title