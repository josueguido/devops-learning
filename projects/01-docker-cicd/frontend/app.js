const API_URL = "http://localhost:8000/api";

const statusElement = document.querySelector("#status");
const messageElement = document.querySelector("#message");
const tasksElement = document.querySelector("#tasks");
const form = document.querySelector("#task-form");

async function request(path, options) {
  const response = await fetch(`${API_URL}${path}`, options);
  const body = await response.json();
  if (!response.ok) {
    throw new Error(body.error || `Request failed with status ${response.status}`);
  }
  return body;
}

async function loadTasks() {
  const tasks = await request("/tasks");
  tasksElement.replaceChildren();
  for (const task of tasks) {
    const item = document.createElement("li");
    item.textContent = task.title;
    tasksElement.append(item);
  }
}

async function checkHealth() {
  try {
    const health = await request("/health");
    statusElement.textContent = `API: ${health.status} · PostgreSQL: ${health.database}`;
    statusElement.dataset.state = "ok";
  } catch (error) {
    statusElement.textContent = `No se pudo conectar: ${error.message}`;
    statusElement.dataset.state = "error";
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const input = form.elements.title;
  messageElement.textContent = "";
  try {
    await request("/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: input.value }),
    });
    input.value = "";
    await loadTasks();
  } catch (error) {
    messageElement.textContent = `No se pudo guardar la tarea: ${error.message}`;
  }
});

checkHealth();
loadTasks().catch((error) => {
  messageElement.textContent = `No se pudieron cargar las tareas: ${error.message}`;
});
