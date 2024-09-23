# etikettofilename
## Etiket Üzerindeki Sayıları Dosya İsimleriyle Değiştirme Aracı

Bu Python programı, taranmış resimler üzerinde bulunan sarı etiketlerin üzerindeki kırmızı sayıları tespit eder ve bu sayıları kullanarak dosyaları yeniden adlandırır. Program, kullanıcıdan bir sayı aralığı alır ve sadece bu aralık içindeki sayıları dikkate alır.

### Özellikler

- Sarı etiketler üzerindeki kırmızı sayıları otomatik olarak tespit eder.
- Tespit edilen sayıları dosya isimleri olarak kullanarak dosyaları yeniden adlandırır.
- Kullanıcıdan sayı aralığını grafiksel arayüz ile alır (varsayılan: 15000 - 25000).
- Dosya seçim işlemi için grafiksel arayüz kullanır.

### Gereksinimler

- **Windows İşletim Sistemi**
- **Python 3** (sadece Python kurulu olması yeterlidir)

### Gerekli Python Kütüphaneleri

- `opencv-python`
- `numpy`
- `pytesseract`
- `tkinter` (Python ile birlikte gelir)

### Ek Gereksinimler

- **Tesseract OCR** yazılımı (metin tanıma için)

### Kurulum ve Kullanım

#### 1. Python Kurulumu

Eğer sisteminizde Python kurulu değilse, [Python'ın resmi web sitesinden](https://www.python.org/downloads/windows/) Python 3 sürümünü indirip kurabilirsiniz. Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın.

#### 2. Gerekli Kütüphanelerin Kurulumu

Komut İstemi'ni (CMD) açın ve aşağıdaki komutları sırayla çalıştırın:

```bash
pip install opencv-python
pip install numpy
pip install pytesseract
```

#### 3. Tesseract OCR Kurulumu

- [Tesseract OCR Windows Kurulumu](https://github.com/UB-Mannheim/tesseract/wiki) sayfasından en son Windows yükleyicisini indirin.
- Yükleyiciyi çalıştırın ve Tesseract OCR'ı varsayılan ayarlarla kurun.
- Kurulum dizini genellikle `C:\Program Files\Tesseract-OCR` olacaktır.

**Not:** Eğer Tesseract OCR farklı bir dizine kurulmuşsa veya `pytesseract` Tesseract OCR'ı bulamazsa, Python kodunda `pytesseract.pytesseract.tesseract_cmd` değişkenini ayarlamanız gerekebilir:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### 4. Python Kodunu Çalıştırma

- Yukarıdaki Python kodunu bir metin dosyasına kopyalayın ve `etiket_oku.py` adıyla kaydedin.
- `etiket_oku.py` dosyasını, resim dosyalarının bulunduğu klasöre kopyalayın.
- Komut İstemi'nde dosyanın bulunduğu klasöre gidin:

```bash
cd C:\resim_klasoru
```

- Python kodunu çalıştırın:

```bash
python etiket_oku.py
```

#### 5. Programı Kullanma

- Program çalıştığında, önce sizden minimum ve maksimum sayı değerlerini girmenizi isteyen iki adet pencere açılacaktır. Varsayılan değerler sırasıyla 15000 ve 25000'dir.
- Sayı aralığını girdikten sonra, resimleri seçmeniz için bir dosya seçme penceresi açılacaktır. Yeniden adlandırmak istediğiniz resimleri seçin ve "Aç" butonuna tıklayın.
- Program seçtiğiniz her bir resmi işleyecek, etiketi tespit edecek, üzerindeki sayıyı okuyacak ve dosyayı bu sayıyla yeniden adlandıracaktır.
- İşlem tamamlandığında, Komut İstemi penceresinde işlem durumu ile ilgili mesajlar görüntülenecektir.

### Önemli Notlar

- **Renk Ayarları:** Etiketlerin renk tonları ve aydınlatma koşulları farklılık gösterebilir. Gerekirse sarı ve kırmızı renk aralıklarını (`lower_yellow`, `upper_yellow`, `lower_red1`, `upper_red1`, vb.) Python kodunda ayarlayabilirsiniz.
- **OCR Doğruluğu:** Tesseract OCR'ın doğru çalışabilmesi için resimlerin net ve okunaklı olması gerekmektedir. Bulanık veya düşük çözünürlüklü resimlerde doğruluk oranı düşebilir.
- **Dosya Çakışmaları:** Aynı sayıya sahip bir dosya zaten mevcutsa, program bu dosyayı atlayacaktır.
- **Sayı Aralığı:** Sadece belirttiğiniz sayı aralığındaki sayılar kabul edilir. Bu aralığı ihtiyaçlarınıza göre ayarlayabilirsiniz.

### Sorun Giderme

- **Tesseract Bulunamadı Hatası:** Eğer `pytesseract` Tesseract OCR'ı bulamazsa, Python kodunda Tesseract'ın yolunu belirtmeniz gerekebilir (yukarıdaki notlara bakınız).
- **Kütüphane Eksikliği Hatası:** Eğer bir kütüphane bulunamadı hatası alırsanız, ilgili kütüphanenin kurulu olduğundan emin olun ve gerekirse `pip install` komutunu tekrar çalıştırın.
- **Renk Tespiti Sorunları:** Etiket veya sayı renkleri tespit edilemiyorsa, renk aralıklarını ayarlamak için kodda değişiklik yapmanız gerekebilir.

### Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

---

## Destek

Herhangi bir sorunla karşılaşırsanız veya ek yardım gerekiyorsa, lütfen GitHub üzerinden bir issue açın veya benimle iletişime geçin.

# Teşekkürler

Programı kullandığınız için teşekkür ederim! Umarım işinizi kolaylaştırır.
