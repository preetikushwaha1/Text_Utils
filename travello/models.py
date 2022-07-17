from django.db import models

# Create your models here.
class blog(models.Model): 
    post_By = models.CharField(max_length=200)
    img =  models.ImageField(upload_to="pics")
    discription  = models.TextField()
    like = models.IntegerField()
    offer = models.BooleanField(default=False)
