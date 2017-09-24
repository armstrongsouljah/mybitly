from django.db import models

from shortener.models import MyBitlyUrl

class ClickDataManager(models.Manager):
    
    def create_click(self, MyBitlyInstance):
        if isinstance(MyBitlyInstance, MyBitlyUrl):
            obj, created = self.get_or_create(mybitly_url=MyBitlyInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickData(models.Model):
    mybitly_url = models.OneToOneField(MyBitlyUrl)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    objects = ClickDataManager()

    class Meta:
        db_table = 'analytical_data'
        verbose_name = 'Click count'
        verbose_name_plural = 'Clicks count'
    
    def __str__(self):
        return '{i}'.format(i=self.count)

