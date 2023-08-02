from datetime import datetime

def tarih_kontrol(tarih_str):
    try:
        datetime.strptime(tarih_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def arac_servis_zamani_hesapla(gun, ay, yil):
    tarih_str = f"{gun}/{ay}/{yil}"
    
    if not tarih_kontrol(tarih_str):
        return "Hatalı tarih girişi! Lütfen geçerli bir tarih giriniz. (Gün/Ay/Yıl)"
    
    trafiğe_cikis_tarihi = datetime(yil, ay, gun)
    su_an = datetime.now()
    arac_yasi = su_an - trafiğe_cikis_tarihi
    
    if arac_yasi.days < 365:
        return "Araç henüz 1. yıl bakımına gelmemiştir."
    elif arac_yasi.days < 365 * 2:
        return "Araç 1. yıl bakım süresini tamamlamıştır, 2. yıl bakımına gelmelidir."
    elif arac_yasi.days < 365 * 3:
        return "Araç 2. yıl bakım süresini tamamlamıştır, 3. yıl bakımına gelmelidir."
    else:
        return "Araç 3. yıl bakım süresini tamamlamıştır, bakım yapılmalıdır."

# Test
gun = 11
ay = 3
yil = 2023
print(arac_servis_zamani_hesapla(gun, ay, yil))
