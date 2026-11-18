
# Staj Görev Yönetimi
### Full-Stack CRUD Web Application

## Proje Hakkında

Bu proje, İletişim Yazılım bünyesinde gerçekleştirdiğim 20 iş günlük zorunlu yaz stajı kapsamında geliştirilmiştir.

Projenin amacı; kullanıcı kimlik doğrulama (Authentication) ve CRUD (Create, Read, Update, Delete) işlemlerini içeren, frontend ve backend bileşenlerinden oluşan bir web uygulaması geliştirmektir.

Uygulama, ilişkisel ve NoSQL veritabanlarıyla çalışacak şekilde tasarlanmış ve Docker kullanılarak konteynerize edilmiştir.

## Kullanılan Teknolojiler

### Backend
- Python
- FastAPI

### Frontend
- React.js
- Vite

### Veritabanları
- Microsoft SQL Server (MSSQL)
- MongoDB

### Altyapı ve Araçlar
- Docker
- Docker Compose
- Miniconda
- VS Code

## Uygulama Özellikleri

- Kullanıcı kayıt ve giriş işlemleri
- Kullanıcı kimlik doğrulama (Authentication)
- Veri ekleme (Create)
- Veri listeleme (Read)
- Veri güncelleme (Update)
- Veri silme (Delete)
- Form doğrulama ve hata yönetimi
- Responsive kullanıcı arayüzü
- MSSQL ve MongoDB entegrasyonu
- Docker Compose ile servislerin birlikte çalıştırılması

## Proje Mimarisi

Proje üç temel bileşenden oluşmaktadır:

- **Frontend:** React.js ile geliştirilen kullanıcı arayüzü.
- **Backend:** FastAPI ile geliştirilen API ve iş mantığı.
- **Database:** MSSQL ve MongoDB veritabanları.

Uygulama servisleri Docker Compose aracılığıyla birlikte çalıştırılmaktadır.

## Kurulum ve Çalıştırma

Projeyi yerel ortamda çalıştırmak için Docker ve Docker Compose kurulu olmalıdır.

1. Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/esrahatunoglu/staj-gorev-yonetimi.git
```

2. Proje klasörüne girin:

```bash
cd staj-gorev-yonetimi
```

3. Uygulamayı Docker Compose ile başlatın:

```bash
docker compose up --build
```

4. Servisler başlatıldıktan sonra uygulamayı yapılandırılmış yerel adresler üzerinden kullanabilirsiniz.

## Proje Durumu

**Tamamlandı – Çalışır Durumda**

Uygulama Docker Compose üzerinden başlatılabilmekte; kullanıcı kayıt, giriş ve CRUD işlemleri gerçekleştirilebilmektedir.

## Kazanımlar

Bu proje kapsamında:

- Full-stack web geliştirme süreçlerini deneyimleme,
- REST API geliştirme ve kullanma,
- İlişkisel ve NoSQL veritabanlarıyla çalışma,
- Kullanıcı kimlik doğrulama süreçlerini uygulama,
- Docker ve Docker Compose kullanımı,
- Backend ve frontend entegrasyonu

konularında uygulamalı deneyim kazandım.

## Geliştirici

**Esra Nur Hatunoğlu**

Doğuş Üniversitesi  
Bilgisayar Mühendisliği (İngilizce) – 2. Sınıf

GitHub: [@esrahatunoglu](https://github.com/esrahatunoglu)

