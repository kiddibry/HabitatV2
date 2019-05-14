$(document).ready(function(){
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/houses?search_filter=' + searchText,
                type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `
                            <div>
                                <a href="/houses/${d.id}" > 
                                <div class="Boxman">   
                                    <img src="${d.firstImage}" alt="image"/>
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                 </div>
                                </a>
                            </div>

                            <style>
                                .Boxman {
                                    border: 1px solid black;
                                    margin-bottom: 1em;
                                }
                            
                            </style>


                            `
                });
                $('.houses').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                 /* TODO: show toastr*/
                console.error(error);
            }
        })
    });
});