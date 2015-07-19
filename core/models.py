from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

STATUS_CHOICES = (
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('submitted', 'Submitted'),
)

class Genre(models.Model):
    title = models.CharField('Genre', max_length=255)

    def __str__(self):
        return self.title

class story(models.Model):
    title = models.CharField('Story title', max_length=255)
    genre = models.ForeignKey(Genre, blank=True, null=True)
    slug = models.SlugField('Story slug', max_length=255, null=True, blank=True, unique=True)
    story_owner = models.ForeignKey(User, blank=True, null=True)
    current_length = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(story, self).save(*args, **kwargs)


class section(models.Model):
    body_content = models.TextField('Story body')
    votes = models.IntegerField('Number of votes', default=0)
    status = models.CharField('Story status', max_length=255, choices=STATUS_CHOICES, default='submitted')
    position = models.IntegerField('Position of section in the story', null=True, blank=True)
    story = models.ForeignKey('story')
    user = models.ForeignKey(User, blank=True, null=True)
    votes_cast = models.ManyToManyField(User, blank=True, related_name='votes_cast')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Story section'
        verbose_name_plural = 'Story sections'

    def __str__(self):
        story_title = self.story.title
        story_user = self.user.username
        return story_title + ' | ' + story_user

