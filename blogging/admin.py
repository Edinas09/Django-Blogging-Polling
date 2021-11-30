from django.contrib import admin
from blogging.models import Post, Category # import all models

# Register your models here.

class CategoriesInline(admin.TabularInline):
    model = Post.categories.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline, ]
    exclude = ('categories',)



# and a new admin registration
admin.site.site_header = 'Admin Blog - Django - UW'
# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)



