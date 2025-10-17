from django.db import models

class CategoryHome(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class StatusChoices(models.TextChoices):
    SALE = "sale", "Sale"
    RENT = "rent", "Rent"


class Home(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    description = models.TextField()
    main_image = models.FileField(upload_to="home/")
    size = models.DecimalField(max_digits=8,decimal_places=2)
    floor = models.PositiveSmallIntegerField(default=1,blank=True,null=True)
    new = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=StatusChoices,default=StatusChoices.SALE)
    recomended = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryHome,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
      verbose_name = "Home"
      verbose_name_plural = "Home"
    
    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    image = models.FileField(upload_to="home/")
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.home.name} - {self.image.url}"
    
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    text = models.TextField()
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to="client/")

    def __str__(self):
        return self.name
  
  
class BlogCategory(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)   
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(upload_to="blog/")
    description = models.TextField()
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.phone