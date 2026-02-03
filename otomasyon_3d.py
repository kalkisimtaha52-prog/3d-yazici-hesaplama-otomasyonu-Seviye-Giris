# 3D Yazıcı Maliyet Hesaplama (Detaylı)

# Kullanıcıdan veriler
filament = float(input("Kullanılacak filament miktarı (gram): "))
fiyat_filament = float(input("1 gram filament fiyatı (TL): "))
calisma_suresi = float(input("Baskı süresi (saat): "))
elektrik_tuketimi = float(input("Yazıcının 1 saatte tükettiği elektrik (kWh): "))
elektrik_fiyat = float(input("1 kWh elektrik fiyatı (TL): "))

# Opsiyonel: destek ve infill
destek_var_mi = input("Destek yapısı olacak mı? (e/h): ").lower()
infill = float(input("Infill oranı (%) [0-100]: "))

# Hesaplamalar
filament_artisi = filament * (1 + (infill / 100))
if destek_var_mi == 'e':
    filament_artisi *= 1.1  # destek yapısı +%10 filament

toplam_filament_maliyet = filament_artisi * fiyat_filament
toplam_elektrik_maliyet = calisma_suresi * elektrik_tuketimi * elektrik_fiyat
toplam_maliyet = toplam_filament_maliyet + toplam_elektrik_maliyet

# Sonuçlar
print("\n--- 3D Yazıcı Maliyet Hesaplama ---")
print(f"Filament maliyeti: {toplam_filament_maliyet:.2f} TL")
print(f"Elektrik maliyeti: {toplam_elektrik_maliyet:.2f} TL")
print(f"Toplam maliyet: {toplam_maliyet:.2f} TL")

