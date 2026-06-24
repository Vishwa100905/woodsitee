from django.contrib import admin
# Register your models here.
from .models import *
class RoleAdmin(admin.ModelAdmin):
    list_display = ["user_typename"]
admin.site.register(Role,RoleAdmin)

class User_detailAdmin(admin.ModelAdmin):
    list_display = ["User_name","dp","Gender","Email","Phone","Type","Status"]
admin.site.register(User_detail,User_detailAdmin)

class Furniture_categoryAdmin(admin.ModelAdmin):
    list_display = ["Name","furniture","Description","Category_added"]
admin.site.register(Furniture_category,Furniture_categoryAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ["Country_name"]
admin.site.register(Country,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ["Country_id","State_name"]
admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ["State_id","City_name"]
admin.site.register(City,CityAdmin)

class User_AddressAdmin(admin.ModelAdmin):
    list_display = ["User_id","Building_name","Street_name","City_name","Pincode"]
admin.site.register(User_Address,User_AddressAdmin)

class Feedback_detailsAdmin(admin.ModelAdmin):
    list_display = ["Title","Description","Feedback_by","Feedback_on"]
admin.site.register(Feedback_details,Feedback_detailsAdmin)

class Complain_detailsAdmin(admin.ModelAdmin):
    list_display = ["Complain_name", "Details","admin_photo","Complain_by","Complain_on"]
admin.site.register(Complain_details,Complain_detailsAdmin)

class Brand_tableAdmin(admin.ModelAdmin):
    list_display = ["Brand_name","Brand_description","brand_logo"]
admin.site.register(Brand_table,Brand_tableAdmin)

class New_furnitureAdmin(admin.ModelAdmin):
    list_display = ["New_Furniture_Name","New_Furniture_Brand_Name","New_Furniture_Description","New_Furniture_Price","new_furniture","New_Furniture_Type","New_Furniture_Available_Quantity"]
admin.site.register(New_furniture,New_furnitureAdmin)

class Old_furnitureAdmin(admin.ModelAdmin):
    list_display = ["Old_Furniture_Name","Old_Furniture_Brand_Name","Old_Furniture_Description","Old_Furniture_Price","old_furniture","Old_Furniture_Type","Old_Furniture_Available_Quantity"]
admin.site.register(Old_furniture,Old_furnitureAdmin)

class Rent_furnitureAdmin(admin.ModelAdmin):
    list_display = ["Rent_Furniture_Name","Rent_Furniture_Brand_Name","Rent_Furniture_Description","Rent_Furniture_Price","rent_furniture","Rent_Furniture_Type","Rent_Furniture_Available_Quantity"]
admin.site.register(Rent_furniture,Rent_furnitureAdmin)

class New_Furniture_BuyingAdmin(admin.ModelAdmin):
    list_display = ["New_Furniture_ID","UserID","New_Book_DateTime"]
admin.site.register(New_Furniture_Buying,New_Furniture_BuyingAdmin)

class Old_Furniture_BuyingAdmin(admin.ModelAdmin):
    list_display = ["Old_Furniture_ID","UserID","Old_Book_DateTime"]
admin.site.register(Old_Furniture_Buying,Old_Furniture_BuyingAdmin)

class Rent_Furniture_BuyingAdmin(admin.ModelAdmin):
    list_display = ["Rent_Furniture_ID","UserID","Rent_StartDate","Rent_EndDate","Rent_Book_DateTime"]
admin.site.register(Rent_Furniture_Buying,Rent_Furniture_BuyingAdmin)

