from django.shortcuts import render
from . import utils
# Create your views here.


def home(request):
    context = {
        'countries': utils.get_hex_data()
    }
    return render(request, 'hex_grid/home.html', context)


def about(request):
    context = {
        'hexes_in_even': range(5),
        'hexes_in_odd': range(4),
        'total_columns': range(1, 16)
    }
    return render(request, 'hex_grid/about.html', context)
