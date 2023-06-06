from django.shortcuts import render
from .models import UtmData
# Create your views here.
def index(request):
    # do token handling
    # medium and source are mandatory for lead source capture
    # request.session["utm_medium"] = "referral"
    # request.session["utm_source"] = "internal"
    # campaign, term and content are optional fields
    # request.session["utm_campaign"] = "july"
    # request.session["utm_term"] = token
    # request.session["utm_content"] = "buy-me"
    utm_medium = request.GET.get('utm_medium')
    utm_source = request.GET.get('utm_source')
    data = UtmData.objects.create(utm_medium=utm_medium, utm_source=utm_source)
    data.save()

    print(utm_medium)
    print(utm_source)
    return render(request, "index.html")

def advertisment(request):
    return render(request,"advertisment.html")