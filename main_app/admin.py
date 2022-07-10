from django.contrib import admin
from .models import Dog, Played, Toy
# Register your models here.


admin.site.register(Dog)
admin.site.register(Played)
admin.site.register(Toy)