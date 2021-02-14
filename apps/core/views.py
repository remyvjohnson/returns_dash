from django.shortcuts import render
from .models import core_return_reasons_sku

# Two example views. Change or delete as necessary.
def home(request):
    
    return_reasons = core_return_reasons_sku.objects.all()
    print('working')
    context = {
        'return_reasons': return_reasons,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

#data table
# def returns_by_category(): 
