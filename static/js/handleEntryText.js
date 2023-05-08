const entryText = document.getElementsByClassName('create-entry-text')[0];
const titleName = document.getElementsByClassName('create-title-name')[0];
const maxEntryTextLength = 500;
const entryTextCounterText = document.getElementsByClassName('entry-text-counter-text')[0];
const entryTextCounter = document.getElementsByClassName('entry-text-counter')[0];
const form = document.getElementById('create-form');

form.addEventListener('submit', async (e) => {
    const entryTextLength = entryText.value.length;
    if (entryTextLength > 500) {
        alert("Karakter sayısı 500'ü geçemez");
        e.preventDefault();
    }
});



entryText.addEventListener('input', () => {
    const entryTextLength = entryText.value.length;
    if (entryTextLength > 500) {
        entryTextCounter.style.color = 'red';
    } else {
        entryTextCounter.style.color = 'white';
    }
    entryTextCounter.innerHTML = maxEntryTextLength - entryTextLength;
}
);