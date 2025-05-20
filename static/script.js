$(document).ready(function(){
    // simplified the namespace of the io obj
    const socket = io("/test");

    socket.on("a_new_message", function(msg) {
        $("#log").append(`<p>Received: ${msg.data}</p>`)
    });

    $('form#message').on('submit', function(e){
        // prevent the typical form stuff from happening
        e.preventDefault();
        
        // Emitting a message FROM the Client
        socket.emit("form_submitted", { data: $('#message_data').val() });

        // reset form
        document.getElementById("message").reset();
    });
});