const deleteEntry = document.getElementsByClassName('delete-entry');
const editEntry = document.getElementsByClassName('edit-entry');

for (let i = 0; i < deleteEntry.length; i++) {
    deleteEntry[i].addEventListener('click', async () => {
        const entryId = dislikeBtns[i].getAttribute('data-entry-id');
        const titleId = dislikeBtns[i].getAttribute('data-title-id');
        const url = `entry/${entryId}/delete`;
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
        });
        // window.location.href = `/slug?titleId=${titleId}`;
        if (response.status === 204 || response.status === 200 || response.status === 201 || response.status === 202) {
            document.getElementsByClassName(`entry-${entryId}`)[0].remove();
        }
        if (response.status === 403) {
            alert("Bu işlemi yapmaya yetkiniz yok");
            return;
        }
        let entryCount = document.getElementsByClassName("title").length;
        let titleNameCount = document.getElementsByClassName("title-name").length;
        if (entryCount == 0) {
            window.location.href = '/';
        } else if (entryCount == 1 || titleNameCount == 0) {
            window.location.href = `/title?titleId=${titleId}`;
        } 
    });
}

for (let i = 0; i < editEntry.length; i++) {
    editEntry[i].addEventListener('click', async () => {
        const entryId = dislikeBtns[i].getAttribute('data-entry-id');
        const titleId = dislikeBtns[i].getAttribute('data-title-id');
        window.location.href = `/title/${titleId}/entry/${entryId}/edit`;
    });
}
