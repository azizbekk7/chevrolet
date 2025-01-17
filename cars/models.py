from django.db import models

from django.utils import timezone 

class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    model_year = models.IntegerField(verbose_name = 'Yili')
    mileage = models.IntegerField(verbose_name = 'Kilometiri')
    horsepower = models.IntegerField(verbose_name = 'Ot kuchi')
    
    AT = 'Avtomatk'
    MX = 'Mexanik'
    
    transmission_type = (
        ('AT', 'Avtomatik'),
        ('MX', 'Mexanik'),
    )
    
    transmission = models.CharField(max_length=20, choices=transmission_type, default="Mexanik", verbose_name='Transmissiyasi')
    
    UZ = "so'm"
    ENG = '$'

    the_price = (
        (UZ, "so'm"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="so'm")
    price = models.IntegerField(verbose_name='Narxi')
    publish_time = models.DateTimeField(default=timezone.now, verbose_name='Mashina yaratilgan vaqti')
    body = models.TextField(verbose_name="Ma'lumoti")
    image = models.ImageField(upload_to='cars/images', verbose_name='Rasmi')

    def __str__(self):
        return f"{self.name} ({self.model_year})"
    
    
    class Meta:
        db_table = 'Mashina'
        managed = True
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'

class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categories' 
        managed = True
        verbose_name = 'Kategoriyalar'
        verbose_name_plural = 'Kategoriyalar'