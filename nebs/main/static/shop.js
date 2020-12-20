/* Set values + misc */
var fadeTime = 300;

/*$(document).ready(function() {

/*$(".buttonadd").click(function(){
  alert('button clicked');
});*/


/*$(".buttonadd").click(function(){
    var counter1 = parseInt($('.quantity input').val());
    counter1--;
    if (counter1<1) {
      $('.quantity input').val(100);
    }
    else {
      $('.quantity input').val(100);
      $( '.quantity input' ).change();
    }
});
*/

setInputFilter(document.getElementById("number"), function(value) {
  return /^\d*\.?\d*$/.test(value); 
  // Allow digits and '.' only, using a RegExp
});

function setInputFilter(textbox, inputFilter) {
  ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(function(event) {
    textbox.addEventListener(event, function() {
      if (inputFilter(this.value)) {
        this.oldValue = this.value;
        this.oldSelectionStart = this.selectionStart;
        this.oldSelectionEnd = this.selectionEnd;
      } else if (this.hasOwnProperty("oldValue")) {
        this.value = this.oldValue;
        this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
      } else {
        this.value = "";
      }
    });
  });
}

$('.buttonsub').click(function() {
  var $n = $(this).parent(".quantity").find(".quantity-field");

	  var QtyVal = Number($n.val());
	    if (QtyVal > 1) {
		    $n.val(QtyVal-1);
    }
    updateSumItems();
    updateQuantity($n);
});

$('.buttonadd').click(function() {
  var $n = $(this).parent(".quantity").find(".quantity-field");
  
    $n.val(Number($n.val())+1 );
    updateSumItems();
    updateQuantity($n);
});

/* Assign actions */
$('.quantity input').change(function() {
  updateQuantity(this);
});

$('.remove button').click(function() {
  removeItem(this);
});

$(document).ready(function() {
  updateSumItems();
});

/*function addQuantity(quantityInput) {
  /* Calculate line price 
  var productRow = $(quantityInput).parent(".quantity").find(".quantity-field");
  var price = parseFloat(productRow.children('.price').text());
  var quantity = $(quantityInput).val();
    quantity++;
    $(quantityInput).val(quantity);
    $(quantityInput).change();
    productRow.find('.quantity-field').val(quantity);

  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  /* Update line price display and recalc cart totals 
  productRow.children('.subtotal').each(function() {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });
  
  productRow.find('.item-quantity').text(quantity);
  updateSumItems();
}*/

/*function subQuantity(quantityInput) {
  /* Calculate line price 
  var productRow = $(quantityInput).parent().parent();
  var price = parseFloat(productRow.children('.price').text());
  var quantity = $(quantityInput).val();
    quantity--;

      
      $(quantityInput).val(quantity);
      $(quantityInput).change();
      productRow.find('.quantity-field').val(quantity);
    
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  /* Update line price display and recalc cart totals 
  productRow.children('.subtotal').each(function() {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });
  
  productRow.find('.item-quantity').text(quantity);
  updateSumItems();
}*/

/* Recalculate cart */
function recalculateCart(onlyTotal) {
  var subtotal = 0;

  /* Sum up row totals */
  $('.basket-product').each(function() {
    subtotal += parseFloat($(this).children('.subtotal').text());
  });

  /* Calculate totals */
  var total = subtotal;

  /*If switch for update only total, update only total display*/
  if (onlyTotal) {
    /* Update total display */
    $('.total-value').fadeOut(fadeTime, function() {
      $('#basket-total').html(total.toFixed(2));
      $('.total-value').fadeIn(fadeTime);
    });
  } else {
    /* Update summary display. */
    $('.final-value').fadeOut(fadeTime, function() {
      $('#basket-subtotal').html(subtotal.toFixed(2));
      $('#basket-total').html(total.toFixed(2));
      if (total == 0) {
        $('.checkout-cta').fadeOut(fadeTime);
      } else {
        $('.checkout-cta').fadeIn(fadeTime);
      }
      $('.final-value').fadeIn(fadeTime);
    });
  }
}

/* Update quantity */
function updateQuantity(quantityInput) {
  /* Calculate line price */
  var productRow = $(quantityInput).parent().parent();
  var price = parseFloat(productRow.children('.price').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  /* Update line price display and recalc cart totals */
  productRow.children('.subtotal').each(function() {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });

  productRow.find('.item-quantity').text(quantity);
  updateSumItems();
}

function updateSumItems() {
  var sumItems = 0;
  $('.quantity input').each(function() {
    sumItems += parseInt($(this).val());
  });
  $('.total-items').text(sumItems);
}

/* Remove item from cart */
function removeItem(removeButton) {
  /* Remove row from DOM and recalc cart total */
  var productRow = $(removeButton).parent().parent();
  productRow.slideUp(fadeTime, function() {
    productRow.remove();
    recalculateCart();
    updateSumItems();
  });
}