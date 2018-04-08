from django.shortcuts import render, render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
    # context = {
    #     "time": strftime("%I:%M %p %a %m-%d-%Y",localtime())
    # }
    

    
    return render(request,'session_words/index.html')

def add(request):
    if request.method == "POST":
        if not 'add_word' in request.POST:
            add_word = ""
        else:
            add_word = request.POST['add_word']
        if not 'color' in request.POST:
            color = "black"
        else:
            color = request.POST['color']
        if not 'font' in request.POST:
            font = '16px'
        else:
            font = '26px'
        if not "feed" in request.session:
            request.session['feed'] = []
    
        data = {'add_word': add_word, 'color': color, 'font':font, 'time':strftime("%I:%M %p %a %m-%d-%Y",localtime())}
        live_feed = request.session['feed']
        live_feed.append(data)
        request.session['feed'] = live_feed

    return redirect('/session_words')

    
def clear(request):
     
    request.session.clear()

    
    return redirect('/session_words')