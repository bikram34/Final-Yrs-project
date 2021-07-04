from django.contrib import admin
from .models import extendeduser
from .models import Patients_detail
from .models import doctor


# Register your models here.
admin.site.register(extendeduser)
admin.site.register(Patients_detail)
admin.site.register(doctor)
