$( document ).ready(function() {
    let deleteBtn = $('.delete-btn');
    let outputBtn = $('.output-btn');
    let searchBtn = $('#search-btn');
    let searchForm = $('#search-form');
    let paymentBtn = $('.bnt-payment');

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        let delLink = $(this).attr('href');
        let result = confirm('Deseja excluir a entrada do veículo?');

        if(result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(outputBtn).on('click', function(e) {
        e.preventDefault();

        let delLink = $(this).attr('href');
        let result = confirm('Deseja liberar a saída do veículo?');

        if(result) {
            window.location.href = delLink;
        }
    });

});