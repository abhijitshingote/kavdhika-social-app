from django.contrib import admin
from .models import Post, Comment, Reaction

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_preview', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')
    date_hierarchy = 'created_at'
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content_preview', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username', 'post__content')
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reaction_type', 'created_at')
    list_filter = ('reaction_type', 'created_at')
    search_fields = ('user__username', 'post__content')
