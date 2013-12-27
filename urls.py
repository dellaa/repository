urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
#     url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^accounts/login/$', login),
    url(r'^accounts/auth/$', auth_view),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/loggedin/$', loggedin),
    url(r'^accounts/invalid/$', invalid_login), 
)
