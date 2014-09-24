from django.http import HttpResponse
from django.template import RequestContext, loader
from ground.models import Image


def index(request):
    # img = Image.objects.order_by('?')[0]
    img = Image.objects.get(name="futuri-gate")
    data = dict(data=img)
    context = RequestContext(request, data)
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))
