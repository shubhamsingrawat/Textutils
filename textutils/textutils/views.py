# this oue first file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print(request.GET.get('text','default'))
    return render(request,'index.html')
    
def removepunch(request):
    raw_text = request.POST.get('text','default')
    removepunch = request.POST.get('removepunch','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('spaceremover','off')
    wordcount = request.POST.get('wordcount','off')
    what =""
    
    if removepunch=='on' :
        punch = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        freshstr=''
        for char in raw_text:
            if char not in punch:
                freshstr = freshstr+char
        raw_text = freshstr 
        what = 'Removepunch '
        params={'what':what,'analyzedText': freshstr}
        
    if capitalize=='on':
        cap = ""
        for c in raw_text:
            cap = cap+c.capitalize()
        what = what + 'capitalize '
        params={'what':what,'analyzedText':cap}
        raw_text = cap
        
    if newlineremove=='on':
        newlinerm = ""
        for c in raw_text:
            if c !='\n' and c !='\r':
                newlinerm = newlinerm+c
        what = what + 'newlineremove '
        params={'what':what,'analyzedText':newlinerm}
        raw_text = newlinerm
       
    if extraspaceremover=='on':
        spacerm = "" 
        for i,c in enumerate(raw_text):
            if not (c==' ' and raw_text[i+1]==' '):
                spacerm = spacerm + c
        what = what + 'spaceremover '
        params={'what':what,'analyzedText':spacerm}
        raw_text = spacerm
        
    if wordcount=='on':
        count = len(raw_text)
        params={'what':'wordcount','analyzedText':count}
        return render(request,'analyze.html',params)

#checkin if every Switch
    if removepunch!='on' and capitalize!='on' and newlinerem!='on' and extraspaceremover!='on':
        return HttpResponse("Error")
    else:
        return render(request,'analyze.html',params)



 

