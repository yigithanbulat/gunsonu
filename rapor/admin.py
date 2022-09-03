from pdb import pm
from django.contrib import admin
from .models import Rapor
from django.utils.html import format_html

class RaporAdmin(admin.ModelAdmin):
    list_display = ('görüntüle','olusturan','rapor_olusturma_tarihi','image_tag')
    list_filter = ('rapor_olusturma_tarihi','olusturan')
    ordering = ('rapor_olusturma_tarihi',)
    list_per_page = 25
    date_hierarchy = 'rapor_olusturma_tarihi'
    # fields = ('olusturan','pm','kkm','mis','eis','ss','tt','et','ik','ek','tk','tpg')
    
    fieldsets = (
        ('Teknik Personel',{
            'fields':('proje_muduru','kalite_kontrol','mimari_isler','elektrik_isleri','saha_sorumlusu','tesisat_tek','elektrik_tek','insaat_kalfa','elektrik_kalfa','tesisat_kalfa','topograf'),
            'classes': ('collapse',),
        }),
        ('Personel',{
            'fields': ('kalipci','demirci','betoncu','sıvaci','fayansci','izolasyoncu','boyaci','marangoz','kaynakci','elektrikci','sıhhi_tesisatci'),
            'classes': ('collapse',)
        }),
        ('Makine ve Nakil Vasıtası',{
            'fields': ('kamyon','excavator','molopomp','bobcat','demirkesme','demirbukme','kompaktor','yuk_asansoru','kule_vinc','kepce','mikser'),
            'classes': ('collapse',)
        }),
        ('Yapılan İş',{
            'fields':('yapilan_is',),
            'classes': ('collapse',)
        }),
        ('Raporu Oluşturan',{
            'fields':('olusturan','yapilan_is_foto','image_tag'),
        }),

    )


    readonly_fields = ('image_tag',)
    # change_list_template = 'deneme.html'



admin.site.register(Rapor,RaporAdmin)

# Register your models here.
