function toDo(){
    content = document.querySelector('.content').value
    if (content){
        $.ajax({
            method:'post',
            data:{
                "content":content,
                csrfmiddlewaretoken:$("[name = 'csrfmiddlewaretoken']").val(),
            },
            success: function(data){
                console.log(data)
            }
        })
    }

    tbody = document.getElementById('tbody')
    if (content){
        tbody.innerHTML += `
        <tr>
            <th scope="row">4</th>
            <td>${content}</td>
            <td>In proggress</td>
            <td>
                <button class="btn
                    btn-danger" style="width:
                    84px;">Delete</button>
                <form method="post"><button
                
                type="submit" class="btn
                btn-success">Finished</button></form>
            </td>
        </tr>`
    }
}

function deleteTask(id){
    let $ = jQuery.noConflict()
    task = document.getElementById(`task_${id}`)
    setTimeout(task.innerHTML = "",200)
    const modal = new bootstrap.Modal(document.getElementById('modal'))
    console.log(modal)
    modal.hide()
    $('modal').modal('dispose')
}