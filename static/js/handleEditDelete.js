const deleteEntry = document.getElementsByClassName('delete-entry');
const editEntry = document.getElementsByClassName('edit-entry');

for (let i = 0; i < deleteEntry.length; i++) {
    deleteEntry[i].addEventListener('click', async () => {
        const entryId = dislikeBtns[i].getAttribute('data-entry-id');
        const titleId = dislikeBtns[i].getAttribute('data-title-id');
        const url = `entry/${entryId}/delete`;
        await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        });
        window.location.href = `/slug?titleId=${titleId}`;
    });
}

for (let i = 0; i < editEntry.length; i++) {
    editEntry[i].addEventListener('click', async () => {
        const entryId = dislikeBtns[i].getAttribute('data-entry-id');
        const titleId = dislikeBtns[i].getAttribute('data-title-id');
        window.location.href = `/title/${titleId}/entry/${entryId}/edit`;
    });
}
