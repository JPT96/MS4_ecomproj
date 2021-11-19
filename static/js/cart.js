var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
        console.log("User doesn't have a account")}
        else{
            updateUserorder(productId, action)


        } 

    
})
function updateUserorder(productId, action){
    console.log('User has been authorised')

    var url = '/update_item'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json'},
            body:JSON.stringify({'productId':productId, 'action':action})

})
.then((response)=>{
    return response.json();
})
.then((data)=> {
    console.log('Data:', data)
});
}
}