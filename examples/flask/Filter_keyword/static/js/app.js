var socket;
itemList = []

$(document).ready(function () {
    socket = io();

    // When web opened, build socket io with python server
    socket.emit('login', {'login_id':'Tung'});
    
    // When web opened, build socket io with python server
    socket.emit('get_msg_fromPython');

    // when python emit 'get_goods', will do this function
    socket.on('show_msg', function (msg, cb) {
        show_msg(msg)
        RefreshMsgDiv(itemList)
    })

});

function show_msg(msg){
    itemList = msg
}

function RefreshMsgDiv(itemList){
    document.getElementById('msg_div').innerHTML = 
    `
    ${itemList.map((item)=>(
        `
        <div>
            <p>key ${item.key},  value ${item.value}</p>
        </div>
        `
    )).join('')}
    `
    ;
}

function FilterItem(query){
    const queryList = query.split(',').filter(q=>q!='');
    if(queryList.length!==0){
        console.log('[FilterItem] ',queryList);
        const FiltedItemList = itemList.filter((item)=>{
            for (let i=0; i<queryList.length; i++){
                if(item.key.toLowerCase().includes(queryList[i].toLowerCase())){
                    return true;
                }
                else if(item.value.toLowerCase().includes(queryList[i].toLowerCase())){
                    return true;
                }
            }
            return false;
        });

        RefreshMsgDiv(FiltedItemList);
    }
    else{
        RefreshMsgDiv(itemList);
    }
}





