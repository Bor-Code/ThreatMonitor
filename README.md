🛡️ ThreatMonitor: Konteyner Tabanlı Tuzak Sistemi ve Tehdit İstihbaratı Kontrol Paneli
ThreatMonitor , gerçek zamanlı olarak yetkilendirilmiş erişim girişimlerini tespit etmek, düzenlemek ve görselleştirmek için tasarlanmış mikroservis tabanlı bir güvenlik sistemidir. Docker tabanlı mimarisi sayesinde honeypot servisini analiz ederek dışarıda izole eder ve güvenli bir şekilde çalıştırır.
📖 Proje Hakkında
Siber güvenlik dünyasında honeypot'lar, saldırganları gerçek sistemlerden uzaklaştırmak ve bunların taktiklerini öğrenmek için kullanılan kritik araçlardır. ThreatMonitor, bu konsept modern ve kullanıcı dostu bir yaklaşımla hayata geçirmeyi sağlar.
🎯 Ne İşe Yarar?
Saldırı Testi: Sisteminize yapılan yetkisiz erişim girişimlerini gerçek zamanlı olarak yakalar
Tehdit Analizi: Saldırganların IP adreslerini, denedikleri şifreleri ve saldırı zamanlarını destekliyorlar
Görsel İstihbarat: Saldırıların dünya haritası üzerinde Nereden geldiği gösterilir
Eğitim & Araştırma: Siber güvenlik kurumları ve araştırmacılar için mükemmel bir laboratuvar ortamı
🏗️ Sistem Mimarisi
ThreatMonitor, Docker Compose ile yönetilen 3 bağımsız mikroservisten oluşur. Her servis kendi konteynerinde sistem dağıtımını ve kapsamını genişletir:

1. 🍯(Tuzak)
Teknoloji: Python tabanlı TCP sunucusu
Görev: Savunmasız bir servis taklit ederek saldırganları cezbeder
Veri Toplama:
Saldırgan'ın IP adresi
Saldırı zamanı (timestamp)
Denenen şifre yöntemleri
İletişim: Yakaladığı verileri asenkron olarak Redis kuyruğuna gönderilir

2. 💾 Redis (Veri Aracısı)
Rol: Bellek içi mesaj toplu ve veri tabanı
Avantajlar:
Yüksek hızlı veri işleme
Servisler arası kontrolörler (gevşek bağlantı)
Düşük gecikme süresi ile gerçek zamanlı iletişim

3. 📊 Kontrol Paneli (Kontrol Paneli)
Çerçeve: Streamlit ile geliştirilmiş web arayüzü
Özellikler:
Redis'ten gerçek zamanlı veri çekme
Dünya Tehdit Haritası ile bakanlığı görselleştirme
IP tabanlı saldırı istatistikleri
Test için kurulum modu
Kullanıcı Dostu: Teknik bilgi gerektirmeden kullanılabilir geliştirme

🛠️ Kurulum ve Kullanım
Ön Gereksinimler
Sisteminizde aşağıdaki yazılımların kurulu olması gerekmektedir:
Docker (versiyon 20.10 veya üzeri önerilir)
Docker Compose (versiyon 1.29 veya üzeri önerilir)

💡 Not: Docker'ı henüz kurmamışsanız, resmi Docker eklentilerini ziyaret edebilirsiniz.

Adım Adım Kurulum
1️⃣ Projeyi İndirin
vurmak# Repository'yi bilgisayarınıza klonlayın
git clone https://github.com/KULLANICI_ADIN/ThreatMonitor.git
2️⃣ Proje Dizinine Geçin
vurmakcd ThreatMonitor
3️⃣ Servisleri Yansıtın
vurmak# Docker konteynerlerini oluştur ve başlat
docker-compose up --build

⏱️İlk Başlatma: İlk çalıştırmada Docker'ın kullanımı indirilip derlenecektir. Bu işlem internet hızınıza bağlı olarak birkaç dakika boyunca gerçekleştirilebilir.

4️⃣ Dashboard'a Erişin
Servisler başarıyla başlatıldıktan sonra:

Kontrol Paneli URL'si:  http://localhost :8501
Honeypot Portu: 9999 (varsayılan ayar)
Redis Portu: 6379 (dahili iletişim için)


📊 Kullanım Senaryoları
🧪 Test Modunda Çalıştırma
Dashboard'daki "Simülasyon Modu" özelliğini kullanarak gerçek saldırı olmadan sistemi test edebilirsiniz:

Dashboard'u seçin
Sol menüden "Simülasyon Modu" nu etkinleştirin
Rastgele saldırı verilerinin haritadaki yansımasını izleyin

🎯 Gerçek Honeypot Kullanımı
Honeypot'u gerçek saldırılara açmak için:
vurmak# Honeypot'u harici erişime aç (DİKKATLİ KULLANIN!)
# docker-compose.yml dosyasında ports ayarını düzenleyin
# ports:
#   - "0.0.0.0:9999:9999"

⚠️ GÜVENLİK UYARISI: Honeypot'u internete açmadan önce politikalarınızı gözden geçirin. Yalnızca izole edilmiş test ortamlarında kullanın.

