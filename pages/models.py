from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from froala_editor.fields import FroalaField
from django.core.validators import MaxValueValidator, MinValueValidator
from django import template
register = template.Library()


class Section(models.Model):

    title = models.CharField(max_length=512, null=True, blank=True)
    content = FroalaField()
    image = models.ImageField(upload_to='imgaes', null=True, blank=True)
    sequence_number = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tag_name

class OdooVersion(models.Model):
    version_name = models.CharField(max_length=20)
    def __str__(self):
        return self.version_name
    
class CommentReply(models.Model):
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=60,default='Techneith')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
    
class Comments(models.Model):
    title = models.CharField(max_length=100, null=True,blank=True)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=60,default='Anonymous')
    replies = models.ManyToManyField(CommentReply, null=True,blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_replies(self):
        ls = []
        for repli in self.replies.all():
            if repli.published:
                ls.append({"content":repli.content,
                           "created_at":repli.created_at})
        return ls


class Article(models.Model):
    heading = models.CharField(max_length=512)
    slug = models.SlugField(max_length=512)
    date_posted = models.DateTimeField(default=timezone.now)
    read_time = models.CharField(max_length=20, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    header_image = models.ImageField(
        upload_to='images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    order_number = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comments, null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(Article, self).save(*args, **kwargs)
        
    def datepublished(self):
        return self.date_posted.strftime('%B %d, %Y')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.heading

    def get_comments(self):
        comment_list = []
        for comment in self.comments.all().order_by('-created_at'):
            if comment.published:
                comment_list.append({
                    "title" : comment.title,
                    "content" : comment.content,
                    "author" : comment.author,
                    "replies" : list(comment.get_replies()),
                    "created_at" : comment.created_at
                    })
        return comment_list


class Page(models.Model):
    slug = models.SlugField(max_length=512)
    comments = models.ManyToManyField(Comments, null=True,blank=True)

    def get_comments(self):
        comment_list = []
        for comment in self.comments.all().order_by('-created_at'):
            if comment.published:
                comment_list.append({
                    "title" : comment.title,
                    "content" : comment.content,
                    "author" : comment.author,
                    "replies" : list(comment.get_replies()),
                    "created_at" : comment.created_at
                    })
        return comment_list



class Product(models.Model):
    name = models.CharField(max_length=512)
    type = models.CharField(max_length=30, default='Add On')
    stripe_price = models.CharField(max_length=100, null=True, blank=True)
    odoo_crm_tech_name = models.CharField(max_length=100, null=True, blank=True)
    version = models.ManyToManyField(OdooVersion)
    card_color = models.CharField(max_length=7, default='#7dffbe')
    icon_url = models.URLField(max_length=512, null=True, blank=True)
    technical_name = models.SlugField(max_length=100)
    doc = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    order_number = models.IntegerField(default=0)
    star_rating = models.IntegerField(default=5,validators=[MaxValueValidator(5),MinValueValidator(0)])
    total_ratings_given = models.IntegerField(default=6,validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    total_sales = models.IntegerField(validators=[MinValueValidator(0)])
    creation_time = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    comments = models.ManyToManyField(Comments, null=True,blank=True)

    def stars(self):
        return range(self.star_rating)

    def checkvideo(self):
        return True if self.icon_url.endswith(".mp4") else False

    def form_parameters(self):
        vers = [v.version_name for v in self.version.all()]
        return vers
    
    def get_comments(self):
        comment_list = []
        for comment in self.comments.all().order_by('-created_at'):
            if comment.published:
                comment_list.append({
                    "title" : comment.title,
                    "content" : comment.content,
                    "author" : comment.author,
                    "replies" : list(comment.get_replies()),
                    "created_at" : comment.created_at
                    })
        return comment_list
    
    def nostars(self):
        return range(5-self.star_rating)

    class Meta:
        ordering = ['-total_sales']

    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class AppBuyRequest(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField()
    odoo_product = models.TextField()
    odoo_version = models.TextField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class DashboardForm(models.Model):

    name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    email = models.EmailField()
    data = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Work(models.Model):

    title = models.CharField(max_length=400)
    done_by = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=500, default=False)

    def __str__(self):
        return self.title


class TrackVisiters(models.Model):
    email = models.CharField(max_length=100, null=True, blank=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} Visited {self.visit_count} Times'
