$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

// Cart functionality
$(document).ready(function() {
    // Le code de gestion du panier a été déplacé dans addtocart.html
    // pour éviter les doubles appels et assurer une gestion cohérente
});

$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            // Mettre à jour le bouton sans recharger la page
            $('.plus-wishlist').replaceWith(`
                <a pid="${id}" class="minus-wishlist btn btn-action" style="
                    display: inline-block;
                    padding: 15px 40px;
                    background: #00f7ff;
                    color: #000;
                    font-weight: bold;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    border: none;
                    margin-right: 15px;
                    text-decoration: none;
                    box-shadow: 0 0 15px #00f7ff;
                    transition: all 0.3s;
                ">
                    <i class="fas fa-heart me-2"></i> In Wishlist
                </a>
            `);
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            // Mettre à jour le bouton sans recharger la page
            $('.minus-wishlist').replaceWith(`
                <a pid="${id}" class="plus-wishlist btn btn-action" style="
                    display: inline-block;
                    padding: 15px 40px;
                    background: #00f7ff;
                    color: #000;
                    font-weight: bold;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    border: none;
                    margin-right: 15px;
                    text-decoration: none;
                    box-shadow: 0 0 15px #00f7ff;
                    transition: all 0.3s;
                ">
                    Add To Wishlist<i class="far fa-heart me-2"></i>
                </a>
            `);
        }
    })
})