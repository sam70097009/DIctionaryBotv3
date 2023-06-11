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
  }
  
  // Execute when the window is resized
  window.addEventListener('resize', function() {
    scrollChatWindowToBottom();
  });
  