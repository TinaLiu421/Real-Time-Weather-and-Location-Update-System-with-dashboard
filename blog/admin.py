from django.contrib import admin
from .models import Philips
from .models import David
from .models import Entry
# Register your models here.
admin.site.register(Philips)
admin.site.register(David)
admin.site.register(Entry)