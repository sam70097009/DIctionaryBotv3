// Scroll to the bottom of the chat window
function scrollChatWindowToBottom() {
    var chatWindow = document.querySelector('.chat-window');
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Execute when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    scrollChatWindowToBottom();
});

// Scroll to the bottom when a new message is added
function handleNewMessage() {
    scrollChatWindowToBottom();
}

// Execute when the window is resized
window.addEventListener('resize', function() {
    scrollChatWindowToBottom();
});

function selectChoice(choice) {
    document.getElementById("msg_input").value = choice;
    document.getElementById("send_button").click();
}


