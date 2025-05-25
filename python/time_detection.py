import numpy as np

# Örnekleme frekansı (Hz)
fs = 6_000_000

# Dosya adı
dosya_yolu = "/home/orkun-alp/Documents/fmcw_bitirme_calismalari/radar_parameter/pluto_rndis_deneme_6Mhz_200k_1M.dat"

# Veriyi oku
data = np.fromfile(dosya_yolu, dtype=np.complex64)

# Süreyi hesapla
time = len(data) / fs

# Sonucu yazdır
print(f"Dosya: {dosya_yolu}")
print(f"Örnek sayısı: {len(data)}")
print(f"Gerçek kayıt süresi: {time:.2f} saniye")