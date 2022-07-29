;(function(){
    const modal = new bootstrap.Modal(document.getElementById('modal'))

    htmx.on('htmx:afterSwap',(e)=>{
        console.log(e.detail.target.id)
        if (e.detail.target.id === "dialog")
        modal.show()
    })
    
    htmx.on('htmx:beforeSwap',(e)=>{
        console.log(e.detail.target.id)
        if (e.detail.target.id === "dialog" && !e.detail.xhr.response)
        modal.hide()
    })

})()