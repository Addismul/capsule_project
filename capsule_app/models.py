from django.db import models

# Create your models here.
class Capsule(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    details=models.CharField(max_length=200,blank=True,null=True)
    static_fire_date_utc= models.CharField(max_length=20,blank=True,null=True)
    static_fire_date_unix=models.CharField(max_length=20,blank=True,null=True)
    date_precision=models.CharField(max_length=20,blank=True,null=True)
    launch_library_id=models.CharField(max_length=20,blank=True,null=True)
    slug=models.SlugField(default = 'test')
    tbd=models.CharField(max_length=20,blank=True,null=True)
    auto_update=models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        return self.name
    