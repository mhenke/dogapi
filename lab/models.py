from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
"""Dog model
A dog should contain the following fields:

name (a character string)
age (an integer)
breed (a foreign key to the Breed Model)
gender (a character string)
color (a character string)
favoritefood (a character string)
favoritetoy (a character string)

Breed Model
A breed should contain the following fields:

name (a character string)
size (a character string) [should accept Tiny, Small, Medium, Large]
friendliness (an integer field) [should accept values from 1-5]
trainability (an integer field) [should accept values from 1-5]
sheddingamount (an integer field) [should accept values from 1-5]
exerciseneeds (an integer field) [should accept values from 1-5]
"""

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    
    
class Breed(models.Model):
    name = models.CharField(max_length=100)
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    size = models.CharField(choices=SIZE_CHOICES, max_length=6)
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name