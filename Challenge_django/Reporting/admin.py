from django.contrib import admin
from .models import Categorie_Agent, Agent, Type_Activite, Activite, Fact_Prestation, Periodicite, Periodes_Reporting, Date
# Register your models here.
admin.site.register(Categorie_Agent)
admin.site.register(Agent)
admin.site.register(Type_Activite)
admin.site.register(Activite)
admin.site.register(Fact_Prestation)
admin.site.register(Periodicite)
admin.site.register(Periodes_Reporting)
admin.site.register(Date)