from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import InstaProfiles,followers,targets,CustomerInteractionsOnFollowers,CustomerInteractionsOnTarget

admin.site.register(InstaProfiles)
admin.site.register(followers)
admin.site.register(targets)
admin.site.register(CustomerInteractionsOnFollowers)
admin.site.register(CustomerInteractionsOnTarget)
