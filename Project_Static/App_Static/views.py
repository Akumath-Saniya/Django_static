from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html')
def Contact(request):
    return render(request,'Contact.html')
def Cart(request):
    return render(request,'Cart.html')
def Books(request):
    return render(request,'Books.html')