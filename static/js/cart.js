const cartItemsElement =  document.getElementById("cartItems");
const placeOrderElement = document.getElementById("placeOrder");
const emptyCartElement = document.getElementById("emptyCart");
function cart() {
    if (localStorage.length>1){
        // Get the cart item from local storage and delete the cart counter
        let cartItems = {...localStorage};
        delete cartItems.cartCounter;
        // Loop over the items and add them to the dom
        for (let item in cartItems){
            const newParagraph = document.createElement('p');
            const newHR = document.createElement(`HR`);
            newParagraph.innerText = `${item} : ${localStorage.getItem(`${item}`)}`;
            cartItemsElement.append(newParagraph,newHR);
        }
    }
    // If there are no items in the cart
    else{
        // Create element, change it's text and append it to the DOM
        const newParagraph = document.createElement('h3');
        newParagraph.innerText = `Your Cart is Empty`;
        cartItemsElement.append(newParagraph);
        // Disable the placing order button
        placeOrderElement.setAttribute("disabled",'');
        // Change the text of empty cart button to add items
        emptyCartElement.innerText = "Add Items";

    }
};
// Call the function
cart();
// Clear the cart 
function emptyCart() {
    // If cart is empty redirect to the shop after clicking add items
    if(document.getElementById("emptyCart").innerText == "Add Items"){
        window.location = "/shop";
    }
    else{
        localStorage.clear();
        // Change the cart text
        cartItemsElement.innerHTML = "<h3>Your Cart Is Empty </h3>";
        // Disable the placing order button
        placeOrderElement.setAttribute("disabled",'');
        // Change the text of empty cart button to add items
        emptyCartElement.innerText = "Add Items";
    }
}
