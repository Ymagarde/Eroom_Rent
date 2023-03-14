from django.forms import EmailField
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import  Property
from.models import  Customerreg
from.models import  Brokerreg
from.models import  Ownerreg
from.models import  Customer
def showproperty(request):
    return render(request,"eroomapp/sproperty.html",{"res":Property.objects.all()})

def booking(request):
    return render(request,"eroomapp/bookproperty.html",{"res":Property.objects.all()})

def customer(request):
    data1=Property.objects.all()
    if request.method=="POST":
        r2 = Customer(name=request.POST["name"],emailid=request.POST["email"],
            bookid=request.POST["ddl"],mobile=request.POST["mobile"],date=request.POST["date"],Category=request.POST["txtt"])
        r2.save()
        return render(request,"eroomapp/customer.html",{"res1":data1,"msg":"Apply sucsessfully","res2":Customer.objects.all()})
    return render(request,"eroomapp/customer.html",{"res1":data1,"bookid":(request.GET["q"])})


def insertProperty(request):
    if request.method=="POST":
         r1 = Property(Category=request.POST["txtt"],Rent=request.POST["txtd"],
            Location=request.POST["txte"],description=request.POST["txtte"])
         r1.save()
         return render(request,"eroomapp/sproperty.html",{"res":Property.objects.all()})
    return render(request,"eroomapp/addproperty.html")


def editprorety(request):
    if request.method=="POST":
      s =Property.objects.get(pk=request.POST["txtid"])
      s.Category=request.POST["txtt"]
      s.Rent=request.POST["txtd"]
      s.Location=request.POST["txte"]
      s.description=request.POST["txtte"]
      s.save()
      return redirect('showproperty')
    rec=Property.objects.get(pk=request.GET["q"])
    return render(request,"eroomapp/editproperty.html",{"res":rec})

def deleteproperty(request):
    if request.method=="POST":
        res=Property.objects.get(pk=request.POST["txtid"])
        res.delete()
        return redirect('showproperty')
    rec=Property.objects.get(pk=request.GET["q"])
    return render(request,"eroomapp/deleteproperty.html",{"res":rec})


def customerreg(request):
    if request.method=="POST":
        s = Customerreg(emailid=request.POST["email"],password=request.POST["password"],mobile=request.POST["mobile"],address=request.POST["Address"])
        s.save()
        return render(request,"eroomapp/clogin.html")
    return render(request,"eroomapp/customerreg.html")

def brokerlogin(request):
    if request.method=="POST":
        r = Brokerreg.objects.filter(emailid=request.POST["emailid"],password=request.POST["password"])
        if r.count()>0:
            request.session["sessemail"]=request.POST["emailid"]
            if request.POST.get("chk"):
                res = HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["emailid"])
                res.set_cookie('upass',request.POST["password"])
                res['Location']='insertProperty'
                return res
        else:
                return render(request,"eroomapp/brokerlogin.html",{"msg":"invalid userid and password"})
    else:
        c1=''
        c2=''
    if request.COOKIES.get('ukey'):
        c1=request.COOKIES['ukey']
        c2=request.COOKIES['upass']
    return render(request,"eroomapp/brokerlogin.html",{'ucookie':c1,'pcookie':c2})
    

def brokerreg(request):
    if request.method=="POST":
        s = Brokerreg(emailid=request.POST["emailid"],password=request.POST["password"],mobile=request.POST["mobile"],address=request.POST["Address"])
        s.save()
        return render(request,"eroomapp/brokerlogin.html")
    return render(request,"eroomapp/brokerreg.html")

def owenerlogin(request):
    if request.method=="POST":
        r = Ownerreg.objects.filter(emailid=request.POST["mail"],password=request.POST["password"])
        if r.count()>0:
            request.session["sessemail"]=request.POST["mail"]
            if request.POST.get("chk"):
                res = HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["mail"])
                res.set_cookie('upass',request.POST["password"])
                res['Location']='insertProperty'
                return res
        else:
                return render(request,"eroomapp/owenerlogin.html",{"msg":"invalid userid and password"})
    else:
        c1=''
        c2=''
    if request.COOKIES.get('ukey'):
        c1=request.COOKIES['ukey']
        c2=request.COOKIES['upass']
    return render(request,"eroomapp/owenerlogin.html",{'ucookie':c1,'pcookie':c2})

def owenerreg(request):
    if request.method=="POST":
        s = Ownerreg(emailid=request.POST["mail"],password=request.POST["password"],mobile=request.POST["mobile"],address=request.POST["Address"])
        s.save()
        return render(request,"eroomapp/owenerlogin.html")
    return render(request,"eroomapp/owenerreg.html")
    

def dash(request): 
    return render(request,"eroomapp/home.html")

def sbp(request): 
    return render(request,"eroomapp/sbookproperty.html",{"res2":Customer.objects.all()})


def login(request):
    if request.method=="POST":
        r = Customerreg.objects.filter(emailid=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session["sessemail"]=request.POST["email"]
            if request.POST.get("chk"):
                res = HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location']='booking'
                return res
        else:
                return render(request,"eroomapp/clogin.html",{"msg":"invalid userid and password"})
    else:
        c1=''
        c2=''
    if request.COOKIES.get('ukey'):
        c1=request.COOKIES['ukey']
        c2=request.COOKIES['upass']
    return render(request,"eroomapp/clogin.html",{'ucookie':c1,'pcookie':c2})
    

def Logout(request):
    res=HttpResponse(status=302)
    res.delete_cookie('ukey',"/")
    res.delete_cookie('upass',"/")
    del request.session["sessemail"]
    res['Location']='dash'
    return res
