from django.contrib import admin

from .models import Article, Section, Contact, Work, TrackVisiters, Tag, Product,DashboardForm, OdooVersion, AppBuyRequest, CommentReply, Comments,Page

# Register your models here.
admin.site.register(Section)
admin.site.register(Contact)
admin.site.register(AppBuyRequest)
admin.site.register(Work)
admin.site.register(TrackVisiters)
admin.site.register(Tag)
admin.site.register(OdooVersion)
admin.site.register(DashboardForm)
admin.site.register(Comments)
admin.site.register(CommentReply)
admin.site.register(Page)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('heading', 'date_posted', 'featured', 'order_number')

admin.site.register(Article, ArticleAdmin)


# Product Admin Register
# class ProductAdmin(admin.ModelAdmin):
#     list_display =('name', 'featured', 'order_number')
# admin.site.register(Product, ProductAdmin)

