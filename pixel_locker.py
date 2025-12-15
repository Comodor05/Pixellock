# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import os
import argparse
import sys

# Terminal Renkleri
class Renk:
    YESIL = '\033[92m'
    KIRMIZI = '\033[91m'
    MAVI = '\033[94m'
    SIFIRLA = '\033[0m'

class ResimKilit:
    def __init__(self, anahtar):
        # Şifreyi sayısal bir "tohum" (seed) değerine çeviriyoruz
        self.anahtar_degeri = sum([ord(c) for c in anahtar]) % (2**32 - 1)
    
    def islem_yap(self, giris_yolu, cikis_yolu, mod="sifrele"):
        try:
            print(f"{Renk.MAVI}[*] Görüntü işleniyor: {giris_yolu}...{Renk.SIFIRLA}")
            
            # Resmi aç ve RGB formatına çevir
            resim = Image.open(giris_yolu).convert("RGB")
            
            # Matrise çevir (uint8 formatında)
            resim_verisi = np.array(resim, dtype=np.uint8)
            
            # Rastgelelik üretecini şifreyle sabitle
            np.random.seed(self.anahtar_degeri)
            
            # Resimle aynı boyutta gürültü maskesi üret
            maske = np.random.randint(0, 256, resim_verisi.shape, dtype=np.uint8)
            
            # XOR işlemi (Şifreleme/Çözme)
            yeni_veri = np.bitwise_xor(resim_verisi, maske)
            
            # Resmi tekrar oluştur
            sonuc_resim = Image.fromarray(yeni_veri.astype('uint8'))
            
            # Veri kaybı olmasın diye PNG olmak zorunda
            if not cikis_yolu.lower().endswith(".png"):
                cikis_yolu = os.path.splitext(cikis_yolu)[0] + ".png"
                
            sonuc_resim.save(cikis_yolu, format="PNG")
            
            durum_mesaji = "KİLİTLENDİ (Şifrelendi) 🔒" if mod == "sifrele" else "AÇILDI (Çözüldü) 🔓"
            print(f"{Renk.YESIL}[BAŞARILI] {durum_mesaji}")
            print(f"Dosya Kaydedildi: {cikis_yolu}{Renk.SIFIRLA}")
            
        except FileNotFoundError:
            print(f"{Renk.KIRMIZI}[HATA] Dosya bulunamadı! İsmi doğru yazdın mı?{Renk.SIFIRLA}")
        except Exception as e:
            print(f"{Renk.KIRMIZI}[HATA] Bir şeyler ters gitti: {e}{Renk.SIFIRLA}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Görsel Şifreleme Aracı - YMF")
    
    # Parametre ayarları
    parser.add_argument("dosya", help="İşlem yapılacak resim dosyası")
    parser.add_argument("-s", "--sifre", required=True, help="Gizli anahtar (Parola)")
    parser.add_argument("-m", "--mod", choices=["sifrele", "coz"], default="sifrele", help="Mod: sifrele (Şifrele) / coz (Çöz)")
    parser.add_argument("-o", "--output", help="Çıktı dosyasının adı (Opsiyonel)")
    
    args = parser.parse_args()
    
    # Aracı başlat
    kilit = ResimKilit(args.sifre)
    
    # Çıktı adı ayarlama
    if args.output:
        hedef_dosya = args.output
    else:
        # İsim verilmezse otomatik oluştur
        dosya_adi = os.path.basename(args.dosya)
        isim_kok, _ = os.path.splitext(dosya_adi)
        
        if args.mod == "sifrele":
            hedef_dosya = f"kilitli_{isim_kok}.png"
        else:
            temiz_isim = isim_kok.replace("kilitli_", "")
            hedef_dosya = f"cozulen_{temiz_isim}.png"

    # Mod bilgisini fonksiyona gönder
    kilit.islem_yap(args.dosya, hedef_dosya, args.mod)