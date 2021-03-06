from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import story, section
from .forms import StoryForm, SectionForm, CreateAccountForm
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views, authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the stories index.")

def stories(request):
    stories = story.objects.all()
    return render(request, 'core/stories.html', {"stories": stories})

def storyDetails(request, story_slug):
    this_story = get_object_or_404(story, slug=story_slug)
    this_story_sections = section.objects.filter(story=this_story, status='approved').order_by('position')
    return render(request, 'core/story_details.html', {"story": this_story, "sections": this_story_sections})

def sections(request, story_slug):
    this_story = get_object_or_404(story, slug=story_slug)
    next_position = this_story.current_length + 1
    sections = this_story.section_set.filter(position=next_position)
    return render(request, 'core/sections.html', {"sections": sections, 'story': this_story})

@login_required
def createStory(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            new_story = form.save(commit=False)     
            story_slug = slugify(new_story.title)
            slug_check = story.objects.filter(slug=story_slug)
            if slug_check:
                return HttpResponse('Oh! Sorry, that slug already exists.')
            else:
                print('This is about to be saved')
                new_story.save()
                return HttpResponse("Thanks!")
    else:
        form = StoryForm()

    return render(request, 'core/story_form.html', {'form': form})

@login_required
def createSection(request, story_slug):
    this_story = get_object_or_404(story, slug=story_slug)
    next_position = this_story.current_length + 1
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.story = this_story
            new_section.user = request.user
            new_section.position = next_position
            new_section.save()
        return HttpResponse("Thanks!")
    else:
        form = SectionForm()
 
    return render(request, 'core/section_form.html', {'form': form, 'story': this_story})


def createAccount(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            request.session['user_name'] = new_user.username
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse('home'));
    else:
        form = CreateAccountForm()
 
    return render(request, 'core/create_account.html', {'form': form})

def Welcome(request):
    username = request.session['user_name']
    return render(request, '/')

def check_if_it_won(this_section, this_story):
    num_voters = this_story.section_set.values_list('user__username').distinct().count()
    this_section = section.objects.get(pk=this_section.id)
    if this_section.votes > (num_voters / 2):
        section.objects.filter(pk=this_section.id).update(status = 'approved')
        story.objects.filter(pk=this_story.id).update(current_length = this_story.current_length + 1)
        this_story.section_set.filter(position=this_section.position).exclude(pk=this_section.id).update(status = 'rejected')
        return True
    else:
        return None

def vote(request, story_slug, section_id):
    if request.method == 'POST':
        this_story = get_object_or_404(story, slug=story_slug)
        this_section = section.objects.get(pk=section_id)
        has_user_made_a_section = section.objects.filter(story=this_story, user=request.user)
        if has_user_made_a_section:
            sections = this_story.section_set.filter(position=this_section.position).exclude(votes_cast=None).distinct()
            vote_list = []
            for a_section in sections:
                voters = a_section.votes_cast.all()
                for voter in voters:
                    vote_list.append(voter)
            if request.user in vote_list:
                return HttpResponse("Sorry, you've already voted on this bit!")
            this_section.votes_cast.add(request.user)
            section.objects.filter(pk=section_id).update(votes = this_section.votes + 1)
            did_it_win = check_if_it_won(this_section, this_story)
            if did_it_win:
                return HttpResponse("CONGRATULATIONS!")
            else:
                return HttpResponse("Thanks for voting!")
        else:
            return HttpResponse("Sorry, you need to write a section before you can vote")
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

