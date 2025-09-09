const sepet = [];

function urunEkle(urun) {
    sepet.push(urun);
    sepettekiUrunleriGuncelle();
}

function urunCikar(urunAdi, urunFiyat) {
    const index = sepet.findIndex(urun => urun.urunAdi === urunAdi && urun.urunFiyat === urunFiyat);
    if (index > -1) {
        sepet.splice(index, 1);
        sepettekiUrunleriGuncelle();
    }
}

function sepettekiUrunleriGuncelle() {
    const sepetElement = document.querySelector('#sepetListesi');
    const toplamTutarElement = document.querySelector('#toplamTutar');
    let toplamTutar = 0;

    sepetElement.innerHTML = '';
    
    sepet.forEach((urun) => {
        toplamTutar += urun.urunFiyat;
        sepetElement.innerHTML += `<li>${urun.urunAdi} - ${urun.urunFiyat} $ <button onclick="urunCikar('${urun.urunAdi}', ${urun.urunFiyat})">Çıkar</button></li>`;
    });

    toplamTutarElement.textContent = `Toplam Tutar: ${toplamTutar} $`;
}
