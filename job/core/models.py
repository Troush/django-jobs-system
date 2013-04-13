from django.db import models

# Create your models here.
class Company(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    BIG = 'L'
    CORP = 'XL'
    company_size =  (
        (SMALL,'<20'),
        (MEDIUM,'20-50'),
        (BIG,'50-100'),
        (CORP,'100<'),
        )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    size = models.CharField(max_length=2,choices=company_size,default=SMALL)
    about = models.TextField()
    phone = models.IntegerField(max_length=12)
    site = models.CharField(max_length=128)
    create_date = models.DateTimeField('date created')
