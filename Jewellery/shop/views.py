from django.shortcuts import render,redirect
from .form import CustForm,ImgForm,ProdForm
from .models import cust_tab,img_up,prod
from django.contrib.auth.models import auth

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact-us.html')

def Staff_Reg(request):
    return render(request,'Staff_Reg.html')

def Sreg(request):
    form=ImgForm()
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('stafflogin')
    return render(request,'Staff_Reg.html',{'form':form})

def stafflog(request):
    return render(request,'Staff_Log.html')

def Slog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')   
        cr = img_up.objects.filter(name=name, address=address)
        
        if cr:
            cr_approve = img_up.objects.filter(name=name,approval=1).exists()
            if cr_approve:
                cr_profile = img_up.objects.all()
                prods = prod.objects.all()
                return redirect("StaffDash")
            else:
                message = "Staff Not Approved"
                return render(request, 'Staff_Log.html', {'message': message})
        else:
            message = "Invalid Credentials"
            return render(request, 'Staff_Log.html', {'message': message})
    
    return render(request, 'Staff_Log.html')

def StaffDash(request):
    product = prod.objects.all()
    return render(request,"Staff.html",{'product':product})

def AddProd(request):
    form=ProdForm()
    if request.method=='POST':
        form=ProdForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'Products.html',{'form':form})

def UpProd(request,pk):
 cr=prod.objects.get(id=pk)
 form=ProdForm(instance=cr)
 if request.method == "POST":
     form=ProdForm(request.POST,instance=cr)
     if form.is_valid:
         form.save()
     return redirect("StaffDash")
 return render(request,"update.html",{'form':form})



    
def home(request):
    form =CustForm()
    if request.method =="POST":
        form =CustForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'registerform.html',{'form':form})

# def registration(request):
#     return render(request,'registration.html')

def view(request):
    cr = cust_tab.objects.all()
    return render(request,"view.html",{'cr':cr})

def registration(request):
    form=CustForm()
    if request.method=='POST':
        form=CustForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('customer')
    return render(request,'registration.html',{'form':form})

def custlog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        cr= cust_tab.objects.filter(name=name, address=address)
        if cr:
            user_details=cust_tab.objects.get(name=name, address=address)
            email=user_details.email
            age=user_details.age
            
            request.session['email']=email
            request.session['address']=age
            return redirect('shop')
        else:
            message = "Invalid Credentials"
            return render(request,'Customer.html',{'message': message})
    return render(request,'Customer.html')
    
def customer(request):
     return render(request,"Customer.html")
 
def shop(request):
    return render(request,"shop.html")

def cart(request):
    return render (request,"cart.html")


def add(request,pk):
    cr=prod.objects.get(id=pk)
    form=ProdForm(instance=cr)
    if request.method == "POST":
        form=ProdForm(request.POST,instance=cr)
        if form.is_valid:
         form.save()
        return redirect("cart")
    return render(request,"AddtoCart.html",{'form':form})


def ring(request):
    cr= cust_tab.objects.filter(name='Ring')
    
def earring(request):
    cr= cust_tab.objects.filter(name='Earring')


def welcome(request):
     return render(request,"Welcome.html")

