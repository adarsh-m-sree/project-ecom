from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def index(request):
    return HttpResponse("DONE")

def AllProducts(request,cat_slug=None):
    cat_page=None
    product_list=None
    if cat_slug!= None:
        cat_page=get_object_or_404(Category,slug=cat_slug)
        product_list=Product.objects.all().filter(category=cat_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True)
    paginator=Paginator(product_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':cat_page,'products':products})


def product_details(request,cat_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=cat_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html',{'product':product})
