# Generated by Django 5.0.1 on 2024-02-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degerlendirme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acilis_karsilama', models.IntegerField(default=0, verbose_name='Açılış ve Karşılama')),
                ('etkin_dinleme_anlama', models.IntegerField(default=0, verbose_name='Etkin Dinleme ve Anlama')),
                ('analiz_etkin_soru', models.IntegerField(default=0, verbose_name='Analiz ve Etkin Soru Sorma')),
                ('gorusme_kirliligi', models.IntegerField(default=0, verbose_name='Görüşme Kirliliği Yaratacak Söylem ve Sesler')),
                ('ses_tonu', models.IntegerField(default=0, verbose_name='Kendinden Emin, Canlı ve Nezaketli Ses Tonu')),
                ('sorun_sahiplenme', models.IntegerField(default=0, verbose_name='Abonenin Sorununun Sahiplenilmesi')),
                ('empati', models.IntegerField(default=0, verbose_name='Empati')),
                ('sure_stres_yonetimi', models.IntegerField(default=0, verbose_name='Süre ve Stres Yönetimi')),
                ('dogru_yonlendirme', models.IntegerField(default=0, verbose_name='Doğru Yönlendirme')),
                ('bilgi_paylasimi', models.IntegerField(default=0, verbose_name='Bilgiyi Anlaşılır Biçimde Paylaşma, İkna Etme')),
                ('uygun_kapanis', models.IntegerField(default=0, verbose_name='Uygun Kapanış Anonsu Verildi mi?')),
                ('bilgi_verme', models.IntegerField(default=0, verbose_name='İlgili/Yönlendirilen Ekiple İlgili Bilgi Verildi mi?')),
                ('hata1', models.BooleanField(default=False, verbose_name='Sürece uygun olmayan şekilde çağrıyı sonlandırdı')),
                ('hata2', models.BooleanField(default=False, verbose_name='Kayıt almadı, hatalı kayıt aldı')),
                ('hata3', models.BooleanField(default=False, verbose_name='Azarlama, kaba ve ukala konuşma, bağırma')),
                ('hata4', models.BooleanField(default=False, verbose_name='İrtibat numarası almama/ güncellememe')),
                ('hata5', models.BooleanField(default=False, verbose_name='Müşteri kapattı ancak MT hattı açık bıraktı')),
                ('hata6', models.BooleanField(default=False, verbose_name='KVKK Uyum')),
                ('hata7', models.BooleanField(default=False, verbose_name='İlgisiz ve duyarsız davranış')),
                ('hata8', models.BooleanField(default=False, verbose_name='Söz kesme, aynı anda konuşma')),
                ('hata9', models.BooleanField(default=False, verbose_name='Çağrıyı geç ya da uygunsuz karşılama')),
                ('hata10', models.BooleanField(default=False, verbose_name='Görüşme esnasında farklı bir ekranla, içerikle ilgilenme')),
                ('hata11', models.BooleanField(default=False, verbose_name='Yemek, sakız vb. nedenlerle çağrıya yanşayan sesler')),
                ('hata12', models.BooleanField(default=False, verbose_name='Kendi kişisel bilgilerini müşteri ile paylaşma')),
                ('hata13', models.BooleanField(default=False, verbose_name='Şirket prosedür ve mevzuata aykırı bilgi paylaşma')),
                ('musteri_temsilcisi', models.CharField(max_length=255, verbose_name='Müşteri Temsilcisi')),
                ('cagri_kuyrugu', models.CharField(max_length=255, verbose_name='Çağrı Kuyruğu')),
                ('telefon_numarasi', models.CharField(max_length=10, verbose_name='Telefon Numarası')),
                ('cagri_tarihi', models.DateField(verbose_name='Çağrı Tarihi')),
                ('aciklamalar', models.TextField(blank=True, verbose_name='Açıklamalar')),
                ('cagri_dosyasi', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Çağrı Dosyası')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Zamanı')),
            ],
            options={
                'verbose_name': 'Değerlendirme',
                'verbose_name_plural': 'Değerlendirmeler',
            },
        ),
        migrations.CreateModel(
            name='Kuyruk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GIRIS_ABONE_TANINMADI', models.DateTimeField(auto_now_add=True, verbose_name='7000 GIRIS ABONE TANINMADI')),
                ('ABONE_SURECLERI', models.DateTimeField(auto_now_add=True, verbose_name='7001 ABONE SÜREÇLERİ')),
                ('GAZ_KESME', models.DateTimeField(auto_now_add=True, verbose_name='7002 GAZ KESME')),
                ('BORC_ODEME_YERI_SORGU', models.DateTimeField(auto_now_add=True, verbose_name='7003 BORÇ/ÖDEME YERİ SORGU')),
                ('ENDEKS', models.DateTimeField(auto_now_add=True, verbose_name='7004 ENDEKS')),
                ('IC_TESISAT', models.DateTimeField(auto_now_add=True, verbose_name='7004 ENDEKS')),
                ('SOZLESME_SONLANDIRMA', models.DateTimeField(auto_now_add=True, verbose_name='7006 SÖZLEŞME SONLANDIRMA')),
                ('DOGALGAZ_TALEP_SIKAYET', models.DateTimeField(auto_now_add=True, verbose_name='7007 DOĞALGAZ TALEP/ŞİKAYET')),
                ('ABONE_MERKEZLERI', models.DateTimeField(auto_now_add=True, verbose_name='7008 ABONE MERKEZLERİ')),
                ('YAS_ENGELLI', models.DateTimeField(auto_now_add=True, verbose_name='7010 65YAS/ENGELLI')),
                ('BORC_HATIRLATMA', models.DateTimeField(auto_now_add=True, verbose_name='7020 BORC HATIRLATMA')),
                ('ACIL_187', models.DateTimeField(auto_now_add=True, verbose_name='79187 187')),
                ('ESGAZ', models.DateTimeField(auto_now_add=True, verbose_name='7926 ESGAZ')),
                ('SANTRAL_GELEN', models.DateTimeField(auto_now_add=True, verbose_name='7997 449 SANTRAL GELEN')),
                ('GELEN_KUYRUGU', models.DateTimeField(auto_now_add=True, verbose_name='7998 477 GELEN KUYRUĞU')),
            ],
        ),
    ]