from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from analytics.models import ClickData

from .forms import ShortenUrl
from .models import MyBitlyUrl

class HomeView(View):
    def get(self, request, *args, **kwargs):
        my_title = "MyBitly.com"
        form = ShortenUrl(request.POST or None)
        context = {
            "form":form,
            "title":my_title
        }
        return render(request, template_name="home.html", context=context)

    def post(self, request, *args, **kwargs):
        form = ShortenUrl(request.POST or None)
        context = {
            "form":form,
        }

        template_name = "home.html" 

        if form.is_valid():
            print(form.cleaned_data.get('url'))
            new_url =  form.cleaned_data.get("url")
            act = form.cleaned_data.get("active")
            obj, created = MyBitlyUrl.objects.get_or_create(url=new_url, active=act)

            context = {
                "code":obj.get_short_url,
                "object": obj,
                "created": created,
            }
            if created:
                template_name = "success.html"
            else:
                template_name="exists.html"
        
        return render(request, template_name, context=context)



class MyBitlyRedirectView(View):
      
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = MyBitlyUrl.objects.filter(shortcode__iexact=shortcode)
        print(qs)
        # obj = get_object_or_404(MyBitlyUrl, shortcode=shortcode)
        if qs.count() !=1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickData.objects.create_click(obj))
        return HttpResponseRedirect(obj.url)


        # obj = get_object_or_404(MyBitlyUrl, shortcode=shortcode)
        # ClickData.objects.create_click(obj)
        # qs = MyBitlyUrl.objects.filter(shortcode__iexact=shortcode)
        # if qs.count() == 1 and qs.exists():
        #   obj = qs.first()
        #   print(ClickData.objects.create_click(obj))
        #   return HttpResponseRedirect(obj.url)
        # raise Http404

    # try:
    #    obj = MyBitlyUrl.objects.get(shortcode=shortcode)
    # except:
    #     obj = MyBitlyUrl.objects.all().first()
    # shortcode = ""

    # obj_url = None
    # qs = MyBitlyUrl.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists and qs.count == 1:
    #    obj = qs.first()
    #     obj_url = obj.url
