from django.shortcuts import render
from django.http import HttpResponse
import datetime
from firstapp.models import Topic, Webpage, AccessRecord


# Create your views here.
def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    Webpage_list= AccessRecord.objects.order_by("date")
    date_dict={'access_records': Webpage_list}
    return render(request,"firstapp/index.html",context=date_dict)
