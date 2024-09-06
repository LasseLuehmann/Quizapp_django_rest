from . import views
from django.urls import path

app_name = 'session-urls'

urlpatterns = [
    path('list/all',views.listallsessions, name = 'listsession'),
    #path('fetch/<sessionid>',views.fetch_session, name = 'fetch_session'),
    
]
