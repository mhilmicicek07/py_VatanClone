# 🖥️ py_VatanClone Projesi  

Bu proje, **Vatan Bilgisayar** benzeri bir e-ticaret sitesinin temel işlevlerini örnekleyen bir **Django tabanlı web uygulamasıdır**.  
Kullanıcılar ürünleri görüntüleyebilir, kategori bazlı filtreleme yapabilir, giriş yaparak yeni ürün ekleyebilir veya mevcut ürünleri düzenleyip silebilir.  
Amaç, Django framework’üyle backend geliştirme becerilerini göstermek ve temel CRUD mantığını uygulamaktır.

---

## 🚀 Özellikler  

- 🛒 Ürün listeleme, kategoriye göre filtreleme  
- ➕ Yeni ürün ekleme (giriş yapmış kullanıcılar için)  
- ✏️ Ürün düzenleme ve 🗑️ silme  
- 👤 Kullanıcı girişi ve kayıt olma  
- 🔒 Sadece giriş yapan kullanıcıların ürün ekleyebilmesi ve yönetebilmesi  
- 📸 Ürün görseli yükleme (media/uploads dizininde saklanır)  
- 📄 Basit, okunabilir ve genişletilebilir Django yapısı  

---

## 🧩 Kullanılan Teknolojiler  

| Teknoloji | Rolü |
|------------|-----------|
| **Python 3.10+** | Backend geliştirme dili |
| **Django 4.2** | Web framework |
| **SQLite3** | Veritabanı |
| **HTML5, CSS3, Bootstrap** | Frontend tasarımı |
| **Django Template Engine** | Dinamik HTML üretimi |
| **Pillow** | Görsel yükleme işlemleri |

---

## 📂 Proje Dosya Yapısı  

📁 **py_VatanClone**  
├── 📄 manage.py  
├── 📁 py_VatanClone (ana proje ayarları)  
│   ├── settings.py  
│   ├── urls.py  
│   ├── wsgi.py  
│   └── asgi.py  
├── 📁 product (ürün uygulaması)  
│   ├── models.py  
│   ├── views.py  
│   ├── forms.py  
│   ├── urls.py  
│   └── templates/product/  
├── 📁 user (kullanıcı uygulaması)  
│   ├── views.py  
│   ├── forms.py  
│   ├── urls.py  
│   └── templates/user/  
├── 📁 static (CSS, JS, img)  
└── 📁 media/uploads (ürün görselleri)  

---

## ⚙️ Kurulum ve Çalıştırma  

Projeyi yerel ortamınızda çalıştırmak için:  

```bash
git clone https://github.com/mhilmicicek07/py_VatanClone.git
cd py_VatanClone/py_VatanClone
python -m venv venv
venv\Scripts\activate   # (Windows için)  
# veya source venv/bin/activate (Linux/macOS için)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Ardından tarayıcıda açın:
👉 http://localhost:8000

🧠 Teknik Açıklama
Uygulama iki temel Django app’ten oluşur:

product: Ürün ve kategori yönetimi

user: Kullanıcı kimlik doğrulama sistemi

Her ürün bir kullanıcıya bağlıdır (ForeignKey(User)), böylece kullanıcı sadece kendi ürünlerini düzenleyip silebilir.
Slug sistemi ürün başlığına göre otomatik üretilir ve URL dostu bağlantılar sağlar.
Formlar Bootstrap sınıflarıyla entegre edilmiştir.

👨‍💻 Geliştirici
Mehmet Hilmi Çiçek
💼 Full Stack Web Developer
📍 Geislingen an der Steige, Almanya

💬 “Basit ama tutarlı kod, karmaşık olandan her zaman üstündür.”

🪪 Lisans
Bu proje açık kaynaklıdır.
İsteyen herkes kodu inceleyebilir, geliştirebilir veya kişisel projelerinde referans olarak kullanabilir.