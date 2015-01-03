from django.http import HttpResponse


def test(request):
    return HttpResponse("test error", status=500)
