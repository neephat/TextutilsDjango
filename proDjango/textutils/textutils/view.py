# I created the file
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
    # return HttpResponse(
    #     '''<h1>My First Django Site</h1> <a style="text-decoration:none "
    #     href="https://www.facebook.com/neephat/">Stay with me</a><a style="margin:10px; text-decoration:none"
    #     href="http://127.0.0.1:8000/about/">About</a><a style="margin:10px; text-decoration:none"
    #     href="http://127.0.0.1:8000/services/">Service</a><a style="margin:10px; text-decoration:none"
    #     href="http://127.0.0.1:8000/contactus/">Contact</a><a style="margin:10px; text-decoration:none"
    #     href="http://127.0.0.1:8000/categories">Category</a>''')


def about(request):
    return HttpResponse('''<h1>Marvel</h1><a href="http://127.0.0.1:8000/">Back</a>''')


def service(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check the switch values
    remvpunc = request.POST.get('remvpunc', 'off')
    upcase = request.POST.get('upcase', 'off')
    nlineremover = request.POST.get('nlineremover', 'off')
    xtraspaceremover = request.POST.get('xtraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # Error Message
    if djtext == "":
        output = "This site cannot be reached\nPlease write anything in the textarea and select a operation for viewing result"
        return HttpResponse(output, content_type="text/plain")

    # Removing punctuations
    if remvpunc == "on":
        punctuations = '''`!@#$%^&*(){}[],.":;'<>'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        param = {'purpose': 'Removed Punctuations', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', param)
        djtext = analyze

    # Uppercasing chars
    if upcase == "on":
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        param = {'purpose': 'Uppercased Alphabets', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', param)
        djtext = analyze

    # New Line Remover
    if nlineremover == "on":
        analyze = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char
            else:
                print("No")
        print("Pre", analyze)
        param = {'purpose': 'New Line Removed', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', param)
        djtext = analyze

    # Extra Space Remover
    if (xtraspaceremover == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == "" and djtext[index+1] == ""):
                analyze = analyze + char
        param = {'purpose': 'Extra Space Removed', 'analyzed_text': analyze}
        djtext = analyze


    # Character Counter
    if (charcounter == "on"):
        analyze = len(djtext)
        param = {'purpose': 'Characters Counted', 'analyzed_text': analyze}

    # Chechking all buttons are checked or not
    if (remvpunc != "on" and upcase != "on" and nlineremover != "on" and xtraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("This site cannot be reached/nPlease select a operation for viewing result")

    return render(request, 'analyze.html', param)


def contact(request):
    return HttpResponse('''<h1>Contact with us</h1><a href="http://127.0.0.1:8000/">Back</a>''')


def category(request):
    return HttpResponse('''<h1>Product Categories</h1><a href="http://127.0.0.1:8000/">Back</a>''')
