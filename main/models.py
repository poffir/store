from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "category"
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name

    2




class CPU(models.Model):
    cpu_name = models.CharField(max_length=200)
    cpu_core = models.IntegerField(default=2)
    cpu_video_core = models.IntegerField(default=0)
    cpu_frequency = models.DecimalField(default=1, decimal_places=2 ,max_digits=10)
    streams = models.IntegerField(default=1)

    def __str__(self):
        return self.cpu_name
    
class GPU(models.Model):
    gpu_name = models.CharField(max_length=200) 
    
    gpu_core = models.IntegerField(default=2)
    gpu_memory = models.IntegerField(default=2)
    gpu_frequency = models.DecimalField(default=0, decimal_places=2 ,max_digits=10)

    def __str__(self):
        return self.gpu_name
    
class RAM(models.Model):
    ram_name = models.CharField(max_length=200)
    ram_size = models.IntegerField(default=2)
    ram_frequency = models.IntegerField(default=2)

    def __str__(self):
        return self.ram_name
        
class SSD(models.Model):
    ssd_name = models.CharField(max_length=200)
    ssd_size = models.IntegerField(default=2)
    ssd_speed = models.IntegerField(default=0)

    def __str__(self):
        return self.ssd_name



class Characteristics(models.Model):
    
    hz = models.DecimalField(decimal_places=2 ,max_digits=10)
    resolution = models.CharField(max_length=40)
    weight = models.DecimalField(default=0.00, decimal_places=2 ,max_digits=10)

    cpu = models.ForeignKey(CPU, on_delete = models.CASCADE) 
    ram = models.ForeignKey(RAM, on_delete = models.CASCADE)
    ssd = models.ForeignKey(SSD, on_delete = models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete = models.CASCADE)
    

class Image:
    product_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField()    

    class Meta:
        ordering = ["name"]
        indexes = [
                    models.Index(fields=["id"]),
                    models.Index(fields=["name"]),
                    models.Index(fields=["created"])
                    ] 


    def get_deferred_url(self):
        return reverse("main:product_detail") 

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    characteristics = models.ForeignKey(Characteristics, on_delete = models.CASCADE)
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=200) #то что будет отображатся в поисковой строке 
    description = models.TextField(max_length=4000)
    price = models.DecimalField(default=0.00, decimal_places=2 ,max_digits=10 )
    variable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_created=True)
    discount = models.DecimalField(default=0.00, decimal_places=2 ,max_digits=10 )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main", args=[self.slug])

#создать класс характеристик списком вниз все (ширина экрана герцовка компелктующие и тд)
#найти или создать в фигме дизайн сайта (фронт) 