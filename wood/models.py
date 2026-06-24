# Create your models here.
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
User_type = [("user","User"),
             ("buyer","Buyer"),
             ("seller","Seller"),
             ("rent","Rent")]

gender = [("male","Male"),
          ("female","Female")]

status = [("active","Active"),
          ("inactive","Inactive")]
Furniture_Quantity = [("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20")]

class Role(models.Model):
    user_typename = models.CharField(max_length=30,choices=User_type)

    def __str__(self):
        return self.user_typename

class User_detail(models.Model):
    User_name = models.CharField(max_length=30)
    Dp = models.ImageField(upload_to="photos")
    Gender = models.CharField(max_length=30,choices=gender)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    Type = models.ForeignKey(Role,on_delete=models.CASCADE)
    Status = models.CharField(max_length=10,choices=status)

    def __str__(self):
        return self.User_name

    def dp(self):
      return mark_safe('<img src="{}" width="100"/>'.format(self.Dp.url))

class Furniture_category(models.Model):
    Name = models.CharField(max_length=30)
    Pictures = models.ImageField(upload_to="photos")
    Description = models.TextField()
    Category_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

    def furniture(self):
      return mark_safe('<img src="{}" width="100"/>'.format(self.Pictures.url))

class Country(models.Model):
    Country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.Country_name

class State(models.Model):
    Country_id = models.ForeignKey(Country,on_delete=models.CASCADE)
    State_name = models.CharField(max_length=30)

    def __str__(self):
        return self.State_name

class City(models.Model):
    State_id = models.ForeignKey(State,on_delete=models.CASCADE)
    City_name = models.CharField(max_length=30)

    def __str__(self):
        return self.City_name

class User_Address(models.Model):
    User_id = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    Building_name = models.CharField(max_length=40)
    Street_name = models.CharField(max_length=40)
    City_name = models.ForeignKey(City,on_delete=models.CASCADE)
    Pincode = models.IntegerField()

class Feedback_details(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Feedback_by = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    Feedback_on = models.DateTimeField(auto_now=True)

class Complain_details(models.Model):
    Complain_name = models.CharField(max_length=50)
    Details = models.TextField()
    Photo = models.ImageField(upload_to="photos")
    Complain_by = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    Complain_on = models.DateTimeField(auto_now=True)

    def admin_photo(self):
      return mark_safe('<img src="{}" width="100"/>'.format(self.Photo.url))

class Brand_table(models.Model):
    Brand_name = models.CharField(max_length=50)
    Brand_description = models.TextField()
    Brand_logo = models.ImageField(upload_to="photos")

    def brand_logo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Brand_logo.url))

    def __str__(self):
        return self.Brand_name

class New_furniture(models.Model):
    New_Furniture_Name = models.CharField(max_length=50)
    New_Furniture_Brand_Name = models.ForeignKey(Brand_table,on_delete=models.CASCADE)
    New_Furniture_Description = models.TextField()
    New_Furniture_Price = models.FloatField()
    New_Furniture_Image = models.ImageField(upload_to="photos")
    New_Furniture_Type = models.ForeignKey(Furniture_category,on_delete=models.CASCADE)
    New_Furniture_Available_Quantity = models.CharField(max_length=10,choices=Furniture_Quantity)

    def new_furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.New_Furniture_Image.url))

    def __str__(self):
        return self.New_Furniture_Name

class Old_furniture(models.Model):
    Old_Furniture_Name = models.CharField(max_length=50)
    Old_Furniture_Brand_Name = models.ForeignKey(Brand_table,on_delete=models.CASCADE)
    Old_Furniture_Description = models.TextField()
    Old_Furniture_Price = models.FloatField()
    Old_Furniture_Image = models.ImageField(upload_to="photos")
    Old_Furniture_Type = models.ForeignKey(Furniture_category, on_delete=models.CASCADE)
    Old_Furniture_Available_Quantity = models.CharField(max_length=10, choices=Furniture_Quantity)

    def old_furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Old_Furniture_Image.url))

    def __str__(self):
        return self.Old_Furniture_Name

class Rent_furniture(models.Model):
    Rent_Furniture_Name = models.CharField(max_length=50)
    Rent_Furniture_Brand_Name = models.ForeignKey(Brand_table, on_delete=models.CASCADE)
    Rent_Furniture_Description = models.TextField()
    Rent_Furniture_Price = models.FloatField()
    Rent_Furniture_Image = models.ImageField(upload_to="photos")
    Rent_Furniture_Type = models.ForeignKey(Furniture_category, on_delete=models.CASCADE)
    Rent_Furniture_Available_Quantity = models.CharField(max_length=10, choices=Furniture_Quantity)

    def rent_furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Rent_Furniture_Image.url))

    def __str__(self):
        return self.Rent_Furniture_Name

class New_Furniture_Buying(models.Model):
    New_Furniture_ID = models.ForeignKey(New_furniture,on_delete=models.CASCADE)
    UserID = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    New_Book_DateTime = models.DateTimeField()

class Old_Furniture_Buying(models.Model):
        Old_Furniture_ID = models.ForeignKey(Old_furniture, on_delete=models.CASCADE)
        UserID = models.ForeignKey(User_detail, on_delete=models.CASCADE)
        Old_Book_DateTime = models.DateTimeField()

class Rent_Furniture_Buying(models.Model):
    Rent_Furniture_ID = models.ForeignKey(Rent_furniture,on_delete=models.CASCADE)
    UserID = models.ForeignKey(User_detail,on_delete=models.CASCADE)
    Rent_StartDate = models.DateField()
    Rent_EndDate = models.DateField()
    Rent_Book_DateTime = models.DateTimeField()
