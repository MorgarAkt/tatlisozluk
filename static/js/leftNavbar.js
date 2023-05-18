var kategoriler = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
];
var kategorilerPerSayfa = 10; // Her sayfada kaç kategori gösterileceği

var currentPage = 1; // Şu anki sayfa numarası

function showKategoriler() {
    var startIndex = (currentPage - 1) * kategorilerPerSayfa;
    var endIndex = startIndex + kategorilerPerSayfa;
    var currentKategoriler = kategoriler.slice(startIndex, endIndex);

    var kategoriListesiDiv = document.getElementById("kategoriListesi");
    kategoriListesiDiv.innerHTML = "";

    for (var i = 0; i < currentKategoriler.length; i++) {
        var kategoriDiv = document.createElement("div");
        kategoriDiv.innerText = currentKategoriler[i];
        kategoriListesiDiv.appendChild(kategoriDiv);
    }
}

function showSayfaNumaralari() {
    var sayfaNumaralariSpan = document.getElementById("sayfaNumaralari");
    sayfaNumaralariSpan.innerHTML = "";

    var totalPages = Math.ceil(kategoriler.length / kategorilerPerSayfa);

    for (var i = 1; i <= totalPages; i++) {
        var sayfaLink = document.createElement("a");
        sayfaLink.href = "#";
        sayfaLink.innerText = i;
        sayfaLink.onclick = function () {
            currentPage = parseInt(this.innerText);
            showKategoriler();
            showSayfaNumaralari();
            return false;
        };

        sayfaNumaralariSpan.appendChild(sayfaLink);
    }
}

function previousPage() {
    if (currentPage > 1) {
        currentPage--;
        showKategoriler();
        showSayfaNumaralari();
    }
    return false;
}

function nextPage() {
    var totalPages = Math.ceil(kategoriler.length / kategorilerPerSayfa);
    if (currentPage < totalPages) {
        currentPage++;
        showKategoriler();
        showSayfaNumaralari();
    }
    return false;
}

showKategoriler();
showSayfaNumaralari();
