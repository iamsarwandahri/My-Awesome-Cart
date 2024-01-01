if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'))
    $('#cart').html(sum(cart))
    updateCart(cart)
    $('#popcart').popover('hide')
}

$('.divpr').on('click','button.cart',function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        var qty = cart[idstr][0] = cart[idstr][0] + 1;
        var price = cart[idstr][2] = cart[idstr][2]*qty
    }
    else {
        qty = 1
        var name = $('#name'+idstr).html()
        var price = $('#price'+idstr).html()
        cart[idstr] = [qty,name,parseInt(price)]
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    $('#cart').html(sum(cart))
    updateCart(cart)
});


function updateCartItem(cart) {

    var popStr = "<h5>Cart for your items in my shopping cart</h5> <div>"
    var i = 1
    btn = `<a id='clearCart' class="btn btn-primary my-2" href="#" role="button">Clear Cart</a><a href='/checkout/' id='checkout' class="btn btn-primary my-2 mx-2" href="#" role="button">Checkout</a><br>`
    for (var item in cart) {
        if (cart[item][0] == 0) {
            popStr = popStr + ""
        } else {
            popStr = popStr + "<b>" + i + "</b>. "
            popStr = popStr + $('#name' + item).html() + " Qty: " + cart[item][0] + '<br>'
            popStr = popStr + "</div>"
            i = i + 1
        }
    }
    for(var item in cart){
        if(cart[item][0]!=0 && popStr.includes(btn)==false){
            popStr = popStr + btn
            }
    }

    $('#popcart').attr('data-content', popStr)
    $('#popcart').popover('show')
}


// Updating Cart

function updateCart(cart) {
    for (var item in cart) {
        if (cart[item][0] != 0) {
            $('#bt' + item).html("<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>")
        }
        updateCartItem(cart)

        // else{
        //     $('#bt' + item).html("<button id='"+item+"' class='btn btn-primary cart'>Add To Cart</button>")

        // }
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    $('#cart').html(sum(cart))
}

//Clearing Cart
$('body').on('click', '#clearCart', function () {
    cart = JSON.parse(localStorage.getItem('cart'))
    for(var item in cart){
        $('#bt'+item).html("<button id="+item+" class='btn btn-primary cart'>Add To Cart</button>")
    }
    localStorage.clear()
    cart = {}
    updateCart(cart)
    var popStr = "<h5>Cart for your items in my shopping cart</h5>"
    $('#popcart').attr('data-content', popStr)
    $('#popcart').popover('hide')
})



//  Returning sum of object
function sum(obj) {
    let sum = 0;
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            sum += obj[key][0];
        }
    }
    return sum;
}

// Addding and removing Items in Cart
$('.divpr').on('click', '.minus', function () {
    var id = this.id.slice(5,)
    cart[id][0] = cart[id][0] - 1
    cart[id][0] = Math.max(0, cart[id][0])
    $('#val' + id).html(cart[id][0])
    updateCart(cart)
})
$('.divpr').on('click', '.plus', function () {
    var id = this.id.slice(4,)
    cart[id][0] = cart[id][0] + 1
    $('#val' + id).html(cart[id][0])
    updateCart(cart)
})