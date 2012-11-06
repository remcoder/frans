from django.db import models
from django.template.defaultfilters import slugify
from django.db import IntegrityError

class Column(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField(null=True)
  slug = models.SlugField(max_length=255, unique=True)

  # override save method to generate slug from title
  # def save(self, *args, **kwargs):
  #     self.slug = slugify(self.title)
  #     super(Column, self).save(*args, **kwargs)

  def __unicode__(self):
    return self.title
