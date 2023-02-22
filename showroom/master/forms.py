from django import forms
from master.models import Vehicle, Accessories


class Vehicleform(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['Vehicle_Name', 'Vehicle_Type', 'Description', 'Vehicle_Color', 'Rate', 'Weight', 'Capacity',
                  'Mileage', 'Fuel', 'Vehicle_Model', 'Year_of_built', 'Autogear', 'Seatcap', 'Center_lock',
                  'Power_steering', 'Power_break', 'Tyre', 'Chassis', 'Vehicle_Image']


class Accessoriesform(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['Accessory_Name', 'Vehicle_Name', 'Description', 'Rate', 'Accessory_Image']
