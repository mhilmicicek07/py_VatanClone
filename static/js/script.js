let sepet = JSON.parse(localStorage.getItem("sepet")) || [];

// Sayfa yüklendiğinde sepeti güncelle
document.addEventListener("DOMContentLoaded", sepettekiUrunleriGuncelle);

function urunEkle(urun) {
    sepet.push(urun);
    localStorage.setItem("sepet", JSON.stringify(sepet));
    sepettekiUrunleriGuncelle();
}

function urunCikar(urunAdi, urunFiyat) {
    const index = sepet.findIndex(
        u => u.urunAdi === urunAdi && u.urunFiyat === urunFiyat
    );
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

    sepet.forEach((urun) => {
        toplamTutar += urun.urunFiyat;
        sepetElement.innerHTML += `
            <li class="dropdown-item d-flex justify-content-between align-items-center">
                ${urun.urunAdi} - ${urun.urunFiyat} ₺
                <button class="btn btn-sm btn-danger" onclick="urunCikar('${urun.urunAdi}', ${urun.urunFiyat})">X</button>
            </li>`;
    });

    if (sepet.length > 0) {
        sepetElement.innerHTML += `
            <li><hr class="dropdown-divider"></li>
            <li>
                <button class="btn btn-sm btn-warning w-100" onclick="sepetiTemizle()">Sepeti Temizle</button>
            </li>`;
    }

    toplamTutarElement.textContent = `Toplam Tutar: ${toplamTutar} ₺`;
}

// let sepet = JSON.parse(localStorage.getItem("sepet")) || [];

// // Sayfa yüklendiğinde sepeti güncelle
// document.addEventListener("DOMContentLoaded", sepettekiUrunleriGuncelle);

// function urunEkle(urun) {
//     sepet.push(urun);
//     localStorage.setItem("sepet", JSON.stringify(sepet));
//     sepettekiUrunleriGuncelle();
// }

// function urunCikar(urunAdi, urunFiyat) {
//     const index = sepet.findIndex(
//         u => u.urunAdi === urunAdi && u.urunFiyat === urunFiyat
//     );
//     if (index > -1) {
//         sepet.splice(index, 1);
//         localStorage.setItem("sepet", JSON.stringify(sepet));
//         sepettekiUrunleriGuncelle();
//     }
// }

// function sepettekiUrunleriGuncelle() {
//     const sepetElement = document.querySelector('#sepetListesi');
//     const toplamTutarElement = document.querySelector('#toplamTutar');
//     let toplamTutar = 0;

//     if (!sepetElement || !toplamTutarElement) return;

//     sepetElement.innerHTML = '';

//     sepet.forEach((urun, i) => {
//         toplamTutar += urun.urunFiyat;
//         sepetElement.innerHTML += `
//             <li class="dropdown-item d-flex justify-content-between align-items-center">
//                 ${urun.urunAdi} - ${urun.urunFiyat} ₺
//                 <button class="btn btn-sm btn-danger" onclick="urunCikar('${urun.urunAdi}', ${urun.urunFiyat})">X</button>
//             </li>`;
//     });

//     toplamTutarElement.textContent = `Toplam Tutar: ${toplamTutar} ₺`;
// }
