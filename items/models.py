from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
import threading
import re
import logging
import asyncio
def sendTelegram(product):
    try :
        from pyrogram import Client
        api_id = 1234
        api_hash = ""


        app = Client(
            "my_bot",
            api_id=api_id, api_hash=api_hash
        )

        async def main():
            async with Client("my_account", api_id, api_hash) as app:
                await app.send_photo("me", product.image.file, caption=f"**{product.name}**\n\nPrice:\n__{product.price}__\n\nCategory:\n__{product.category}__\n\n\n{product.description}")


        asyncio.run(main())

        
    except Exception as e :
        logging.exception("When we tried sending in Telegram we saw some problems", exc_info=True)
class Items(models.Model):
    """کالاها"""
     
    _first_ = True
    _choices_ = (
        ('sport', 'sport'),
        ('classic', 'classic'),
        ('normal', 'normal'),
        ('modern', 'modern'),
        ('new', 'new'),
        ('old', 'old'),
        ('racing', 'racing'),
        ('other', 'other'),
                         
    )
    name     = models.CharField(verbose_name="نام کالا",max_length=100)
    category = models.CharField(verbose_name="دسته بندی",choices=_choices_, max_length=10)
    image    = ImageField(verbose_name="تصویر", upload_to="media/images/")
    brand    = models.CharField(verbose_name="شرکت سازنده", max_length=25)

    available   = models.BooleanField(verbose_name="موجود",default=True)
    number      = models.IntegerField(verbose_name="موجودی",editable=True)
    price       = models.IntegerField(verbose_name="قیمت")
    description = models.TextField(verbose_name="توضیحات",max_length=1000)
    info        = models.TextField(verbose_name="مشخصات",max_length=10000,null=True, blank=True)
    views       = models.IntegerField(default=0)
    boughts      = models.IntegerField(default=0)
    
    slug = models.SlugField(verbose_name="لینک مایه", unique=True)



    def bought(self, number):
        self.number = self.number - number
        self.save()

    def offerBYpercent(self, percent=10):
        self.price = self.price - (self.price * percent / 100 ) 
        self.save()

    def offerBYamount(self, amount=10):
        self.price = self.price - amount
        self.save()

    def IncreasingInventory(self, number):
        self.number = self.number + number
        self.save()

    def IncreasingBought(self):
        self.boughts += 1
        self.save()

    def MainPageItems():
        return (Items.objects.filter(available=True)).order_by("-id")[0:9]

    def IncreasingViews(self):
        self.views += 1
        self.save()

    def newCollection():
        return Items.objects.filter(available=True).order_by("-id")[:2]



    def save(self, *args, **kwargs):
        if self._first_ :
            details_lst = re.findall(".{1,25} = .{1,50};", self.info)
            details_arr = {}
            for detail in details_lst :
                name = re.findall("(.{1,25}) =", detail)[0]
                value = re.findall("= (.{1,50});", detail)[0]
                
                details_arr[name] = value
                print(1)
            
            self.info = details_arr

           
        if self.number <= 0:
            self.available = False
            self.number = 0
        else :
            self.available = True

        telegram_sending = threading.Thread(sendTelegram, (self, ))
        telegram_sending.start()
        super(Items, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "کالاها"


    def __str__(self):
        return self.name






