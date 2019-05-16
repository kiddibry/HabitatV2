$(document).ready(function(){
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/houses?search_filter=' + searchText,
                type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<a href="/houses/${ d.id }">
                            <div class="single_house">
                                <div class="name">
                                    <fieldset>
                                        <legend>   
                                             ${ d.name }
                                            <p style="font-size: 0.8em"> Postal code: ${ d.postal_code }</p>
                                        </legend>
                                        <div class="description">
                                            <p> ${ d.description } </p>
                                        </div>
                                    </fieldset>
                                </div>
                    
                    
                                <div class="photo_frame">
                    
                                        <img class="house_photo" src="${d.firstImage}" alt="image"/>
                                        <div class="size">
                                            <p>Size: ${ d.size } M<sup>2</sup> price: ${ d.price } kr</p>
                                        </div>
                    
                                </div>
                            </div>
                            </a>

                            <style>
                                .single_house {
                                    margin-bottom: 1em;
                                    overflow: auto;
                                    border: 1px solid black;
                                    background-color: orange;
                                }
                                
                                
                                .name {
                                
                                    margin-top: 0.3em;
                                    margin-left: 0.3em;
                                    border: 1px solid black;
                                    text-align: center;
                                    float: left;
                                    width: 29%;
                                    overflow: auto;
                                    color: black;
                                
                                }
                                
                                .description {
                                    margin-left: 0.2em;
                                    margin-right: 0.2em;
                                    float: left;
                                }
                                
                                .photo_frame {
                                
                                    float: right;
                                    width: 70%;
                                    height: 100%;
                                    position: relative;
                                    z-index: 1;
                                }
                                
                                .house_photo {
                                    border: 1px solid black;
                                    border-radius: 20px;
                                    width:  100%;
                                    max-width: 100%;
                                    max-height: 450px;
                                    position: relative;
                                }
                                
                                .size {
                                    border: 1px groove black;
                                    border-radius: 3px;
                                    background-color: white;
                                    float: right;
                                    position: absolute;
                                    right: 0px;
                                    bottom: 0px;
                                    z-index: 3;
                                    padding-left: 0.2em;
                                    padding-right: 0.2em;
                                    color: black;
                                
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