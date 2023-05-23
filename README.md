# Tatlisozluk

Bu, Django projesi olup aşağıdaki gereksinimlere sahiptir:

- Django
- Pillow


## Installation

1. Depoyu klonlayın:
```
git clone https://github.com/MorgarAkt/tatlisozluk
cd tatlisozluk
```


2. Sanal bir ortam oluşturun:
```
python -m venv venv
```

3. Sanal ortamı etkinleştirin:
- macOS ve Linux için:
```
source venv/bin/activate
```
- Windows için:
```
venv\Scripts\activate
```

4. Bağımlılıkları yükleyin:
```
pip install -r requirements.txt
```

5. Veritabanı migrasyonlarını çalıştırın:
```
python manage.py migrate
```

6. Geliştirme sunucusunu başlatın:
```
python manage.py runserver
```

7. Uygulamaya http://localhost:8000/ adresinden erişebilirsiniz.

## Amaç
Bu Django projesi Ekşisözlük sitesinden ilhan almış bir final proje ödevidir.


## Katkıda Bulunma
Katkılarınızı bekliyoruz! Bir hata bulursanız veya bir öneriniz varsa lütfen aşağıdaki adımları izleyin:

1. Depoyu "fork" edin.
2. Özellik veya hata düzeltmesi için yeni bir dal oluşturun.
3. Değişikliklerinizi yapın ve açıklayıcı "commit" mesajlarıyla kaydedin.
4. Değişikliklerinizi "fork" ettiğiniz depoya gönderin.
5. Değişikliklerinizi açıklayan bir "pull request" oluşturun.

## Lisans
Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
