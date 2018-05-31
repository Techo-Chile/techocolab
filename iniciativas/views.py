import os

from django.shortcuts import render
from django.http import HttpResponse
from .models import Community_issue
from django.template import loader
from django.http import Http404
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    lastest_issues_list = Community_issue.objects.order_by('-id')[:5]
    context = {
        'lastest_issues_list': lastest_issues_list,
    }
    return render(request, 'iniciativas/index.html', context)

def detail(request, community_issue_id):
    try:
        i = Community_issue.objects.get(pk=community_issue_id)
    except Community_issue.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': i})

def results(request, community_issue_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % community_issue_id)

def vote(request, community_issue_id):
    return HttpResponse("You're voting on question %s." % community_issue_id)

@require_POST
def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'media', request.FILES['file'])
    path = default_storage.save(save_path, request.FILES['file'])
    document = Document.objects.create(document=path, upload_by=request.user)
    return JsonResponse({'document': document.id})