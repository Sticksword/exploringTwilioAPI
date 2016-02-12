"""phoneBuzzLendUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

import phoneBuzzLendUp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # making calls
    url(r'^call_someone/$', phoneBuzzLendUp.views.call_someone),
    url(r'^make_previous_call/$', phoneBuzzLendUp.views.make_previous_call),

    # SMS response endpoint (did for funsies)
    url(r'^sms/$', phoneBuzzLendUp.views.sms),

    # call response endpoint
    url(r'^ring/$', phoneBuzzLendUp.views.ring),

    # handling call response endpoint
    url(r'^response/$', phoneBuzzLendUp.views.handle_response_message),

    # replay response endpoint
    url(r'^replay/?$', phoneBuzzLendUp.views.handle_replay_message),

    # get past call history
    url(r'^get_previous_calls/', phoneBuzzLendUp.views.get_previous_calls),

]
