from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Post, Comment, Reaction
from .forms import PostForm, CommentForm

def home(request):
    """Display the feed of all posts."""
    posts = Post.objects.all().annotate(
        comment_count=Count('comments'),
        reaction_count=Count('reactions')
    )
    
    # Get reactions summary for each post
    reaction_counts = {}
    for post in posts:
        post_reactions = {}
        for reaction_type, emoji in Reaction.REACTION_CHOICES:
            post_reactions[reaction_type] = post.reactions.filter(reaction_type=reaction_type).count()
        reaction_counts[post.id] = post_reactions
    
    context = {
        'posts': posts,
        'title': 'Family Feed',
        'reaction_choices': Reaction.REACTION_CHOICES,
        'reaction_counts': reaction_counts
    }
    return render(request, 'kavdhika_app/home.html', context)

def post_detail(request, post_id):
    """Display a single post with its comments and reactions."""
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    
    # Handle new comment submission
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('kavdhika_app:post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    
    # Get reactions summary
    reactions = post.reactions.all()
    reaction_counts = {}
    for reaction_type, emoji in Reaction.REACTION_CHOICES:
        reaction_counts[reaction_type] = reactions.filter(reaction_type=reaction_type).count()
    
    # Check if the current user has reacted
    user_reaction = None
    if request.user.is_authenticated:
        user_reactions = reactions.filter(user=request.user)
        if user_reactions.exists():
            user_reaction = user_reactions.first().reaction_type
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'reaction_counts': reaction_counts,
        'user_reaction': user_reaction,
        'title': f'Post by {post.author.username}',
        'reaction_choices': Reaction.REACTION_CHOICES
    }
    return render(request, 'kavdhika_app/post_detail.html', context)

@login_required
def create_post(request):
    """Create a new post."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('kavdhika_app:post_detail', post_id=new_post.id)
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'title': 'Create Post'
    }
    return render(request, 'kavdhika_app/create_post.html', context)

@login_required
def react_to_post(request, post_id):
    """Handle reactions to posts."""
    if request.method == 'POST':
        reaction_type = request.POST.get('reaction_type')
        if reaction_type not in [choice[0] for choice in Reaction.REACTION_CHOICES]:
            return JsonResponse({'status': 'error', 'message': 'Invalid reaction type'})
        
        post = get_object_or_404(Post, id=post_id)
        
        # Check if user already reacted to this post
        try:
            reaction = Reaction.objects.get(post=post, user=request.user)
            if reaction.reaction_type == reaction_type:
                # If clicking same reaction, remove it
                reaction.delete()
                action = 'removed'
            else:
                # If clicking different reaction, update it
                reaction.reaction_type = reaction_type
                reaction.save()
                action = 'updated'
        except Reaction.DoesNotExist:
            # Create new reaction
            Reaction.objects.create(
                post=post,
                user=request.user,
                reaction_type=reaction_type
            )
            action = 'added'
        
        # Return updated reaction counts
        reaction_counts = {}
        for r_type, emoji in Reaction.REACTION_CHOICES:
            reaction_counts[r_type] = post.reactions.filter(reaction_type=r_type).count()
        
        return JsonResponse({
            'status': 'success',
            'action': action,
            'reaction_counts': reaction_counts
        })
    
    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'})

@login_required
def delete_comment(request, comment_id):
    """Delete a comment."""
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Only allow comment author to delete
    if request.user != comment.author:
        messages.error(request, "You cannot delete someone else's comment.")
        return redirect('kavdhika_app:post_detail', post_id=comment.post.id)
    
    post_id = comment.post.id
    comment.delete()
    messages.success(request, 'Your comment has been deleted.')
    return redirect('kavdhika_app:post_detail', post_id=post_id)
