from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Degerlendirme(models.Model):
    acilis_karsilama = models.IntegerField(verbose_name="Açılış ve Karşılama", default=0, validators=[])
    etkin_dinleme_anlama = models.IntegerField(verbose_name="Etkin Dinleme ve Anlama", default=0, validators=[])
    analiz_etkin_soru = models.IntegerField(verbose_name="Analiz ve Etkin Soru Sorma", default=0, validators=[])
    gorusme_kirliligi = models.IntegerField(verbose_name="Görüşme Kirliliği Yaratacak Söylem ve Sesler", default=0, validators=[])
    ses_tonu = models.IntegerField(verbose_name="Kendinden Emin, Canlı ve Nezaketli Ses Tonu", default=0, validators=[])
    sorun_sahiplenme = models.IntegerField(verbose_name="Abonenin Sorununun Sahiplenilmesi", default=0, validators=[])
    empati = models.IntegerField(verbose_name="Empati", default=0, validators=[])
    sure_stres_yonetimi = models.IntegerField(verbose_name="Süre ve Stres Yönetimi", default=0, validators=[])
    dogru_yonlendirme = models.IntegerField(verbose_name="Doğru Yönlendirme", default=0, validators=[])
    bilgi_paylasimi = models.IntegerField(verbose_name="Bilgiyi Anlaşılır Biçimde Paylaşma, İkna Etme", default=0, validators=[])
    uygun_kapanis = models.IntegerField(verbose_name="Uygun Kapanış Anonsu Verildi mi?", default=0, validators=[])
    bilgi_verme = models.IntegerField(verbose_name="İlgili/Yönlendirilen Ekiple İlgili Bilgi Verildi mi?", default=0, validators=[])

    hata1 = models.BooleanField(default=False, verbose_name="Sürece uygun olmayan şekilde çağrıyı sonlandırdı")
    hata2 = models.BooleanField(default=False, verbose_name="Kayıt almadı, hatalı kayıt aldı")
    hata3 = models.BooleanField(default=False, verbose_name="Azarlama, kaba ve ukala konuşma, bağırma")
    hata4 = models.BooleanField(default=False, verbose_name="İrtibat numarası almama/ güncellememe")
    hata5 = models.BooleanField(default=False, verbose_name="Müşteri kapattı ancak MT hattı açık bıraktı")
    hata6 = models.BooleanField(default=False, verbose_name="KVKK Uyum")
    hata7 = models.BooleanField(default=False, verbose_name="İlgisiz ve duyarsız davranış")
    hata8 = models.BooleanField(default=False, verbose_name="Söz kesme, aynı anda konuşma")
    hata9 = models.BooleanField(default=False, verbose_name="Çağrıyı geç ya da uygunsuz karşılama")
    hata10 = models.BooleanField(default=False, verbose_name="Görüşme esnasında farklı bir ekranla, içerikle ilgilenme")
    hata11 = models.BooleanField(default=False, verbose_name="Yemek, sakız vb. nedenlerle çağrıya yanşayan sesler")
    hata12 = models.BooleanField(default=False, verbose_name="Kendi kişisel bilgilerini müşteri ile paylaşma")
    hata13 = models.BooleanField(default=False, verbose_name="Şirket prosedür ve mevzuata aykırı bilgi paylaşma")

    musteri_temsilcisi = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='degerlendirmeler',
        verbose_name="Müşteri Temsilcisi")

    def get_musteri_temsilcisi_full_name(self):
        return f"{self.musteri_temsilcisi.first_name} {self.musteri_temsilcisi.last_name}"


    def __str__(self):
        # Döndürmek istediğiniz string ifade
        return f"{self.get_musteri_temsilcisi_full_name()} - Değerlendirme"


    cagri_kuyrugu = models.CharField(max_length=255, verbose_name="Çağrı Kuyruğu") #kuyruk id mi almalıyım?
    telefon_numarasi = models.CharField(max_length=10, verbose_name="Telefon Numarası",
                                        validators=[])  # Include appropriate validators
    cagri_tarihi = models.DateField(verbose_name="Çağrı Tarihi")

    # Comments and file upload
    aciklamalar = models.TextField(verbose_name="Açıklamalar", blank=True)
    cagri_dosyasi = models.FileField(upload_to='uploads/', verbose_name="Çağrı Dosyası", blank=True, null=True)

    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return f"{self.musteri_temsilcisi} - {self.cagri_tarihi.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Değerlendirme"
        verbose_name_plural = "Değerlendirmeler"


    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Zamanı")

    def __str__(self):
        return f"{self.created_at.strftime('%Y-%m-%d %H:%M')} - Değerlendirme"

    class Meta:
        verbose_name = "Değerlendirme"
        verbose_name_plural = "Değerlendirmeler"


class Kuyruk(models.Model):
    GIRIS_ABONE_TANINMADI = models.DateTimeField(auto_now_add=True, verbose_name="7000 GIRIS ABONE TANINMADI")
    ABONE_SURECLERI = models.DateTimeField(auto_now_add=True, verbose_name="7001 ABONE SÜREÇLERİ")
    GAZ_KESME = models.DateTimeField(auto_now_add=True, verbose_name="7002 GAZ KESME")
    BORC_ODEME_YERI_SORGU = models.DateTimeField(auto_now_add=True, verbose_name="7003 BORÇ/ÖDEME YERİ SORGU")
    ENDEKS = models.DateTimeField(auto_now_add=True, verbose_name="7004 ENDEKS")
    IC_TESISAT = models.DateTimeField(auto_now_add=True, verbose_name="7004 ENDEKS")
    SOZLESME_SONLANDIRMA = models.DateTimeField(auto_now_add=True, verbose_name="7006 SÖZLEŞME SONLANDIRMA")
    DOGALGAZ_TALEP_SIKAYET = models.DateTimeField(auto_now_add=True, verbose_name="7007 DOĞALGAZ TALEP/ŞİKAYET")
    ABONE_MERKEZLERI = models.DateTimeField(auto_now_add=True, verbose_name="7008 ABONE MERKEZLERİ")
    YAS_ENGELLI = models.DateTimeField(auto_now_add=True, verbose_name="7010 65YAS/ENGELLI")
    BORC_HATIRLATMA = models.DateTimeField(auto_now_add=True, verbose_name="7020 BORC HATIRLATMA")
    ACIL_187 = models.DateTimeField(auto_now_add=True, verbose_name="79187 187")
    ESGAZ = models.DateTimeField(auto_now_add=True, verbose_name="7926 ESGAZ")
    SANTRAL_GELEN = models.DateTimeField(auto_now_add=True, verbose_name="7997 449 SANTRAL GELEN")
    GELEN_KUYRUGU = models.DateTimeField(auto_now_add=True, verbose_name="7998 477 GELEN KUYRUĞU")
