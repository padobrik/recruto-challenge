from django.http import HttpResponse

# Create your views here.

def hello_name(request):

    name = request.GET.get('name', None)
    message = request.GET.get('message', None)

    if not name or not message:
        return HttpResponse(" Please enter name OR message params to GET request")
    else:
        return HttpResponse(f'Hello {name}! {message}')

