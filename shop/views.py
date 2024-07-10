
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from rest_framework.decorators import api_view
from django.db.models.functions import Random
from rest_framework.response import Response
from django.http import JsonResponse
from items.models import Items

import yagmail
import logging
import threading

yag = yagmail.SMTP("example@gmail.com", "Code code code code")
problem_saver = logging.getLogger(__name__)

@api_view(['POST'])
def add_to_cart(request):
    data = request.data
    item_slug = data.get('item')
    # Process the data here (e.g., add the item to the user's cart)
    print(item_slug)
    return Response({"message": "Item added to cart", "item": item_slug})

def send_EMail(name="", email="", msg=""""""):
    try :
        yag.send(to="gamer.good1400@gmail.com", subject=f"from '{email}'", contents=f"{name} sayed : \n\n{msg}")
    except :
        print(msg)
def get_data(request):
    random_items = Items.objects.annotate(random_order=Random()).order_by('random_order')[:4]
    random_items_list = list(random_items.values())
    return JsonResponse(random_items_list, safe=False)

def itempage(request, slug_):
    theItem = get_object_or_404(Items, slug=slug_)
    theItem.IncreasingViews()
    return render(request, "item.html",{'item':theItem})

def mainpage(request):
    if request.method == "GET" :
        contactnow = request.COOKIES.get('contactnow')
        if contactnow is None:
            contactnow = True
        return render(request, 'index.html', {'items':Items.MainPageItems(),
                                            'new_collection1': Items.newCollection()[0:1][0],
                                            'new_collection2': Items.newCollection()[1:2][0],
                                            'contactnow': contactnow,
                                                })
    else :
        if request.POST['message'] != '':
            t1 = threading.Thread(target=send_EMail, args=(request.POST['name'] ,request.POST['email'], request.POST['message']))
            t1.start()

        response = redirect("/")
        response.set_cookie('contactnow', 'false')
        return response
        
        
        

def shoespage(request):
    items = Items.objects.all()[0:20]
    return render(request, 'shoes.html', {'items': items, 'more':True})

def collectionpage(request):
    return render(request,'collection.html', {    
        'new_collection1': Items.newCollection()[0:1][0],
        'new_collection2': Items.newCollection()[1:2][0],
        
        })

def categories(request):
    category = request.GET.get('category', None)
    if category is '':
        return redirect('/')
    items = Items.objects.filter(category=category)
    return render(request, 'shoes.html', {'items': items, 'more':False})

def contact(request):
    if request.method == "GET" :
        contactnow = request.COOKIES.get('contactnow')
        if contactnow is None:
            contactnow = True
        return render(request, 'contact.html', {'contactnow':contactnow})
    
    else :
        if request.POST['message'] != '':
            t1 = threading.Thread(target=send_EMail, args=(request.POST['name'] ,request.POST['email'], request.POST['message']))
            t1.start()
        response = redirect("/")
        response.set_cookie('contactnow', 'false')
        return response
        
        