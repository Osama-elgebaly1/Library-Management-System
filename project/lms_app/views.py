from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm , CategoryForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()


    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()


    categories = Category.objects.all()
    books = Book.objects.all()
    form = BookForm()
    cat_form = CategoryForm()
    allbooks = Book.objects.filter(active =True).count()
    soldbooks = Book.objects.filter(status='sold').count()
    availablebooks = Book.objects.filter(status ='available').count()
    rentalbooks = Book.objects.filter(status ='rental').count()










    return render(request,'pages/index.html',{'books':books,
                                              'categories':categories,
                                              'form':form,
                                              'cat_form':cat_form,
                                              'allbooks':allbooks,
                                              'rentalbooks':rentalbooks,
                                              'soldbooks':soldbooks,
                                              'availablebooks':availablebooks,

                                              
                                              })



def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)




    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    categories = Category.objects.all()
    books = search
    cat_form = CategoryForm()


    return render(request,'pages/books.html',{'books':books, 'categories':categories,'cat_form':cat_form })



def update(request,id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book_save = BookForm(request.POST,request.FILES,instance=book)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
        
    else:
        book_save = BookForm(instance=book)

    return render(request,'pages/update.html',{'form':book_save})


def delete(request,id):
    book =Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    
    return render(request,'pages/delete.html')


