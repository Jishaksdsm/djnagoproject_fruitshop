$(document).ready(function() {
    // Add to cart button click event
    $('.add-to-cart-form').on('submit', function(e) {
        e.preventDefault();
        var form = $(this);
        var fruitId = form.data('fruit-id');
        var quantity = form.find('.quantity').val();

        // Send AJAX request to add item to cart
        $.ajax({
            type: 'POST',
            url: '/add-to-cart/' + fruitId + '/',
            data: {
                'quantity': quantity,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response) {
                // Update the cart icon or any other UI indicator
                alert('Item added to cart!');
            },
            error: function(response) {
                alert('Error adding item to cart.');
            }
        });
    });
});
