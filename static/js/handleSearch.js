document.addEventListener('DOMContentLoaded', function () {
    var searchInput = document.getElementsByClassName('search')[0];
    var searchResults = document.getElementById('search-results');
    var searchButton = document.getElementsByClassName('search-button')[0];

    searchInput.addEventListener('input', async () => {
        var query = searchInput.value;
        if (query.trim() !== '') {
            try {
                var response = await fetch('/title/search?query=' + encodeURIComponent(query));
                var data = await response.json();
                var results = data.results;
                searchResults.innerHTML = '';
                if (results.length > 0) {
                    for (let i = 0; i < results.length; i++) {
                        console.log(results[i]);
                        const option = document.createElement('div');
                        option.classList.add('dropdown-item');
                        option.setAttribute('href', "/" + results[i].fields.slug + '?titleId=' + results[i].pk);
                        option.addEventListener('click', () => {
                            window.location = option.getAttribute('href');
                        });

                        option.textContent = results[i].fields.title_name;
                        searchResults.appendChild(option);
                    };
                    searchResults.style.display = 'block';
                } else {
                    searchResults.style.display = 'none';
                }
            } catch (error) {
                console.error('Error:', error);
            }
        } else {
            searchResults.style.display = 'none';
        }
    });

    searchButton.addEventListener('click', () => {
        var query = searchInput.value;
        let searchResults = document.getElementById('search-results');
        if (query.trim() !== '' && searchResults.children.length > 0) {
            window.location = searchResults.children[0].getAttribute('href');
        } else {
            alert('Lütfen önce aramaya bir şeyler yazın!');
        }
    }
    );
});