let sepet = JSON.parse(localStorage.getItem("sepet")) || [];

// Sayfa yüklendiğinde sepeti güncelle
document.addEventListener("DOMContentLoaded", sepettekiUrunleriGuncelle);

function urunEkle(urunAdi, urunFiyat) {
    const urun = { urunAdi, urunFiyat: parseFloat(urunFiyat) };
    sepet.push(urun);
    localStorage.setItem("sepet", JSON.stringify(sepet));
    sepettekiUrunleriGuncelle();
}

function urunCikar(index) {
    if (index > -1) {
        sepet.splice(index, 1);
        localStorage.setItem("sepet", JSON.stringify(sepet));
        sepettekiUrunleriGuncelle();
    }
}

function sepetiTemizle() {
    sepet = [];
    localStorage.removeItem("sepet");
    sepettekiUrunleriGuncelle();
}

function sepettekiUrunleriGuncelle() {
    const sepetElement = document.querySelector('#sepetListesi');
    const toplamTutarElement = document.querySelector('#toplamTutar');
    let toplamTutar = 0;

    if (!sepetElement || !toplamTutarElement) return;

    sepetElement.innerHTML = '';

    sepet.forEach((urun, index) => {
        toplamTutar += urun.urunFiyat;
        sepetElement.innerHTML += `
            <li class="dropdown-item text-wrap">
                <div class="d-flex justify-content-between align-items-center">
                    <span class="me-2">${urun.urunAdi}</span>
                    <span>${urun.urunFiyat} ₺</span>
                </div>
                <button class="btn btn-sm btn-outline-danger w-100 mt-1"
                    onclick="urunCikar(${index})">
                    Çıkar
                </button>
            </li>`;
    });

    if (sepet.length > 0) {
        sepetElement.innerHTML += `
            <li class="dropdown-item text-center">
                <button class="btn btn-sm btn-danger w-100" onclick="sepetiTemizle()">
                    Sepeti Temizle
                </button>
            </li>`;
    }

    toplamTutarElement.textContent = `Toplam Tutar: ${toplamTutar} ₺`;
}