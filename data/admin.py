from django.contrib import admin
from data.models import MyModel,data

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'username', 'email', 'password', 'balance','requiset','condition')
    list_display_links = ('id', 'fullname')
    list_editable = ('username', 'email', 'password', 'balance','requiset','condition') 
    list_per_page = 20 

admin.site.register(MyModel, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'phone_number','subject','message')

admin.site.register(data, MessageAdmin)

