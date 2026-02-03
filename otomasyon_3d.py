import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="PrintCost - 3D Yazıcı Maliyet Hesaplayıcı",
    page_icon="🚀",
    layout="centered"
)

# Stil
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.title("3D Yazıcı Maliyet Hesaplama 🚀")
st.markdown("---")

# Yan Panel - Ayarlar ve Presets
with st.sidebar:
    st.header("⚙️ Malzeme Ayarları")
    material_type = st.selectbox(
        "Malzeme Türü",
        ["Özel", "PLA", "PETG", "ABS", "TPU"]
    )
    
    # Preset değerleri
    presets = {
        "PLA": 0.45,  # Gram fiyatı (Tahmini : 450 TL / 1000g)
        "PETG": 0.55,
        "ABS": 0.50,
        "TPU": 0.85,
        "Özel": 0.0
    }
    
    default_price = presets[material_type]
    fiyat_filament = st.number_input(
        "1 gram filament fiyatı (TL):", 
        min_value=0.0, 
        value=default_price if material_type != "Özel" else 0.0,
        step=0.01
    )

    st.markdown("---")
    st.header("⚡ Enerji Ayarları")
    elektrik_tuketimi = st.number_input("Yazıcı Tüketimi (kWh/saat):", min_value=0.0, value=0.1, step=0.01)
    elektrik_fiyat = st.number_input("Elektrik Birim Fiyat (TL/kWh):", min_value=0.0, value=2.5, step=0.1)

# Ana Panel - Girişler
col1, col2 = st.columns(2)

with col1:
    filament = st.number_input("Kullanılacak filament miktarı (gram):", min_value=0.0, step=1.0)
    calisma_suresi = st.number_input("Baskı süresi (saat):", min_value=0.0, step=0.1)

with col2:
    infill = st.slider("Infill (Doluluk) oranı (%)", min_value=0, max_value=100, value=20)
    destek_var_mi = st.checkbox("Destek yapısı (Support) var mı?")

# Hesaplamalar
# Doluluk oranına göre filament artışı (basit modelleme)
filament_toplam = filament * (1 + (infill / 500)) # Infill artışı doğrusal ama küçük bir etki
if destek_var_mi:
    filament_toplam *= 1.15  # Destek yapısı için %15 ekleme

toplam_filament_maliyet = filament_toplam * fiyat_filament
toplam_elektrik_maliyet = calisma_suresi * elektrik_tuketimi * elektrik_fiyat
toplam_maliyet = toplam_filament_maliyet + toplam_elektrik_maliyet

# Sonuçları göster
st.markdown("---")
st.subheader("📊 Maliyet Analizi")

m1, m2, m3 = st.columns(3)
m1.metric("Filament", f"{toplam_filament_maliyet:.2f} TL")
m2.metric("Elektrik", f"{toplam_elektrik_maliyet:.2f} TL")
m3.metric("TOPLAM", f"{toplam_maliyet:.2f} TL", delta=f"{toplam_maliyet * 0.1:.2f} TL (Vergi/Aşınma Tahmini)", delta_color="inverse")

if filament > 0:
    st.info(f"💡 Bu baskı için yaklaşık **{filament_toplam:.1f} gram** filament kullanılacaktır.")

# Alt Bilgi
st.markdown("---")
st.caption("PrintCost v1.0 | CoreBridge Standardına Uygun Geliştirilmiştir.")
