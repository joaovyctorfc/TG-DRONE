window.addEventListener('DOMContentLoaded', function() {
    var footerTop = document.querySelector('footer').offsetTop;
    var formTop = document.querySelector('.formulario').offsetTop;
    var chatButton = document.querySelector('.chat-btn');

    function adjustChatButtonPosition() {
        var scrollPosition = window.scrollY;
        if (window.innerWidth <= 1020) {
            // Para telas de até 1020px, o botão de chat para antes do formulário "Fale Conosco"
            if (scrollPosition >= formTop - window.innerHeight) {
                chatButton.style.bottom = (scrollPosition - formTop + window.innerHeight + 20) + 'px';
            } else {
                chatButton.style.bottom = '20px';
            }
        } else {
            // Para telas maiores que 1020px, o botão de chat para no rodapé
            if (scrollPosition >= footerTop - window.innerHeight) {
                chatButton.style.bottom = (scrollPosition - footerTop + window.innerHeight + 20) + 'px';
            } else {
                chatButton.style.bottom = '20px';
            }
        }
    }

    window.addEventListener('scroll', adjustChatButtonPosition);
});



