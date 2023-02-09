from django.db import models


class ProductCategoryMaster(models.Model):
    product_cat_id = models.AutoField(primary_key=True)
    product_type = models.CharField("Product Type",max_length=20, choices=(
        ('Consumable', 'Consumable'), ('Non-Consumable', 'Non-Consumable')))
    product_cat_name = models.CharField("Product Category Name :",max_length=250)

    def __str__(self):
        return self.product_cat_name

class ProductDetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_cat_id = models.ForeignKey(
        ProductCategoryMaster, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_model = models.CharField(max_length=250)
    product_serialno = models.CharField(max_length=250)
    entry_date = models.DateField(auto_now_add=True)
    initial_quantity = models.IntegerField()
    current_quantity = models.IntegerField(editable = False)
    cartridge_toner = models.CharField(max_length=250)
    remarks = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        self.current_quantity = self.initial_quantity
        super(ProductDetails, self).save(*args, **kwargs)

class UserDesignationMaster(models.Model):
    usr_des_id = models.AutoField(primary_key=True)
    usr_des_name = models.CharField(max_length=250)
    usr_des_type = models.CharField(max_length=10, choices=(
        ('Judge', 'Judge'), ('Staff', 'Staff')))

    def __str__(self):
        return self.usr_des_name


class BuildingMaster(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.building_name


class SectionDetails(models.Model):
    section_id = models.AutoField(primary_key=True)
    building_name = models.ForeignKey(BuildingMaster, on_delete=models.CASCADE)
    section_type = models.CharField(max_length=10, choices=(
        ('Court', 'Court'), ('Section', 'Section')))
    section_name = models.CharField(max_length=250)
    def __str__(self):
        return self.section_name
    

class LocationDetails(models.Model):
    location_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(SectionDetails, on_delete=models.CASCADE)
    floor = models.CharField(max_length=250)
    roomno = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    deleted = models.BooleanField(default=False)

    # def __str__(self):
    #     return str(self.floor+self.roomno)
    #     # return str(self.location_id)

    
    
class UserDetails(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_des_id = models.ForeignKey(
        UserDesignationMaster, on_delete=models.CASCADE)
    usr_name = models.CharField(max_length=250)
    usr_mobile = models.CharField(max_length=250)
    entry_date = models.DateField(auto_now_add=True)
    location_id = models.ForeignKey(LocationDetails, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    

class TransactionDetails(models.Model):
    trans_id = models.AutoField(primary_key=True)
    product_id  = models.ForeignKey(
        ProductDetails, on_delete=models.CASCADE) 
    usr_id =  models.ForeignKey(
        UserDetails, on_delete=models.CASCADE)
    location_id = models.ForeignKey(
        LocationDetails, on_delete=models.CASCADE)
    trans_tpye = models.CharField(max_length=50, choices=(
        ('Issued', 'Issued'),('AtComputerSection', 'At Computer Section')))
    trans_date = models.DateField()
    remarks = models.CharField(max_length=250)


class HealthStatusDetails(models.Model):
    health_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    product_healthy = models.CharField(max_length=10, choices=(
        ('Yes', 'Yes'), ('No', 'No')))
    health_remarks = models.CharField(max_length=250)
    product_status = models.CharField(max_length=50, choices=(
        ('Working', 'Working'), ('Not Working', 'Not Working')))
    status_date = models.DateField(auto_now_add=True)

