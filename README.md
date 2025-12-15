🔐 PixelLock - Görsel Şifreleme Aracı

PixelLock, görüntüleri matematiksel matris operasyonları ve XOR şifreleme algoritması kullanarak şifreleyen gelişmiş bir Python aracıdır. Pikselleri NumPy kütüphanesi ile manipüle ederek, doğru anahtar olmadan açılması imkansız "gürültülü" (noise) görsellere dönüştürür.

Bu proje, görüntü işleme ve veri güvenliği (Kriptografi) prensiplerini birleştirir.

📷 Örnek Görünüm

Aşağıda şifreleme işleminin sonucu görülmektedir. Orijinal resim anlamsız bir gürültü yığınına dönüşür.

1. Orijinal Resim

<img src="deneme.jpg" width="400" />

2. Şifrelenmiş Hali (Kilitli)

<img src="kilitli_deneme.png" width="400" />

🚀 Özellikler

Matematiksel Şifreleme: Görüntü verisini RGB matrislerine dönüştürüp işler.

Anahtar Tabanlı Güvenlik: Kullanıcının belirlediği anahtar (Password) ile deterministik gürültü üretir.

Kayıpsız Dönüşüm: JPG bozulmalarını önlemek için otomatik PNG dönüşümü yapar.

Özel Çıktı: Şifrelenen dosyanın ismini belirleme imkanı sunar.

🛠️ Kurulum

Gerekli kütüphaneleri yükleyin:

pip install numpy pillow 


💻 Kullanım

Komutlar tamamen Türkçeleştirilmiştir.

🔒 1. Resmi Şifreleme

python pixel_locker.py deneme.jpg -s 1234 -m sifrele


Çıktı: kilitli_deneme.png

🔓 2. Şifreyi Çözme

python pixel_locker.py kilitli_deneme.png -s 1234 -m coz


Çıktı: cozulen_deneme.png

⚙️ Özel İsim Verme

İsterseniz -o parametresi ile dosya adını kendiniz belirleyebilirsiniz:

python pixel_locker.py deneme.jpg -s 1234 -o gizli_resim.png