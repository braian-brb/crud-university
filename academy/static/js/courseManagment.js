(function () {
    const btnDeleted = document.querySelectorAll('.btnDeleted');

    btnDeleted.forEach(btn => {
        btn.addEventListener('click', e => {
            const confirmed = confirm('Are you sure you want to delete this course?');
            if(!confirmed) e.preventDefault();
        })
    })
})();   