from django.http import HttpResponseRedirect

def permession(viewfunc):
    def wrapper(request,*args,**kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return  viewfunc(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrapper