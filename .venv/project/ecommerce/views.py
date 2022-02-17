from django.shortcuts import render

def home(request):
    
    if 'is_logged_in' in request.session:
        is_logged_in = request.session['is_logged_in']
    else:
        is_logged_in = False
    request.session['is_logged_in'] = is_logged_in
    request.session.modified = True

    return render(request,'home.html')
