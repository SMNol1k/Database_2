from django.contrib import admin
from .models import Tag, Article, Scope


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at',)
    inlines = [ScopeInline]

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ScopeAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag', 'is_main')
    list_filter = ('is_main',)

    def save_model(self, request, obj, form, change):
        if obj.is_main and Scope.objects.filter(is_main=True, article=obj.article).count() > 1:
            raise ValueError("There can only be one main scope for each article")
        super().save_model(request, obj, form, change)

admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Scope, ScopeAdmin)