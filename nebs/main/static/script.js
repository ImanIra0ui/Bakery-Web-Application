items = document.querySelectorAll('.item-zone');
sortDropdown = document.querySelector('.sort-dropdown');
itemsContainer = document.querySelector('.display-items-grid');

for (var index = 0; index < items.length; index++) {
    console.log(items[index]);
}

sortDropdown.addEventListener('change', ()=>{
    if(sortDropdown.value == "name"){

        items = [].slice.call(items);

        items.sort(function(a, b) {
            var compA = a.querySelector('.item-name').innerHTML;
            var compB = b.querySelector('.item-name').innerHTML;
            return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
        });
        
        itemsContainer.innerHTML = "";

        for (var index = 0; index < items.length; index++) {
            itemsContainer.append(items[index]);
        }

    }else if(sortDropdown.value == "price-ascending"){
        items = [].slice.call(items);

        items.sort(function(a, b) {
            var compA = parseFloat(a.querySelector('.item-price').innerHTML);
            var compB = parseFloat(b.querySelector('.item-price').innerHTML);
            return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
        });
        
        itemsContainer.innerHTML = "";

        for (var index = 0; index < items.length; index++) {
            itemsContainer.append(items[index]);
        }
    }else if(sortDropdown.value == "price-descending"){
        items = [].slice.call(items);

        items.sort(function(a, b) {
            var compA = parseFloat(a.querySelector('.item-price').innerHTML);
            var compB = parseFloat(b.querySelector('.item-price').innerHTML);
            return (compA > compB) ? -1 : (compA < compB) ? 1 : 0;
        });
        
        itemsContainer.innerHTML = "";

        for (var index = 0; index < items.length; index++) {
            itemsContainer.append(items[index]);
        }
    }
});
