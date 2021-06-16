from .forms import MembershipForm
from django.shortcuts import redirect, render

# Create your views here.
def membership_form(request):
    context={}
    if request.POST:
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member:member_confirm')
        else:
            context['membership_form']=form
    
    else:
        form = MembershipForm()
    
    context['membership_form']=form
    return render(request, 'member/form.html', context)

def membershipConfirm_view(request):
    return render(request, 'member/confirm.html')