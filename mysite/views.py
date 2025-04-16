#created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  # return HttpResponse('''jed <br> <button><a href="/removepunc">removepunc</a></button><br> <button><a href="/capitalizefirst">capfirst</a></button><br> <button><a href="/newlineremove">newlineremove</a></button><br> <button><a href="/spaceremover">spaceremover</a></button><br> <button><a href="/charcount">charcount</a></button>''')
  return render(request, "index2.html")

def analyze(request):
  purpose_value = ""
  djtext = request.POST.get('text','default')
  removepunc = request.POST.get('removepunc','off')
  upcase = request.POST.get('upcase','off')
  newlineremove = request.POST.get('newlineremove','off')
  spaceremove = request.POST.get('spaceremove','off')
  charcount = request.POST.get('charcount','off')
  
  analyzed = ""
  if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in djtext:
      if char not in punctuations:
        analyzed+=char
    djtext = analyzed
    purpose_value = 'remove punctuation'
  
  if upcase=="on":
    analyzed=""
    for char in djtext:
      analyzed+= char.upper()
    djtext = analyzed
    purpose_value='convert to uppercase'

  if newlineremove=="on":
    analyzed=""
    for char in djtext:
      if char!= "\n":
        analyzed+=char
    djtext = analyzed
    purpose_value='removed new lines'

  if spaceremove=="on":
    analyzed=""
    for index, char in enumerate(djtext):
      if not(djtext[index]==" " and djtext[index+1]==" "):
        analyzed+= char
    djtext = analyzed
    purpose_value = 'remove extraspace '
  
  if charcount == "on":
      text_length = len(djtext)
      analyzed = f"Your text is: {djtext}<br>Length of your text is: {text_length}"
      purpose_value = 'charcount'
  
  if removepunc!="on" and upcase!="on" and newlineremove!="on" and spaceremove!="on" and charcount!="on":
    return HttpResponse("Select an operation first and then try again")

  params = {'purpose':purpose_value, 'analyzed_text':analyzed}
  return render(request,'analyse2.html', params)

def about(request):
  return render(request,'about.html')

def contact(request):
  return render(request, 'contact.html')

  

# def capfirst(request):
#   return HttpResponse('''capitalize first<br> <button><a href="/">Back to home page</a></button>''')

# def newlineremove(request):
#   return HttpResponse('''newline<br> <button><a href="/">Back to home page</a></button>''')

# def spaceremover(request):
#   return HttpResponse('''spaceremover<br> <button><a href="/">Back to home page</a></button>''')

# def charcount(request):
#   return HttpResponse('''charcount<br> <button><a href="/">Back to home page</a></button>''')