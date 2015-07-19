from __future__ import absolute_import
from django.db import models
from celery import shared_task
from .models import section, story
from datetime import datetime, timezone


def get_stories():
    stories = story.objects.all()
    return stories

def get_sections(a_story, next_position):
    sections = a_story.section_set.filter(position=next_position)
    return sections

def get_voters(a_story):
    num_voters = a_story.section_set.values_list('user__username').distinct().count()
    return num_voters

def find_a_winner(a_story, next_position):
    sections = a_story.section_set.filter(position=next_position).order_by('-votes')
    winning_section = sections.first()
    drawing_sections = a_story.section_set.filter(position=next_position, votes=winning_section.votes)
    if drawing_sections.count() > 1:
        for a_section in drawing_sections:
            voters = a_story.section_set.filter(pk=a_section.id).values_list('votes_cast__username')
            for vote in voters:
                print(vote)
                if a_story.story_owner.username in vote:
                    winning_section = a_section
                    return winning_section
            return None
    else:
        return winning_section

def update_sections(winning_section, next_position, a_story):
    a_story.section_set.filter(pk=winning_section.id).update(status = 'approved')
    a_story.section_set.filter(position=next_position).exclude(pk=winning_section.id).update(status = 'rejected')
    story.objects.filter(pk=a_story.id).update(current_length = a_story.current_length + 1)    

@shared_task
def check_for_winners():
    stories = get_stories()
    for a_story in stories:
        next_position = a_story.current_length + 1
        current_sections = get_sections(a_story, next_position)
        if current_sections:
            start_date = current_sections.first().created
            num_voters = get_voters(a_story)
            now = datetime.now(timezone.utc)
            delta = now - start_date
            time_in_hours = (delta.seconds / 60) / 60
            if delta.seconds > 1:
                winning_section = find_a_winner(a_story, next_position)
                if winning_section:
                    update_sections(winning_section, next_position, a_story)



                    
                


    