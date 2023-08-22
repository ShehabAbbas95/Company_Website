const cartElement = document.getElementById("cart")
function addToCart(event) {
    let counter = 0;
    // Get the id of the parent on which the button add is clicked
    let target = event.target.parentNode.id;
    // Get the remove button element exist in that specific Div
    // Change the disabled attribute to allow user to remove the added product
    let remove_button = document.getElementById(`${target}`).childNodes[15];
    remove_button.removeAttribute("disabled");
    // Check if there is already products in cart using localStorage
    if (localStorage.getItem(`${target}`)){
        // Get the already exist products
        counter = parseInt(localStorage.getItem(`${target}`)) + 1;
        // Increase the quantity of the selected product
        localStorage.setItem(`${target}`,`${counter}`);
        // Change the cartCounter in the localStorage
        localStorage.getItem(`cartCounter`)?cartCounter = parseInt(localStorage.getItem(`cartCounter`)) + 1 :cartCounter = 1;
        localStorage.setItem(`cartCounter`,`${cartCounter}`);
        // Change the cart item inner text 
        cartElement.innerText = localStorage.getItem("cartCounter");
    }
    else{
        // If the selected product not exist in the locale storage then use the counter which starts from Zero
        counter++;
        // Add the selected product to the locale storage
        localStorage.setItem(`${target}`,`${counter}`);
        // Check if there are any products in the cart else initiate the cartCounter
        localStorage.getItem(`cartCounter`) ? cartCounter = parseInt(localStorage.getItem(`cartCounter`)) + 1 : cartCounter = 1;
        // Change the cartCounter in the localStorage
        localStorage.setItem(`cartCounter`,`${cartCounter}`);
        // Change the cart item inner text 
        cartElement.innerText = localStorage.getItem("cartCounter");
    }
}
// Function to handle items removed from the cart
function removeFromCart(event) {
    // Get the id of the parent on which the button add is clicked
    let target = event.target.parentNode.id;
    // Get the remove button element exist in that specific Div
    // Change the disabled attribute to allow user to remove the added product
    if (localStorage.getItem(`${target}`) > 1){
        // Decrease the quantity of the selected product
        let counter = parseInt(localStorage.getItem(`${target}`)) - 1;
        localStorage.setItem(`${target}`,`${counter}`);
        // Get the cartCounter from localStorage and decrease it
        let cartCounter = parseInt(localStorage.getItem("cartCounter")) - 1;
        // Change the cartCounter in the localStorage
        localStorage.setItem(`cartCounter`,`${cartCounter}`);
        // Change the cart item inner text 
        cartElement.innerText = localStorage.getItem("cartCounter");
    }
    else {
        // Remove the item if the counter is zero
        localStorage.removeItem(`${target}`);
        // Disable the remove button for that specific product
        let remove_button = document.getElementById(`${target}`).childNodes[15];
        remove_button.setAttribute("disabled",'');
        // Get the cartCounter from localStorage and decrease it
        let cartCounter = parseInt(localStorage.getItem("cartCounter")) - 1;
        // Change the cartCounter in the localStorage
        localStorage.setItem(`cartCounter`,`${cartCounter}`);
        // Change the cart item inner text 
        cartElement.innerText = localStorage.getItem("cartCounter");
    }
}
// Function to allow us to reset the counter and enable remove buttons for the previously selected products
function cartState() {
    // Check if there are any products in the cart else initiate the cartCounter
    localStorage.getItem(`cartCounter`)?cartCounter = parseInt(localStorage.getItem(`cartCounter`)) + 1:cartCounter = 0;
    // Change the cart item inner text 
    cartElement.innerText = localStorage.getItem("cartCounter");
    if (localStorage.length > 0){
        // Get all remove product buttons
        let buttons = document.getElementsByClassName("remove");
        for (let button of buttons){
            // Check if the selected button is in localStorage so it had been selected 
            if(localStorage.getItem(button.parentNode.id)){
                // Remove the disabled attribute
                button.removeAttribute("disabled");
            }
        }
    }
}
// Call cartState function on window load
window.addEventListener("load",cartState);
