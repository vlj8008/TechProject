from django.forms import ModelForm
from .models import Product # from .models.py import my Product class

#class is upper case.


class ProductForm(ModelForm): # inherit the Model Form class in to my ProductForm
    class Meta:  # This is just a class container with some options (metadata) attached to the model.
        # It defines such things as available permissions, associated database table name,
        model = Product # because that is what we have in our model.py
        fields = '__all__' # this dunder method gets all fields from Product. It is a shortcut.
