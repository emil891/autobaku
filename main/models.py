from django.db import models

class Avtomobil(models.Model):
    VALYUTA_SEClMLERl = [
        ('AZN', 'AZN'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]

    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    il = models.PositiveIntegerField()
    
    qiymet = models.PositiveIntegerField()
    valyuta = models.CharField(max_length=3, choices=VALYUTA_SEClMLERl, default='AZN')
    
    muherrik = models.CharField(max_length=50) 
    yurush = models.PositiveIntegerField() 
    
    seher = models.CharField(max_length=100, default='Bakı')
    
    # Yeni əlavə olunan telefon sahəsi
    telefon = models.CharField(max_length=50, default='+994 50 000 00 00')
    
    # --- ƏLAVƏ OLUNAN SAHƏLƏR ---
    kredit = models.BooleanField(default=False)
    barter = models.BooleanField(default=False)
    yeni = models.BooleanField(default=False) # İşarələnibsə Yeni, yoxsa Sürülmüş deməkdir
    
    shekil = models.ImageField(upload_to='avtomobiller/', blank=True, null=True)
    
    is_vip = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    
    elave_tarix = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marka} {self.model} ({self.il})"