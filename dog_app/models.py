from django.db import models

# Create your models here.
SIZE_CHOICES =(
    ('Tiny' , 'Tiny'),
    ('Small' ,'Small'),
    ('Medium' , 'Medium'),
    ('Large' , 'Large')
)
INTENSITY_CHOICES =(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)


class Bread(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50 , choices=SIZE_CHOICES)
    friendliness =models.IntegerField(choices= INTENSITY_CHOICES)
    trainability = models.IntegerField(choices=INTENSITY_CHOICES)
    sheddingamount = models.IntegerField(choices=INTENSITY_CHOICES)
    exerciseneeds = models.IntegerField(choices=INTENSITY_CHOICES)
    def __str__(self):
        return self.name
    
class Dog(models.Model):
    name =models.CharField(max_length=50)
    age = models.IntegerField() 
    bread = models.ForeignKey('Bread' , on_delete=models.CASCADE)
    gender = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 
    favoritefood = models.CharField(max_length=50) 
    favoritetoy = models.CharField(max_length=50)
    def __str__(self):
        return self.name
