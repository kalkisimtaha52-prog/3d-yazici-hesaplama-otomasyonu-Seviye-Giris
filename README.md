# PrintCost 🚀

> 3D Yazıcı baskı maliyetlerinizi saniyeler içinde doğrulukla hesaplayın.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <a href="#-özellikler">Özellikler</a> •
  <a href="#-kurulum">Kurulum</a> •
  <a href="#-nasıl-çalışır">Nasıl Çalışır?</a> •
  <a href="#-yol-haritası">Yol Haritası</a>
</p>

---

## 🎯 PrintCost Nedir?

**PrintCost**, 3D baskı meraklıları ve profesyonelleri için geliştirilmiş, malzeme ve enerji maliyetlerini hassas bir şekilde hesaplayan açık kaynaklı bir CLI/Web aracıdır.

Karmaşık hesaplamalarla vakit kaybetmeyin. Sadece verileri girin ve projenizin gerçek maliyetini anında görün.

---

## ✨ Özellikler

| Özellik | Açıklama |
|---------|-------------|
| **Hassas Hesaplama** | Filament gramajı ve birim fiyat üzerinden net maliyet |
| **Enerji Analizi** | Yazıcının güç tüketimi ve elektrik tarifesine göre maliyet hesaplama |
| **Gelişmiş Faktörler** | Infill oranı ve destek (support) yapıları için otomatik ekleme |
| **Modern UI** | Streamlit ile güçlendirilmiş, kullanıcı dostu arayüz |

---

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.9 veya daha yeni bir sürüm.

### Kurulum

```bash
# Projeyi klonlayın
git clone https://github.com/kalkisimtaha52-prog/printcost.git
cd printcost

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
streamlit run oso.py
```

---

## 🏗️ Mimari ve Mantık

Uygulama, verilen parametreleri aşağıdaki formüllere göre işler:

1.  **Filament Maliyeti**: `(Net Gramaj * (1 + Doluluk Oranı)) * (Destek Çarpanı) * Birim Fiyat`
2.  **Elektrik Maliyeti**: `Baskı Süresi * Güç Tüketimi (kWh) * Elektrik Fiyatı`
3.  **Toplam**: `Filament Maliyeti + Elektrik Maliyeti`

---

## 📋 Eksiklikler ve Geliştirme Önerileri

Yapılan analiz sonucunda projenin şu alanlarda geliştirilmesi hedeflenmektedir:

- [ ] **Malzeme Kütüphanesi**: PLA, ABS, PETG gibi malzemeler için hazır yoğunluk/fiyat profilleri.
- [ ] **Grafiksel Görselleştirme**: Maliyet dağılımını gösteren pasta grafikler.
- [ ] **Çoklu Dil Desteği**: İngilizce ve Türkçe dil seçenekleri.
- [ ] **PDF Raporlama**: Hesaplama sonuçlarını PDF olarak dışa aktarma.

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Hata bildirimleri ve özellik talepleri için Issue açabilirsiniz.

---

## 📄 Lisans

MIT License - Detaylar için [LICENSE](LICENSE) dosyasına göz atın.
