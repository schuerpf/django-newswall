from newswall.models import Story

def latest_story(request):
    try:
        latest_story = Story.objects.active()[0]
    except IndexError:
        latest_story = None

    return {
        'LATEST_STORY': latest_story,
    }