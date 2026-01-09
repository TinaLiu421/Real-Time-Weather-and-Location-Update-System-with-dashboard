from django.db import models

class Entry(models.Model):
#Fields
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #Methods
    def __str__(self):
        return 'Entry #{}'.format(self.id)
    class Meta:
        verbose_name_plural = 'entries'
        
class Philips(models.Model):
    Inventory_no=models.CharField(max_length=255)
    Location=models.CharField(max_length=255)
    Owner=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    Price=models.CharField(max_length=255)
    Purchase_date=models.DateTimeField(auto_now_add=True)
    Active=models.BooleanField(default=False)
    def __str__(self):
        return 'Philips #{}'.format(self.id)


class David(models.Model):
    Owner=models.CharField(max_length=255)
    Full_name=models.CharField(max_length=255)
    Title=models.CharField(max_length=255)
    Phone=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    def __str__(self):
        return 'David #{}'.format(self.id)