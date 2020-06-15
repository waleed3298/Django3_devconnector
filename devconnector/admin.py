from django.contrib import admin
from .models import Developer,Education,Experience,Posts,Comments

admin.site.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Posts)
admin.site.register(Comments)
