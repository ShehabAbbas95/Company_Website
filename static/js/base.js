// Get the logout button or link
let logout = document.getElementById("logout");
// Add an event listner to clear the cart on logout
if (logout){
    logout.addEventListener("click",()=> {
        let confirmAction = confirm(`Do You Want to empty your cart`);
        if (confirmAction){
            localStorage.clear();
        }
    });
};
// Function to clear the flashing messages
const clearFlashes = () =>{
    let flashElement = document.getElementById("flashes");
    if(flashElement){
        flashElement.style.display = "none";
    }
};
setTimeout(clearFlashes,5000);
