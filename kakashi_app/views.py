from django.shortcuts import render,HttpResponse,redirect
from .models import Msg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def create(request):
    if request.method=='POST':
        n = request.POST['uname']
        mail = request.POST['uemail']
        mob = request.POST['umobile']
        msg = request.POST['msg']
        # print(n)
        m = Msg.objects.create(name=n, email=mail, mobile=mob, msg=msg)
        m.save()
        #return HttpResponse("Data is Inserted")
        return redirect('/dashboard')
    else:
        print("Request is:",request.method)
        return render(request,'create.html')

def dashboard(request):
    m = Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    #return HttpResponse("Data fetch succesfully")
    return render(request,'dashboard.html',context)

def edit(request,rid):
    if request.method=='POST':
        n = request.POST['uname']
        mail = request.POST['uemail']
        mob = request.POST['umobile']
        msg = request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=n, email=mail, mobile=mob, msg=msg)
        return redirect('/dashboard')
    else:
        # display from with old data
        m=Msg.objects.get(id = rid)
        context={}
        context['data']=m
        return render (request,'edit.html',context)
        
    # print("Id of record to be Edited:",rid)
    # return HttpResponse("Id:"+rid)

def delete(request,rid):
    #print("Id of record to be Deleted:",rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    #return HttpResponse("Id:"+rid)
    return redirect('/dashboard')

def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uname=="" or upass=="" or ucpass=="":
            context={}
            context['errmsg']="Field Cannot be empty"
            return render(request, 'register.html', context)
        
        elif upass!=ucpass:
            context={}
            context['errmsg']="Password did not match"
            return render(request, 'register.html', context)
        else:
            try:
                u = User.objects.create(username=uname,password=upass,email=uname)
                u.set_password(upass)
                u.save()
                context={}
                context['success']="User Created Successfully"
                return render(request,'register.html',context)
            
            except Exception:
                context={}
                context['errmsg']="Username already Exists"
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')
        

def user_login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=="" or upass=="":
            context={}
            context['errmsg']="Field Cannot be empty"
            return render(request, 'login.html', context)
        else:
            u=authenticate(username=uname, password=upass)
            if u is not None:           #USER NAME & PASS IS NOT NULL
                login(request,u)
                return redirect('/create')
            else:
                context={}
                context['errmsg']='Invalid Username or Password'
                return render(request,"login.html",context)
        
    else:
        return render(request,'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('/login')
