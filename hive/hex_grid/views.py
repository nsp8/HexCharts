from django.shortcuts import render
from . import utils
# Create your views here.


def home(request):
    context = {
        'countries': utils.get_hex_data()
    }
    return render(request, 'hex_grid/home.html', context)
