from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if not 'word' in request.session:
        request.session['word'] = 0
    else:
        request.session['word'] = request.session['word']

    return render(request,'survey_form/index.html')

def process(request):
    request.session['word'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect("/result")


def result(request):
    
    return render(request,'survey_form/result.html')
