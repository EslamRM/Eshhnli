import requests
import random
from bs4 import BeautifulSoup
from ebaysdk.finding import Connection as finding

from django.shortcuts import render ,HttpResponse,redirect,Http404
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from .models import Order



def index(request):
    return render(request,'index.html')

def how_work (request):
    return render(request,'how-work.html')

def offers (request):
    return render(request,'offer.html')

def orders(request):
    return render(request,'orders.html')
def order(request):
    return render(request,'order.html')
def support (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(subject=name, message=message, from_email=request.user, recipient_list=[EMAIL_HOST_USER],
                  fail_silently=False)
        return HttpResponse('Email has been send successfully')
    else:
        return render(request,'support.html')


#def faq (request):
    #return render(request,'faq.html')

def cart(request):

    if request.user.is_authenticated:
        orders = Order.objects.all()
        count = orders.count()
        return render(request, 'cart.html',{'orders':orders,'count':count})

    else:
        return redirect('/accounts/login/')

def clear_cart(request):
    Order.objects.all().delete()
    return redirect('/cart')
def clear_item(request,id):
    prd = Order.objects.get(id=id)
    prd.delete()
    return redirect('/cart')
def edit_item(request,id):
    if request.method == 'POST':
        prd = Order.objects.get(id=id)
        context = {
            'prd':prd,
            'logo':prd.logo_url,
            'title':prd.title,
            'price':prd.price,
            'img':prd.img_url,
            'url':prd.url,
            'category':prd.category,
            'color':prd.color,
            'size':prd.size,
            'qty':prd.Qty,
        }

        return HttpResponse(context)
    else:
        return redirect('/cart')

def add_cart(request):
    if request.method == 'POST':
        new = Order(logo_url=request.POST['logo'],
                    title=request.POST['title'],
                    price=request.POST['price'],
                    img_url=request.POST['img'],
                    url=request.POST['url'],
                    category=request.POST['category'],
                    color=request.POST['color'],
                    size=request.POST['size'],
                    Qty=request.POST['qty']
                    )
        new.user = request.user
        new.save()
        return redirect('/cart/')
    else:
        return redirect('/')

    
#- ecommerce sites api

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
proxies_list = ["128.199.109.241:8080","113.53.230.195:3128","125.141.200.53:80","125.141.200.14:80","128.199.200.112:138","149.56.123.99:3128","128.199.200.112:80","125.141.200.39:80","134.213.29.202:4444"]
proxies = {'https': random.choice(proxies_list)}

# for ebay
# URL = 'https://www.ebay.com/p/9034209182?iid=114157441243'
#
# page = requests.get(URL,headers=headers)
# soup = BeautifulSoup(page.content,features='lxml')
# soup.findAll(True,{'class':'product-title','id':'itemTitle'})
# # title = soup.find(id='itemTitle').text
# # price = soup.find(id='prcIsum').text
# # #img = soup.find_all(class_='img')[0].find_all('img')[-1]['src']
# # img = soup.find_all(class_='vi-image-gallery__image vi-image-gallery__image--absolute-center')
# selectors = ['.product-title', '#itemTitle']
# inf = []
# for s in selectors:
#     inf.append(soup.find_all(attrs=s))
#
# print(inf)
# print(img)

# ID_APP = 'EslamRam-shahnli-PRD-6c8eaa52b-95f85fe5'
#
# Keywords =
# api = finding(appid=ID_APP, config_file=None)
# api_request = { 'keywords': Keywords }
# response = api.execute('findItemsByKeywords', api_request)
# soup = BeautifulSoup(response.content,'lxml')
#
# totalentries = int(soup.find('totalentries').text)
# items = soup.find_all('item')
#
# for item in items:
#     cat = item.categoryname.string.lower()
#     title = item.title.string.lower()
#     price = int(round(float(item.currentprice.string)))
#     url = item.viewitemurl.string.lower()
# #########################
def api(request):
    if request.method == 'POST':
        URL = request.POST['url']

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, features='lxml')

        if '6pm.com' in URL:
            try:
                logo = URL.split('/')[2]
                title = soup.find(class_='av').text
                price = soup.find(class_='dr ir').text
                img = soup.find(class_='lt')['src']
                context = {
                    'title':title,
                    'price':price,
                    'img':img,
                    'url':URL,
                    'logo':logo,
                }
                return render(request,'cart.html',context)
            except:
                return render(request,'cart.html')
        elif 'carters.com' in URL:
            try:
                logo = URL.split('/')[2]
                title = soup.find(class_='product-title').text.strip()
                price = soup.find(class_='value').text.strip()
                img = soup.find(class_='js-product-main-image-0')['data-yo-src']
                context = {
                    'title': title,
                    'price': price,
                    'img': img,
                    'url': URL,
                    'logo':logo,
                }
                return render(request, 'cart.html', context)
            except:
                return render(request,'cart.html')
        elif 'gap.com' in URL:
            try:
                logo = URL.split('/')[2]
                title = soup.find(class_="product-title__text").get_text(strip=True)
                price = soup.find(class_="pdp-pricing__selected").text
                img = soup.find(class_="hover-zoom")['href']
                context = {
                    'title': title,
                    'price': price,
                    'img': 'https://www.gap.com'+img,
                    'url': URL,
                    'logo':logo,
                }
                return render(request, 'cart.html', context)
            except:
                return render(request,'cart.html')
        elif 'guess.eu' in URL:
            try:
                logo = URL.split('/')[2]
                title = soup.find(class_="pull-left").text
                price = soup.find(class_="actual").text
                img = soup.find_all(class_="zoom-link")[-1].find('img')
                img = img['src'][:84]+img['data-image']
                context = {
                    'title': title,
                    'price': price,
                    'img': img,
                    'logo':logo,
                    'url': URL,
                }
                return render(request, 'cart.html', context)
            except:
                return render(request,'cart.html')
        elif 'uspoloassn.com' in URL:
            try:
                logo = URL.split('/')[2]
                title = soup.find(class_="emos_H1").text
                price = soup.find(class_="urunDetay_satisFiyat").text
                img = soup.find_all(class_="mask")[-1].find_all('a')
                img = 'https://eg.uspoloassn.com/'+img[0]['href']
                context = {
                    'title': title,
                    'price': price,
                    'img': img,
                    'logo':logo,
                    'url': URL,
                }
                return render(request, 'cart.html', context)
            except:
                return render(request,'cart.html')
        elif 'ralphlauren.com' in URL:
            try:
                logo = URL.split('/')[2]
                title = soup.find(class_="product-name").text.strip()
                price = soup.find(class_="lowblack").text.strip()
                img = soup.find(class_="popup-img")['data-img']
                context = {
                    'title': title,
                    'price': price,
                    'img': img,
                    'url': URL,
                    'logo':logo,
                }
                return render(request, 'cart.html', context)
            except:
                return render(request, 'cart.html')
        else:
            return render(request,'cart.html')

