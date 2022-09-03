from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe




class Rapor(models.Model):
    readonly_fields =['image_tag']
    kac =((0,'0'),
        (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11'),(12,'12'),(13,'13'),(14,'14'),(15,'15'),
        (16,'16'),(17,'17'),(18,'18'),(19,'19'),(20,'20'),(21,'21'),(22,'22'),(23,'23'),(24,'24'),(25,'25'),(26,'26'),(27,'27'),(28,'28'),(29,'29'),(30,'30')
    )
    görüntüle = models.CharField(max_length=5,default="Raporu Görüntüle")
    #TEKNİK PERSONEL
    proje_muduru = models.IntegerField(default=0, choices=kac, verbose_name="Proje Müdürü")
    kalite_kontrol = models.IntegerField(default=0, choices=kac, verbose_name="Kalite Kontrol Müdürü")
    mimari_isler = models.IntegerField(default=0, choices=kac, verbose_name="Mimari İşler Sorumlusu")
    elektrik_isleri = models.IntegerField(default=0, choices=kac, verbose_name="Elektrik İşleri Sorumlusu")
    saha_sorumlusu = models.IntegerField(default=0, choices=kac, verbose_name="Saha Sorumlusu")
    tesisat_tek = models.IntegerField(default=0, choices=kac, verbose_name="Tesisat Teknikeri")
    elektrik_tek = models.IntegerField(default=0, choices=kac, verbose_name="Elektrik Teknikeri")
    insaat_kalfa = models.IntegerField(default=0, choices=kac, verbose_name="İnşaat Kalfası")
    elektrik_kalfa = models.IntegerField(default=0, choices=kac, verbose_name="Elektrik Kalfaası")
    tesisat_kalfa = models.IntegerField(default=0, choices=kac, verbose_name="Tesisat Kalfası")
    topograf = models.IntegerField(default=0, choices=kac, verbose_name="Topograf")
    #PERSONEL
    kalipci = models.IntegerField(default=0, choices=kac, verbose_name="Kalıpçı")
    demirci = models.IntegerField(default=0, choices=kac, verbose_name="Demirci")
    betoncu = models.IntegerField(default=0, choices=kac, verbose_name="Betoncu")
    sıvaci = models.IntegerField(default=0, choices=kac, verbose_name="Sıvacı")
    fayansci = models.IntegerField(default=0, choices=kac, verbose_name="Fayanscı")
    izolasyoncu = models.IntegerField(default=0, choices=kac, verbose_name="İzolasyoncu")
    boyaci = models.IntegerField(default=0, choices=kac, verbose_name="Boyacı")
    marangoz = models.IntegerField(default=0, choices=kac, verbose_name="Marangoz")
    kaynakci = models.IntegerField(default=0, choices=kac, verbose_name="Kaynakçı")
    elektrikci = models.IntegerField(default=0, choices=kac, verbose_name="Elektrikçi")
    sıhhi_tesisatci = models.IntegerField(default=0, choices=kac, verbose_name="Sıhhi Tesisatçı")
    #MAKİNE VE NAKİL VASITASI
    kamyon = models.IntegerField(default=0, choices=kac, verbose_name="Kamyon")
    excavator = models.IntegerField(default=0, choices=kac, verbose_name="Excavator")
    molopomp = models.IntegerField(default=0, choices=kac, verbose_name="Molopomp")
    bobcat = models.IntegerField(default=0, choices=kac, verbose_name="Bobcat")
    demirkesme = models.IntegerField(default=0, choices=kac, verbose_name="Demir Kesme Makinesi")
    demirbukme = models.IntegerField(default=0, choices=kac, verbose_name="Demir Bükme Makinesi")
    kompaktor = models.IntegerField(default=0, choices=kac, verbose_name="Kompaktor")
    yuk_asansoru = models.IntegerField(default=0, choices=kac, verbose_name="Yük Asansörü")
    kule_vinc = models.IntegerField(default=0, choices=kac, verbose_name="Kule Vinç")
    kepce = models.IntegerField(default=0, choices=kac, verbose_name="Kepçe")
    mikser = models.IntegerField(default=0, choices=kac, verbose_name="Mikser")
    #YAPILAN İŞ
    yapilan_is = models.TextField(verbose_name="Yapılan İş")
    yapilan_is_foto = models.ImageField(upload_to='img',null=True,blank=True)

    def image_tag(self):
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.yapilan_is_foto))

    image_tag.short_description = 'Yapılan İş 1'
    
    
    olusturan = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Raporu Oluşturan")
    rapor_olusturma_tarihi = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Rapor"
        verbose_name_plural = "Raporlar"
    def __str__(self):
        return str(self.olusturan)+"'ın "+str(self.rapor_olusturma_tarihi.day)+"."+str(self.rapor_olusturma_tarihi.month)+"."+str(self.rapor_olusturma_tarihi.year)+" tarihli raporu"