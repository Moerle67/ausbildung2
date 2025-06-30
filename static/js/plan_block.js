
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);  
}

function drop(ev, group, year, kw, day, daytime, team) {
    // alert("Test");
    ev.preventDefault();
    var aubi = ev.dataTransfer.getData("text");
    // ev.target.appendChild(document.getElementById(data));
    //path('block/<int:group>/<int:year>/<int:kw>/<int:day>/<str:daytime>/<int:aubi_id>/<int:team>', views.block, name='block'),
    const url = `/plan/block/${group}/${year}/${kw}/${day}/${daytime}/${aubi}/${team}`;
    //console.log(url);
    window.location = url;
}

function onChangeContent(id, text, team, year, kw) {
    const url = `/plan/set_content/${id}/${text}/${team}/${year}/${kw}`;
    window.location = url;
}

function onChangeSelect(team, year, kw) {
    const url = `/plan/${team}/${year}/${kw}`;
    window.location = url; 
}

function onChangeLehrplan(block, plan, team, year, kw) {
    const url = `/plan/set_lehrplan/${block}/${plan}/${team}/${year}/${kw}`;
    console.log(url);
    window.location = url;
}