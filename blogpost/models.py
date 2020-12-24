from django.db import models
CATEGORY = (('busines','ビジネス'),('lief','生活'),('other','その他'))

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    contet = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices= CATEGORY
    )
    def _str_ (self):
        return self.title
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
