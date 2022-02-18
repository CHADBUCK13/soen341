from django.shortcuts import render
from .api import itembrowsing

def home(request):
    
    # Get Categories
    categoriesOptions = ['Phones','Food','Games']
    request.session['categoriesOptions'] = itembrowsing.get_categories()


    categorySearch=""

    if request.method=="POST":
        categorySearch = request.POST.get("category")   


    request.session['search'] = categorySearch

    if 'is_logged_in' in request.session:
        is_logged_in = request.session['is_logged_in']
    else:
        is_logged_in = False
    request.session['is_logged_in'] = is_logged_in


    if categorySearch is not "":
        request.session['items'] = itembrowsing.get_items_by_category(categorySearch,100)
    else:
        request.session['items'] = itembrowsing.get_all_items(100)

    request.session.modified = True

    return render(request,'home.html')
