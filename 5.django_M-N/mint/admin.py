from django.contrib import admin
from mint.models import Article

admin.site.register(Article)

# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'title','tag_list']
#     search_fields = ('title', 'content')
#     prepopulated_fields = {'slug':('title',)}

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')

#     def tag_list(self, obj):
#         return u", ".join(o.name for o in obj.tags.all())