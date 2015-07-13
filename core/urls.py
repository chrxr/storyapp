from django.conf.urls import url, include
from django.views.generic.base import RedirectView, TemplateView



from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create-account/$', views.createAccount, name='create-account'),
    url(r'^welcome/$', views.Welcome, name='welcome'),
    url(r'^stories/$', views.stories, name='stories'),	
    url(r'^stories/create-story/$', views.createStory, name='create-story'),
    url(r'^stories/(?P<story_slug>[a-zA-Z0-9_.-]+)/$', views.storyDetails, name='story-details'),
    url(r'^stories/(?P<story_slug>[a-zA-Z0-9_.-]+)/sections/$', views.sections, name='sections'),
    url(r'^stories/(?P<story_slug>[a-zA-Z0-9_.-]+)/sections/(?P<section_id>[a-zA-Z0-9_.-]+)/vote/$', views.vote, name='vote'),
    url(r'^stories/(?P<story_slug>[a-zA-Z0-9_.-]+)/sections/create-section/$', views.createSection, name='create-section'),
]