from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

POST_STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY_OPTIONS = (
    ('R', 'Reviews'),
    ('A', 'Announcements'),
    ('N', 'News'),
    ('OP', 'Opinion'),
    ('P', 'Previews'),
    ('S', 'Streaming'),
    ('T', 'Tech'),
    ('M', 'Miscellaneous'),
)


class Post(models.Model):

    title = models.CharField(max_length="100", unique=True)
    slug = models.SlugField(max_length="100", unique=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="blog_posts")
    category = models.CharField(max_length=1, choices=CATEGORY_OPTIONS) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    post_image = CloudinaryField(name='image', default='placeholder')
    status = models.IntegerField(choices=POST_STATUS, default=0)
    upvotes = models.ManyToManyField(User, related_name='blog_upvotes', 
                                     blank=True)
    downvotes = models.ManyToManyField(User, related_name="blog_downvotes",
                                       blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()   

      
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
