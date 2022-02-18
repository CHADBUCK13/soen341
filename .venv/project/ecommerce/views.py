from django.shortcuts import render

def home(request):
    
    # Get Categories
    categoriesOptions = ['Phones','Food','Games']
    request.session['categoriesOptions'] = categoriesOptions


    categorySearch=""

    if request.method=="POST":
        if request.POST.get("category") is not None:
            categorySearch = request.POST.get("category")            

    if 'is_logged_in' in request.session:
        is_logged_in = request.session['is_logged_in']
    else:
        is_logged_in = False
    request.session['is_logged_in'] = is_logged_in

    # Get Items
    items = [
        {
            'category': "Phones",
            'description': "Best Phone out There!",
            'name': "iPhone 12",
            'price':1000,
            'sellerID':1234,
            'weight(g)':"200"
        },
        {
            'category': "Phones",
            'description': "Second Best Phone out There!",
            'name': "iPhone X",
            'price':1001,
            'sellerID':1234,
            'weight(g)':"204"
        }
    ]

    request.session['items'] = items


    request.session.modified = True

    return render(request,'home.html')
