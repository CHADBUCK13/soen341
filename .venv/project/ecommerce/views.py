"""
This module contains all the logic required the home page
"""

from django.shortcuts import render
from .api.item_browsing import get_categories, get_items_by_category, get_all_items_dict

def home(request):
    """
    Goes to the Home page
    """


    # Get Categories
    request.session['categoriesOptions'] = get_categories()

    category=""
    if request.method=="POST":
        category = request.POST.get("category")

    if category is None:
        category=""

    if 'is_logged_in' in request.session:
        is_logged_in = request.session['is_logged_in']
    else:
        is_logged_in = False

    request.session['is_logged_in'] = is_logged_in


    if category != "":
        items = get_items_by_category(category,100)
        if len(items) == 0:
            category = "No Items in "+category
    else:
        items = get_all_items_dict()

    request.session.modified = True

    return render(request,'home.html',{'items':items,'category':category})
