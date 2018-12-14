from django.shortcuts import render
from shop.models import Product, Category

def search(request):
    if request.GET['query']:
        categories = Category.objects.all()
        pattern = request.GET.get('query')
        products = Product.objects.filter(name__contains=pattern)
        return render(request, 'search/search.html',
                        {'products': products, 'query': pattern, 'categories': categories})
