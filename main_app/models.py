from django.db import models
from django.urls import reverse
# Create your models here.

PLAYED = (
   ('Y', 'Played with!'),
   ('N', ' Not played with!')
)

class Toy(models.Model):
    name = models.CharField(max_length = 50)
    color = models.CharField(max_length = 20)
    
    def __str__(self):
        return f"{self.color} {self.name}"
    

class Dog(models.Model):
    name= models.CharField(max_length = 100)
    breed= models.CharField(max_length = 100)
    description = models.TextField(max_length=250)
    age=models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id':self.id})



class Played(models.Model):
    date = models.DateField()
    play = models.CharField(max_length = 1, choices = PLAYED, default =PLAYED[0][0])
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_play_display()} on {self.date}"
    class Meta:
        ordering = ['-date']
    



