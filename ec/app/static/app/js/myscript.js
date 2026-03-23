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

    $(document).on('click', '.plus-wishlist', function(e) {
        e.preventDefault();
        var id = $(this).attr('pid').toString();
        var $button = $(this);
        $.ajax({
            type: 'GET',
            url: '/pluswishlist/',
            data: { prod_id: id },
            success: function(data) {
                $button.replaceWith(`
                    <a pid="${id}" class="minus-wishlist btn btn-secondary-glass">
                        <i class="fas fa-heart text-danger"></i>
                    </a>
                `);
                if (data && data.wishitem !== undefined) {
                    var wishlistBadge = $('#wishlist-badge');
                    wishlistBadge.text(data.wishitem);
                    if (data.wishitem > 0) {
                        wishlistBadge.show();
                    } else {
                        wishlistBadge.hide();
                    }
                }
            },
            error: function(xhr) {
                console.error('Wishlist add failed', xhr.responseText);
            }
        });
    });

    $(document).on('click', '.minus-wishlist', function(e) {
        e.preventDefault();
        if (!confirm('Remove this item from wishlist?')) {
            return;
        }
        var id = $(this).attr('pid').toString();
        var $button = $(this);
        var $card = $button.closest('.col-lg-3, .col-md-4, .col-sm-6');
        $.ajax({
            type: 'GET',
            url: '/minuswishlist/',
            data: { prod_id: id },
            success: function(data) {
                if ($card.length) {
                    $card.fadeOut(250, function() { $(this).remove(); });
                } else {
                    $button.replaceWith(`
                        <a pid="${id}" class="plus-wishlist btn btn-secondary-glass">
                            <i class="far fa-heart"></i>
                        </a>
                    `);
                }
                if (data && data.wishitem !== undefined) {
                    var wishlistBadge = $('#wishlist-badge');
                    wishlistBadge.text(data.wishitem);
                    if (data.wishitem > 0) {
                        wishlistBadge.show();
                    } else {
                        wishlistBadge.hide();
                    }
                }
            },
            error: function(xhr) {
                console.error('Wishlist remove failed', xhr.responseText);
            }
        });
    });
});