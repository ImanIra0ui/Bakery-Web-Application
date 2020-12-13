/* Set values + misc */
var fadeTime = 300;

$(document).ready(function() {

  $("#subMe").click(function(){
      var counter = parseInt($("#hiddenVal").val());
      counter--;
      if (counter<0) {
        $("#hiddenVal").val(0);
      }
      else {
        $("#hiddenVal").val(counter);
        $( '.quantity input' ).change();
      }
  });

  $("#addMe").click(function(){
    var counter = parseInt($("#hiddenVal").val());
    counter++;
    $("#hiddenVal").val(counter);
    $( '.quantity input' ).change();
  });

  $("#addMe2").click(function(){
  var counter2 = parseInt($("#hiddenVal2").val());
  counter2++;
    $("#hiddenVal2").val(counter2);
    $( '.quantity input' ).change();
  });
  $("#subMe2").click(function(){
    var counter2 = parseInt($("#hiddenVal2").val());
    counter2--;
    if (counter2<0) {
      $("#hiddenVal2").val(0);
    }
    else {
      $("#hiddenVal2").val(counter2);
      $( '.quantity input' ).change();
    }
});

$("#addMe1").click(function(){
  var counter1 = parseInt($("#hiddenVal1").val());
  counter1++;
  
  $("#hiddenVal1").val(counter1);
  $( '.quantity input' ).change();
});
  $("#subMe1").click(function(){
    var counter1 = parseInt($("#hiddenVal1").val());
    counter1--;
    if (counter1<0) {
      $("#hiddenVal1").val(0);
    }
    else {
      $("#hiddenVal1").val(counter1);
      $( '.quantity input' ).change();
    }
});


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
    /*$(this).fadeOut(fadeTime, function() {*/
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    /*});*/
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