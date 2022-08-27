

function openModal(url) {
    $('.modal').load(url, function () {
        $('.modal').addClass('modal__show');
        const closeModal = document.querySelector("#modal__close");
        closeModal.addEventListener('click', (e) => {
            e.preventDefault();
            $('.modal').removeClass("modal__show");
        });
    });
}

$(".hide").on('click', function () {
    $(".menu ul").toggle('slow');
})

