from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    my_dic={'insert_me' : "This is from firstApp view add donw by abba tanim"}
    return render(request,"firstapp/index.html",context=my_dic)
