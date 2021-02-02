import  json
from django.http import HttpResponse
from django.shortcuts import render


from autoComplete_filter.models import  Product
# Create your views here.


def autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        return JsonResponse(titles, safe=False)
    return render(request, 'home.html')