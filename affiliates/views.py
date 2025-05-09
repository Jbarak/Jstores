from django.shortcuts import render
from .models import AffiliateLink

def affiliate_list(request):
    affiliates = AffiliateLink.objects.all()
    return render(request, 'affiliates/affiliate_list.html', {'affiliates': affiliates})
 