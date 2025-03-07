from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = HTMLField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d')}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_at.strftime('%Y-%m-%d')}"

class Reaction(models.Model):
    REACTION_CHOICES = [
        ('LIKE', '👍'),
        ('LOVE', '❤️'),
        ('LAUGH', '😄'),
        ('SAD', '😢'),
        ('ANGRY', '😠'),
    ]
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES, default='LIKE')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['post', 'user']
    
    def __str__(self):
        return f"{self.user.username} reacted with {self.get_reaction_type_display()} to post #{self.post.id}"
