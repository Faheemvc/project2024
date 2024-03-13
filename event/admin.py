from django.contrib import admin
from .models import staff,student,EventDetails,studentDischargeDetails
# Register your models here.



class staffAdmin(admin.ModelAdmin):
    pass
admin.site.register(staff, staffAdmin)

class studentAdmin(admin.ModelAdmin):
    pass
admin.site.register(student, studentAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(EventDetails, AppointmentAdmin)

class studentDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(studentDischargeDetails, studentDischargeDetailsAdmin)




