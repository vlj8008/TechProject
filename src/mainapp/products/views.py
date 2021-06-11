from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import views
from .models import Product # from models.py import Product (that we made)
from .forms import ProductForm # from forms.py import ProductForm


def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})


def details(request, pk): # pass in user request and PK which got when user clicked on product from drop down
    # menu
    pk = int(pk) # change primary key from string in to integer.
    item = get_object_or_404(Product, pk=pk) # gets the product with certain pk, or gives 404 message to user
    form = ProductForm(data=request.POST or None, instance=item) # puts the specific item into the form.
    if request.method == 'POST':
        if form.is_valid(): # this method runs validation on all fields.
            form2 = form.save(commit=False) # create form2 but don't save the new form instance.
            form2.save()
            return redirect('admin-console')
        else:
            print(form.errors) # print error message to screen.
    else:
        return render(request, 'products/present_product.html', {'form': form}) # render the products page with
    # the dictionary items
