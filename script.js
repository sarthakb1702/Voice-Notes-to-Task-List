const startBtn = document.getElementById('start-btn');
const todoList = document.getElementById('todo-list');

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.lang = 'en-US';

startBtn.addEventListener('click', () => {
  recognition.start();
});

recognition.onresult = (event) => {
  const transcript = event.results[0][0].transcript;
  addTask(transcript);
};

function addTask(taskText) {
  const li = document.createElement('li');
  li.textContent = taskText;
  li.addEventListener('click', () => {
    li.classList.toggle('completed');
  });
  todoList.appendChild(li);
}

recognition.onerror = (event) => {
  alert(`Error occurred in recognition: ${event.error}`);
};
