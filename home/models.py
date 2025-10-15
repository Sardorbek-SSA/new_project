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
    main_image = models.FileField(upload_to="media/home/")
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