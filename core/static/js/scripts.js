$( document ).ready(function() {
    let deleteBtn = $('.delete-btn');
    let outputBtn = $('.output-btn');
    let editBtn = $('.edit-btn');
    let searchBtn = $('#search-btn');
    let searchForm = $('#search-form');

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

    $(editBtn).on('click', function(e) {
        e.preventDefault();
        window.location.href = "http://127.0.0.1:8000";


        let result = confirm('Deseja alterar os dados do veículo?');

        if(result) {
            window.location.href = delLink;
        }
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