from django.contrib import admin
from .models import Category,Product,CPU,GPU,RAM,SSD,Characteristics


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ["name", "slug", "description", 
                    "price", "variable","created",
                    "updated", "discount"]  
    list_filter = ["variable", "created", "category", "characteristics", "updated"] 
    list_editable = ["price", "discount"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Characteristics)
class Characteristics_admin(admin.ModelAdmin):
    list_display = [ "hz", "resolution", "weight", "cpu", "ram", "ssd", "gpu"]    


@admin.register(CPU)
class CPU_admin(admin.ModelAdmin):
    list_display = ["cpu_name", "cpu_core", 
                    "cpu_video_core", "cpu_frequency",
                    "streams"]




@admin.register(GPU)
class GPU_admin(admin.ModelAdmin):
    list_display = ["gpu_name", "gpu_core", 
                    "gpu_memory", "gpu_frequency"]



@admin.register(RAM)
class RAM_admin(admin.ModelAdmin):
    list_display = ["ram_name", "ram_size", "ram_frequency"]


@admin.register(SSD)
class SSD_admin(admin.ModelAdmin):
    list_display = ["ssd_name", "ssd_size", "ssd_speed"] 








  
