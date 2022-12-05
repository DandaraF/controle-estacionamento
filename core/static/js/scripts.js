$( document ).ready(function() {
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var outBtn = $('.out-btn');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja excluir a entrada do veículo?');

        if(result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(outBtn).on('click', function() {
        e.preventDefault();
        console.log('sim')
//        alert("Saída não permitida. Pagamento em aberto!");
    });


});