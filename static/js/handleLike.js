const likeBtns = document.getElementsByClassName('likeBtn');
const dislikeBtns = document.getElementsByClassName('dislikeBtn');
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;


for (let i = 0; i < likeBtns.length; i++) {
    likeBtns[i].addEventListener('click', async () => {
        const entryId = likeBtns[i].getAttribute('data-entry-id');
        const titleId = likeBtns[i].getAttribute('data-title-id');
        await fetch(`/title/${titleId}/${entryId}/like`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        });
        window.location.reload();
    });
}

for (let i = 0; i < dislikeBtns.length; i++) {
    dislikeBtns[i].addEventListener('click', async () => {
        const entryId = dislikeBtns[i].getAttribute('data-entry-id');
        const titleId = dislikeBtns[i].getAttribute('data-title-id');
        await fetch(`/title/${titleId}/${entryId}/dislike`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        });
        window.location.reload();
    });
}

