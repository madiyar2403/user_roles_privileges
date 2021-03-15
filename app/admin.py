from django.contrib import admin
from .models import Person, Role, Privilege, Example, Data

admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Privilege)
admin.site.register(Example)
admin.site.register(Data)
