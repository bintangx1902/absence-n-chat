from django.contrib.admin import site
from .models import *

site.register(UserExtended)
site.register(AgencyName)
site.register(QRCodeGenerator)
site.register(InvitationLink)
