from django.db import models
from django.conf import settings
from .utils import code_generator, create_shortcode
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class MyBitlyUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(MyBitlyUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    def refresh_shortcodes(self, items=None):
        qs = MyBitlyUrl.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class MyBitlyUrl(models.Model):
    url = models.CharField(max_length=220 )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    active    = models.BooleanField()

    objects = MyBitlyUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode =="":
            self.shortcode = create_shortcode(self)
        if not "http://" in self.url:
            self.url = "http://" + self.url
        super(MyBitlyUrl, self).save(*args, **kwargs)
        

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("site:short", kwargs={'shortcode':self.shortcode}, host='www', scheme='http' )
        # url_path = "http://www.mybtly.com:8000/{shortcode}".format(shortcode=self.shortcode)
        return url_path
        # return "www.mybitly.com:8000/{shortcode}".format(shortcode=self.shortcode)

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'
