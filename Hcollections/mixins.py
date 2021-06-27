from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import Http404

class BuyerRequiredMixmin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(BuyerRequiredMixmin, self).as_view(*args, **kwargs)
        return login_required(view)
    
    @method_decorator(login_required)
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_buyer:
            return super(BuyerRequiredMixmin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404
class SellerRequiredMixmin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(SellerRequiredMixmin, self).as_view(*args, **kwargs)
        return login_required(view)
    
    @method_decorator(login_required)
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_seller:
            return super(SellerRequiredMixmin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

class LoginRequiredMixmin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(LoginRequiredMixmin, self).as_view(*args, **kwargs)
        return login_required(view)
    
    @method_decorator(login_required)
    def dispatch(self, request,*args, **kwargs):
            return super(LoginRequiredMixmin, self).dispatch(request, *args, **kwargs)
