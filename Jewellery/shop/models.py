from django.db import models

class cust_tab(models.Model):
    name = models.CharField(max_length=200)
    age =models.IntegerField()
    email =models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name
    
class img_up(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length = 200)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    approval = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class prod(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    weight = models.IntegerField(null=True)
    certification = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class cart(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
