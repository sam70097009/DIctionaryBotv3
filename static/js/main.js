// Scroll to the bottom of the chat window
function scrollChatWindowToBottom() {
    var chatWindow = document.querySelector('.chat-window');
    var lastMessage = chatWindow.lastElementChild;
    lastMessage.scrollIntoView();
}

// Execute when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    scrollChatWindowToBottom();
});

// Scroll to the bottom when a new message is added
function handleNewMessage() {
    scrollChatWindowToBottom();
    document.getElementById('word').focus(); // Keep the input field focused

    // Add animation to the latest messages
    var messages = document.querySelectorAll('.message');
    var latestMessages = Array.from(messages).slice(-2); // Change the number to specify the number of latest messages to animate

    latestMessages.forEach(function(message) {
        message.classList.add('animated'); // Add your animation class here
    });
}

// Execute when the window is resized
window.addEventListener('resize', function() {
    scrollChatWindowToBottom();
});

// Call the handleNewMessage function on page load to apply the animation to the initial messages
handleNewMessage();
