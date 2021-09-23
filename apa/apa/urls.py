
from django.contrib import admin
from django.conf.urls import handler404, handler500
import home
admin.site.site_header = "Ayurveda Proctology Admin"
admin.site.site_title = "Ayurveda Proctology Admin Portal"
admin.site.index_title = "Ayurveda Proctology Portal"

from django.urls import path, include
from home.views import views
from django.conf import settings
from accounts.views import registration_view, logout_view, login_view, account_view, AccountList, registrationConfirm_view, profile_view
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts.views import AccountList

app_name = 'apa'

urlpatterns = [
    path('admin-apa-2017/', admin.site.urls),
    path('', include('home.urls')),
    path('membership/', include('member.urls')),
    path('events/', include('events.urls')),
 #   path('subscribe/', include('subscribe.urls')),
  #  path('register/', registration_view, name = "register"),
   # path('register/confirm', registrationConfirm_view, name = "register_confirm"),
    path('logout/', logout_view, name = "logout"),
    path('login/', login_view, name = "login"),
    path('account/update/', account_view, name='account_update'),
    path('account/details', profile_view, name='account_details'),
    path('apa-members/', AccountList.as_view(), name='account_list'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
     name='password_reset_complete'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
handler404 = home.views.error_404
handler500 = home.views.error_500