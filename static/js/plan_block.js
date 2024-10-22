
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);  
}

function drop(ev, temp, team) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    // ev.target.appendChild(document.getElementById(data));
    console.log(temp, data);
    const url = `/plan/block/${temp}/${data}/${team}`;

    window.location = url;
}