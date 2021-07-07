from django.db import models

# Create your models here.

TYPE_CHOICES = {
    ('appetizer', 'appetizer'),
    ('entrees','entrees'),
    ('treats', 'treats'),
    ('drinks','drinks'),
}


class Product(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES) # creates the drop down menu.
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)

    objects = models.Manager() # manager() is the interface through which dB query operations are provided
    # to django models.

    def __str__(self): # converts python objects into strings
        return self.name # return the name as a string ie "icecream" instead of obj 2.

