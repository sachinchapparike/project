from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from bson.json_util import ObjectId
from django.core.mail import send_mail, BadHeaderError

session=False

def index(request):
    return render(request, 'educart/main.html')
def upld(request):
    if session == True:
        return render(request,'educart/upload.html')
    else:
        return render(request,'educart/login.html')
def electronics(request):
    return render(request,'educart/electronics.html')
def appliance(request):
    return render(request,'educart/appliance.html')
def shoes(request):
    return render(request,'educart/shoes.html')
def appreals(request):
    return render(request,'educart/appreals.html')
def furniture(request):
    return render(request,'educart/furniture.html')
'''def books(request):
    return render(request,'educart/books.html')'''
	
#Inserting the data

def insert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        pname=request.POST.get('pn')
        pp=request.POST.get('pp')
        pd=request.POST.get('pd')
        cat=request.POST.get('category')
        #cat=request.POST.get('category')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save("./static/educart/uploads/" + myfile.name, myfile)
        filename.replace(' ','_')
        db = settings.CLIENT.educart
        db.books.insert_one({"name":name,"email":email,"productname":pname,"productprice":pp,"productdesc":pd,"cat":cat,"iurl":myfile.name})

    return render(request, 'educart/main.html')

#books category

def books(request):
    db = settings.CLIENT.educart
    data=db.books.find()
    dataDict = []
    for obj in data:
        obj["id"] = str(obj["_id"])
        dataDict.append(obj)
    dd = {"dataDict":dataDict}
    return render(request,"educart/books.html",dd)

#product datails

def product_details(request):
    cat=request.GET.get('cat')
    Id=request.GET.get('id')
    
    db = settings.CLIENT.educart
    if cat=='books':
        collection=db.books
    data=collection.find_one({"_id":ObjectId(Id)})
    return render(request,"educart/product_details.html",data)

#sending mail
def sendmail(request):
    subject = request.POST.get('name', '')
    message = request.POST.get('desc', '')
    from_email = request.POST.get('email', '')
    to_mail=request.POST.get('to_mail','')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_mail])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/educart/upld/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def login(request):
    global session
    if request.method=='POST':
        email = request.POST.get('email1')
        password=request.POST.get('password1')
        db = settings.CLIENT.educart
        data=db.login.find_one({"email":email,"password":password})
        try:
            if len(data)>0:
                session=True
                return render(request,'educart/upload.html')
        except:
                return render(request,'educart/login.html')


    

def logout(request):
    global session
    session=False
    return render(request,'educart/logout.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        db = settings.CLIENT.educart
        db.login.insert_one({"name":name,"email":email,"password":password})

    return render(request,'educart/login.html')








	