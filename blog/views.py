from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        upvoted = False
        downvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True    

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        upvoted = False
        downvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True   

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()    

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment": CommentForm()
            },
        )


class Upvote(View):
    """ Allows upvoting"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Downvote(View):
    """ Allows downvoting"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class SearchPost(View):
    """ Search for posts on the blog"""

    def get(self, request):
        
        return render(request, 'search.html')

    def post(self, request):
       
        searched = request.POST.get('searched')
        post = Post.objects.filter(Q(title__icontains=searched)
                                   | Q(excerpt__icontains=searched))
        
        context = {
                'searched': searched
        }
        if(searched):
            paginator = Paginator(post, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            print(page_obj)
            context = {
                'page_obj': page_obj,
                'searched': searched
            }
            return render(request, 'search.html', context)     
        else:
            return render(request, 'search.html', context)  
           
class EditComment(UpdateView):
    """ Allows user to edit commment """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    


def delete_comment(request, comment_id):
    """allows user to delete comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))           