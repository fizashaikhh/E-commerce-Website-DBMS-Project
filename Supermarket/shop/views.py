
# Create your views here.
from django.shortcuts import render
import json


from .models import Customer,Category,Product,Supplier,Order,OrderDetails
from math import ceil
import datetime
def index(request):
    allProds=[]
    categoryProducts = Product.objects.values('catid')  # list of dict
    categories = ( item['catid'] for item in categoryProducts)
    categories = set(categories)
    for category in categories:
        product = Product.objects.filter(catid=category)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([product,range(1,nSlides),nSlides])
    context = {
        "allProds": allProds
    }
    return render(request, 'shop/index.html',context)


def productView(request, id):
    product = Product.objects.filter(prodid= id)
    return render(request, 'shop/prodView.html', {"product":product[0]})

def checkout(request):
    if(request.method == "POST"):
        itemsJson = request.POST.get('itemsJson','')
        name= request.POST.get('name','')
        contact=request.POST.get('contact','')
        address= request.POST.get('address','')
        itemJson = json.loads(itemsJson)

        customer = Customer(name=name, contact=contact)
        customer.save()

        cust = Customer.objects.filter(name=name)
        for item in cust:
            order = Order(custid= item, date=datetime.datetime.now())
        order.save()

        cust = Customer.objects.filter(name=name)
        for item in cust:
            ord = Order.objects.filter(custid = item)

        for orderid in ord:
            for item in itemJson:
                product = Product.objects.filter(prodid= item )
                for prodid in product:
                    print(itemJson[item][0], itemJson[item][1])
                    orderdetails = OrderDetails(prodid=prodid, qty=itemJson[item][0], orderid=orderid)
                    orderdetails.save()

        thank = True

        return render(request,'shop/checkout.html',{'thank':thank})

    return render(request,'shop/checkout.html')