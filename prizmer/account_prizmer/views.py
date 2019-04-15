from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/') 
def account(request):
    args = {}
    args['user_name']=request.user.first_name + ' ' + request.user.last_name
    return render_to_response("account/base.html", args)