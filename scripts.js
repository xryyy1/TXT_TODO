document.querySelectorAll('.icon').forEach(item => {
    item.addEventListener('click', event => {
        const iconId = event.target.id;
        if (iconId === 'icon8') {
            window.location.href = 'index2.html';
        } else {
            document.querySelectorAll('.content').forEach(content => {
                content.classList.remove('active');
            });
            const contentId = 'content' + iconId.replace('icon', '');
            document.getElementById(contentId).classList.add('active');
        }
    });
});
