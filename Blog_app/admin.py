from django.contrib import admin
from .models import BlogPost,LoginForm,Blogger
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','blogger')
    
class BloggerAdmin(admin.ModelAdmin):
    display = ('name',)
        
admin.site.register(LoginForm)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Blogger,BloggerAdmin)

