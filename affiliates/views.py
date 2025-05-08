from django.shortcuts import render
from .models import Affiliate

def affiliate_list(request):
    affiliates = Affiliate.objects.all()
    return render(request, 'affiliates/affiliate_list.html', {'affiliates': affiliates})
