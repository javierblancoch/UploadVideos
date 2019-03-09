from django.contrib import admin
from web.models import video

# Register your models here.
@admin.register(video)
class videoAdmin(admin.ModelAdmin):
    pass
