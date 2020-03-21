from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from  .models import Book
def index(request):
    return  HttpResponse("hello world")

def detail(request):
    book_list= Book.objects.order_by('-pub_date')[:5]
    context = {'book_list':book_list}
    print(book_list)
    return render(request,'lib/detail.html',context)