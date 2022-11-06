let mainVaribls = {
    inputWindow:document.querySelector('.inputWindow'),
    submiBtn:document.querySelector('.submit'),
    ul_todo:document.querySelector('.ul_todo'),
}

let deleteBtn = document.querySelector('.deleteBtn')

let i = 0;

function plusToDo(i){

    if(mainVaribls.inputWindow.value == ''){
        alert('plis fill window');
    } else {
        
        ++i    

        mainVaribls.ul_todo.innerHTML += `<li class='task_li'>`+ mainVaribls.inputWindow.value +`<button class='deleteBtn'>x</button></li>`;
        mainVaribls.inputWindow.value = '';
        
    }
}
mainVaribls.submiBtn.addEventListener('click', function(){
    plusToDo()
})