from django.urls import path
from .views import presence as p, controller as c, main

app_name = 'dash'

''' this url patterns for main purpose '''
urlpatterns = [
    path('', main.redirection, name='main'),
    path('register', main.account_register, name='manual'),
    path('agency/create', main.create_agency_view, name='agency'),
    # path('agency/create', main.CreateAgency.as_view(), name='agency'),
    path('invitation/<slug:link>', main.register_by_invitation, name='invitation'),
    path('landed', main.LandingPage.as_view(), name='landing'),
]

''' this url patterns for presence only '''
urlpatterns += [
    path('<link>/user/scan', p.scan, name='user-scan'),
    path('<link>/user/history/<qr>', p.HistoryDetailView.as_view(), name='user-history'),
    path('<link>/user', p.UserPresenceLanding.as_view(), name='user-dashboard'),
]

''' this url patterns for controller only '''
urlpatterns += [
    path('<link>/registering-employee', c.registering_user, name='registering-user'),
    path('<link>/generate-presence-qr', c.CreateQRCode.as_view(), name='create-qr'),
    path('<link>/generate-invitation', c.CreateInvitationLink.as_view(), name='create-link'),
    path('<link>', c.DashboardView.as_view(), name='agency-dashboard'),
]

