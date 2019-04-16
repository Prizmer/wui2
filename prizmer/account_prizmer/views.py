from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/') 
def account(request):
    args = {}
    args['user_name']=request.user.first_name + ' ' + request.user.last_name
    return render_to_response("account/base.html", args)

def electric_info(request):
    args = {}
    dt_electric = [[1,2],[1,3]]
    args['dt_electric'] = dt_electric
    from time import sleep
    sleep(1)
    print 'after 1'
    return render_to_response("account/electric_info.html", args)