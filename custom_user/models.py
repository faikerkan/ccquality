from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

telefon_numarasi_validator = RegexValidator(regex=r'^\d{10}$', message="Telefon numarası başında sıfır olmadan 10 haneli olmalıdır.")

class CustomUser(AbstractUser):
    SICIL_NO_MAX_LENGTH = 10
    SKILL_CHOICES = [
        ('187 Acil', '187 Acil'),
        ('Müşteri Hizmetleri', 'Müşteri Hizmetleri'),
        ('Santral', 'Santral'),
    ]

    sicil_no = models.CharField(max_length=SICIL_NO_MAX_LENGTH, null=True, blank=True)
    skill = models.CharField(max_length=20, choices=SKILL_CHOICES, null=True, blank=True)



class Degerlendirme(models.Model):
    # Değerlendirme maddeleri
    acilis_karsilama = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    etkin_dinleme_anlama = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)], null=True, blank=True)
    analiz_etkin_soru = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)], null=True, blank=True)
    gorusme_kirliligi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    ses_tonu = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    sorun_sahiplenme = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    empati = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    sure_stres_yonetimi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    dogru_yonlendirme = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    bilgi_paylasimi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    uygun_kapanis = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    ilgili_yonlendirilen_ekip_bilgi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

    # Hatalar
    hatali_sonlandirma = models.BooleanField(default=False)
    kayit_alma_hatasi = models.BooleanField(default=False)
    kaba_davranis = models.BooleanField(default=False)
    irtibat_numarasi_alma_hatasi = models.BooleanField(default=False)
    mt_hatti_acik_birakma = models.BooleanField(default=False)
    kvkk_uyumu = models.BooleanField(default=False)
    ilgisiz_davranis = models.BooleanField(default=False)
    soz_kesme = models.BooleanField(default=False)
    uygunsuz_karsilama = models.BooleanField(default=False)
    farkli_icerikle_ilgilenme = models.BooleanField(default=False)
    yansayan_sesler = models.BooleanField(default=False)
    kisisel_bilgileri_paylasma = models.BooleanField(default=False)
    prosedur_mevzuata_aykiri_bilgi = models.BooleanField(default=False)

    # Çağrı Detay Bilgileri
    temsilci = models.CharField(max_length=100)
    cagri_kuyrugu = models.CharField(max_length=100)
    telefon_numarasi = models.CharField(max_length=10, validators=[telefon_numarasi_validator], null=True, blank=True)
    cagri_tarihi = models.DateField()

    # Açıklamalar
    aciklamalar = models.TextField()

    # Ek dosya yükleme (opsiyonel)
    ek_dosya = models.FileField(upload_to='degerlendirmeler/', blank=True, null=True)

    def __str__(self):
        return f"Degerlendirme {self.id} - {self.temsilci} - {self.cagri_tarihi}"

    def calculate_score(self):
        # Başlangıç puanınız, örneğin her çağrının maksimum puanı
        score = 100

        # Her bir hata için puan düşürme
        if self.hatali_sonlandirma:
            score = 0
        if self.kayit_alma_hatasi:
            score = 0
        if self.kaba_davranis:
            score = 0
        if self.kvkk_uyumu:
            score = 0
        if self.mt_hatti_acik_birakma:
            score = 0
        # Diğer hatalar için benzer koşullar...

        # %50 düşürme etkisi olan hatalar
        if self.ilgisiz_davranis or self.soz_kesme or self.uygunsuz_karsilama or self.farkli_icerikle_ilgilenme or self.yansayan_sesler or self.kisisel_bilgileri_paylasma or self.prosedur_mevzuata_aykiri_bilgi:
            score *= 0.5

        return score