🔧 Yankı
Ortam Değiştiricileri
.envdosyayı oluşturabilirler özelleştirmeler yapabilirsiniz:
çevreHONEYPOT_PORT=9999
REDIS_HOST=redis
REDIS_PORT=6379
DASHBOARD_PORT=8501
Loglama Ayarları
Honeypot servisinde log seviyesinin ayarlanması için honeypot/config.pybilgilerin listesi:
PythonLOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR

🤝 Katkıda Bulunma
Bu proje açık kaynaklıdır ve katkılarınızı memnuniyetle karşılarım! Katkıda bulunmak için:

💬 Destek ve İletişim
E-Posta:non.mrbora@gmail.com

Teşekkürler
ThreatMonitor'ü kullandığınız için teşekkür ederim! Projenin katkıda bulunarak siber güvenlikten izlenebilmesine destek olabilirsiniz.
⭐ Projeyi beğendiyseniz yıldız bırakmayı unutmayın!

--------------------------------------------------------------------------------------------------------------------------------

🛡️ ThreatMonitor: Container-Based Honeypot System and Threat Intelligence Dashboard
ThreatMonitor is a microservices-based security system designed to detect, manage, and visualize authorized access attempts in real time. Thanks to its Docker-based architecture, it analyzes the honeypot service, isolates it externally, and runs it securely.
📖 About the Project
In the cybersecurity world, honeypots are critical tools used to lure attackers away from real systems and learn their tactics. ThreatMonitor brings this concept to life with a modern and user-friendly approach.
🎯 What Does It Do?
Attack Testing: Captures unauthorized access attempts to your system in real time
Threat Analysis: Supports attackers' IP addresses, passwords they tried, and attack times
Visual Intelligence: Shows where attacks originated on a world map
Education & Research: An excellent laboratory environment for cybersecurity institutions and researchers
🏗️ System Architecture
ThreatMonitor consists of 3 independent microservices managed with Docker Compose. Each service extends the system deployment and scope in its own container:

1. 🍯(Trap)
Technology: Python-based TCP server
Task: Lures attackers by mimicking a vulnerable service
Data Collection:
Attacker's IP address
Attack time (timestamp)
Password methods attempted
Communication: Captured data is sent asynchronously to the Redis queue

2. 💾 Redis (Data Broker)
Role: In-memory message queue and database
Advantages:
High-speed data processing
Inter-service controllers (loose coupling)
Real-time communication with low latency

3. 📊 Control Panel (Dashboard)
Framework: Web interface developed with Streamlit
Features:
Real-time data retrieval from Redis
Visualization of the Ministry with the Global Threat Map
IP-based attack statistics
Setup mode for testing
User-Friendly: Development without requiring technical knowledge

🛠️ Setup and Usage
Prerequisites
The following software must be installed on your system:
Docker (version 20.10 or higher recommended)
Docker Compose (version 1.29 or higher recommended)

💡 Note: If you haven't installed Docker yet, you can visit the official Docker add-ons.

Step-by-Step Installation
1️⃣ Download the Project
Clone the vurmak# Repository to your computer
git clone https://github.com/KULLANICI_ADIN/ThreatMonitor.git
2️⃣ Navigate to the Project Directory
vurmakcd ThreatMonitor
3️⃣ Mirror the Services
vurmak# Create and start Docker containers
docker-compose up --build

⏱️First Start: On the first run, Docker will be downloaded and compiled. This process may take a few minutes depending on your internet speed.

4️⃣ Access the Dashboard
After the services have started successfully:

Control Panel URL:  http://localhost :8501
Honeypot Port: 9999 (default setting)
Redis Port: 6379 (for internal communication)


📊 Use Cases
🧪 Run in Test Mode
You can test the system without a real attack using the “Simulation Mode” feature on the Dashboard:

Select the Dashboard
Enable “Simulation Mode” from the left menu
Watch the reflection of random attack data on the map

🎯 Actual Honeypot Usage
To open the Honeypot to real attacks:
vurmak# Open the Honeypot to external access (USE WITH CAUTION!)
# Edit the ports setting in the docker-compose.yml file
# ports:
#   - “0.0.0.0:9999:9999”

⚠️ SECURITY WARNING: Review your policies before opening the Honeypot to the internet. Use only in isolated test environments.

🔧 Echo
Environment Modifiers
You can create a .env file and make customizations:
environmentHONEYPOT_PORT=9999
REDIS_HOST=redis
REDIS_PORT=6379
DASHBOARD_PORT=8501
Logging Settings
List of information for setting the log level in the honeypot service:
PythonLOG_LEVEL = “INFO”  # DEBUG, INFO, WARNING, ERROR

🤝 Contribute
This project is open source, and I welcome your contributions! To contribute:

💬 Support and Contact
E-Posta:non.mrbora@gmail.com

Thank You
Thank you for using ThreatMonitor! You can support the project by contributing to its cybersecurity monitoring capabilities.
⭐ If you like the project, don't forget to leave a star!

Translated with DeepL.com (free version)
