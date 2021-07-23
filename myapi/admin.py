from django.contrib import admin

# Register your models here.

from .models import User
admin.site.register(User)

from .models import Medication
admin.site.register(Medication)

from .models import Ingredient
admin.site.register(Ingredient)
