from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from accounts.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Account
from django.views import generic


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.cleaned_data.get('profile_image')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            accounts = authenticate(email=email, password=raw_password)
            login(request, accounts)
            return redirect('register_confirm')
        else:
            context['registration_form'] = form
            
        
    else:
        form = RegistrationForm()
    context['registration_form'] = form
    return render(request, 'accounts/register.html', context)

def registrationConfirm_view(request):
    return render(request, 'accounts/register_confirm.html')

def logout_view(request):
	logout(request)
	return render (request, 'accounts/logout.html')



def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home:home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home:home")


    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)

def profile_view(request):
    context = {}
    user = request.user
    form = RegistrationForm(request.POST)
    if user.is_authenticated:
        return render(request, 'accounts/account_detail.html', context)
    
    
@login_required(login_url='login/')
def account_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user,)

        if form.is_valid():
            form.initial = {
                "email": request.POST.get('email'),
                "username": request.POST.get('username'),
                "first_name": request.POST.get('first_name'),
                "last_name": request.POST.get('last_name'),
                "phone":request.POST.get('phone'),
                "designation": request.POST.get('designation'),
                "qualification": request.POST.get('qualification'),
                "address": request.POST.get('address'),
                "profile_image": request.POST.get('profile_image'),
                }
            form.save()
            context['success_message'] = "updated"

    else:
        form = AccountUpdateForm(
            initial= {
                "email": request.user.email,
				"username": request.user.username,
				"first_name": request.user.first_name,
                "last_name": request.user.last_name,
				"designation": request.user.designation,
				"qualification": request.user.qualification,
				"address": request.user.designation,
                "phone": request.user.phone,
                "profile_image": request.user.profile_image
				}
			)
    context['account_form'] = form
    return render(request, 'accounts/account_update.html', context)

class AccountList(generic.ListView):
    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'
    paginate_by=16
    def get_queryset(self):
        try:
            a = self.request.GET.get('account')
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(
                Q(username__icontains=a) |
                Q(email__icontains=a) |
                Q(first_name__icontains=a) |
                Q(last_name__icontains=a) |
                Q(address__icontains=a) |
                Q(qualification__icontains=a) |
                Q(phone__icontains=a) |
                Q(designation__icontains=a)               
            )
        else:
            account_list = Account.objects.filter(is_active=True)[2:]
        return account_list

