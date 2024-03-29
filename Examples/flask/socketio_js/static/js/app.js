var socket;

$(document).ready(function () {
    socket = io();

    // When web opened, build socket io with python server
    socket.emit('login', {'login_id':'Tung'});
    
    // when python emit 'show_log', will do this function
    socket.on('show_msg', function (msg, cb) {
        show_msg(msg)
    })
});

function js_to_python(){
    let key = document.getElementById("key").value;
    key = key.replace(/\s+/g, '');
    console.log('[input key] ',key);

    // call python function 'js_to_python' with argument key
    socket.emit('js_to_python',key)
}

function show_msg(msg){
    console.log('[show_msg] ',msg);
    // insert msg into html, id='msg_div_1'
    document.getElementById('msg_div_1').insertAdjacentHTML('beforeend',
    `
    <h3 class="form-text text-muted"> Return key: ${msg}</h3>
    `
    );

    const msg_list = ['123','234']
    // using map() to insert something into html, id='msg_div_2'
    document.getElementById('msg_div_2').insertAdjacentHTML('beforeend',
    `
    ${msg_list.map(map_list).join('')}
    `
    );
}

function map_list(currElement, idx){
    return `<p class="form-text text-muted"> Index-${idx} ${currElement}</p>`
}





