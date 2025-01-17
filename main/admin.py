from django.contrib import admin
from .models import Category,Product,CPU,GPU,RAM,SSD,characteristics,Image


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ["name", "category", "description", 
                    "price", "variable","created",
                    "updated", "discount"]   
    list_editable = ["price", "discount"]


@admin.register(characteristics)
class characteristics_admin(admin.ModelAdmin):
    list_display = ["settings", "hz", "resolution", "weight", "cpu", "ram", "ssd", "gpu"]    


@admin.register(CPU)
class CPUadmin(admin.ModelAdmin):
    list_display = ["cpu_name", "cpu_core", 
                    "cpu_video_core", "cpu_frequency",
                    "streams"]




@admin.register(GPU)
class GPUadmin(admin.ModelAdmin):
    list_display = ["gpu_name", "gpu_core", 
                    "gpu_memory", "gpu_frequency"]



@admin.register(RAM)
class RAMadmin(admin.ModelAdmin):
    list_display = ["ram_name", "ram_size", "ram_frequency"]


@admin.register(SSD)
class SSDadmin(admin.ModelAdmin):
    list_display = ["ssd_name", "ssd_size", "ssd_speed"] 








  
