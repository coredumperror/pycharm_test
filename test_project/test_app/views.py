from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'test_app/index.html', {})
