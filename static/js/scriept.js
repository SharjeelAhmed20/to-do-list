document.getElementById('addBtn').addEventListener('click', function(e) {
    e.preventDefault();

    var taskInput = document.getElementById('taskInput');
    if (taskInput.value.trim() !== '') {
        var taskList = document.querySelector('.list-group');
        var newTask = document.createElement('li');

        newTask.innerHTML = `
            <span>${taskInput.value}</span>
            <div>
                <button class="btn btn-success" onclick="completeTask(this)">✔ Complete</button>
                <button class="btn btn-danger" onclick="deleteTask(this)">❌ Delete</button>
            </div>
        `;

        taskList.appendChild(newTask);
        taskInput.value = '';

        // Flash success message
        var alert = document.querySelector('.alert');
        alert.style.display = 'block';
        setTimeout(() => alert.style.display = 'none', 2000);
    }
});

function completeTask(button) {
    var task = button.parentElement.parentElement;
    task.querySelector('span').classList.toggle('text-decoration-line-through');
}

function deleteTask(button) {
    var task = button.parentElement.parentElement;
    task.remove();
}
