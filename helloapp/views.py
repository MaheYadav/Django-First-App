from django.http  import HttpResponse

# Create your views here.
def home(request):
	Response="<h1>Hi wellcome To  The First django web application</h1>"
	return HttpResponse(Response)
