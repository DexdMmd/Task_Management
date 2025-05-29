<template>
  <div class="task-manager">
    <div class="task-form">
      <h1>🗂️ Task Manager</h1>
      <form @submit.prevent="addTask">
        <input v-model="newTask.title" placeholder="Title *" required />
        <textarea v-model="newTask.description" placeholder="Description *" required></textarea>

        <label>Start Time:</label>
        <input type="datetime-local" v-model="newTask.start_time" required />

        <label>End Time:</label>
        <input type="datetime-local" v-model="newTask.end_time" required />

        <!-- Status Dropdown -->
        <label>Status:</label>
        <select v-model="newTask.status" required>
          <option value="to_do">To Do</option>
          <option value="in_progress">In Progress</option>
          <option value="done">Done</option>
        </select>

        <!-- Category Dropdown -->
        <label>Category:</label>
        <select v-model="newTask.category" required>
          <option value="work">Work</option>
          <option value="personal">Personal</option>
          <option value="urgent">Urgent</option>
        </select>

        <label>
          <input type="checkbox" v-model="newTask.completed" /> Completed
        </label>

        <input v-model="newTask.assigned_to" placeholder="Assigned Users / Groups (comma separated)" />

        <button type="submit">➕ Add Task</button>
      </form>
    </div>

    <div class="task-list">
      <ul>
        <li v-for="task in tasks" :key="task.id">
          <h3>{{ task.title }}</h3>
          <p>{{ task.description }}</p>
          <p><strong>Start:</strong> {{ task.start_time }} | <strong>End:</strong> {{ task.end_time }}</p>
          
          <!-- Show Status -->
          <p><strong>Status:</strong> {{ formatStatus(task.status) }}</p>
          
          <!-- Show Category -->
          <p><strong>Category:</strong> {{ formatCategory(task.category) }}</p>

          <p><strong>Completed:</strong> 
            <span class="status" :class="{ completed: task.completed, notcompleted: !task.completed }">
              {{ task.completed ? '✅ Yes' : '❌ No' }}
            </span>
          </p>

          <p><strong>Assigned to:</strong> {{ task.assigned_to }}</p>
          <button @click="deleteTask(task.id)">🗑️ Delete</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import apiClient from '../services/api';

export default {
  data() {
    return {
      tasks: [],
      newTask: {
        title: '',
        description: '',
        start_time: '',
        end_time: '',
        status: 'to_do',         // Default value
        category: 'work',        // Default value
        completed: false,
        assigned_to: '',
      },
    };
  },
  methods: {
    fetchTasks() {
      apiClient.get('tasks/')
        .then(response => {
          this.tasks = response.data;
        });
    },
    addTask() {
      apiClient.post('tasks/', this.newTask)
        .then(() => {
          this.newTask = {
            title: '',
            description: '',
            start_time: '',
            end_time: '',
            status: 'to_do',
            category: 'work',
            completed: false,
            assigned_to: '',
          };
          this.fetchTasks();
        });
    },
    deleteTask(id) {
      apiClient.delete(`tasks/${id}/`)
        .then(() => {
          this.fetchTasks();
        });
    },
    formatStatus(status) {
      return {
        to_do: '📌 To Do',
        in_progress: '🔄 In Progress',
        done: '✅ Done'
      }[status];
    },
    formatCategory(category) {
      return {
        work: '💼 Work',
        personal: '👤 Personal',
        urgent: '🔥 Urgent'
      }[category];
    }
  },
  mounted() {
    this.fetchTasks();
  },
};
</script>

<style scoped>
.task-manager {
  display: flex;
  justify-content: space-between;
  padding: 30px;
  gap: 30px;
  font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #000000, #1e3a8a, #ec4899);
  min-height: 70vh;
  color: #fff;
  border-radius: 20px;
}
.task-form, .task-list {
  width: 48%;
  background-color: rgba(255, 255, 255, 0.05);
  padding: 40px;
  border-radius: 30px;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s, box-shadow 0.3s;
}
.task-form:hover, .task-list:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
.task-form h1 {
  text-align: center;
  margin-bottom: 20px;
}
.task-form form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.task-form input,
.task-form textarea,
.task-form select {
  padding: 12px;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
}
.task-form button {
  padding: 12px;
  background-color: #10b981;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-weight: bold;
  font-size: 1rem;
  transition: background-color 0.3s, transform 0.2s;
}
.task-form button:hover {
  background-color: #059669;
  transform: scale(1.05);
}
.task-list ul {
  list-style: none;
  padding: 0;
}
.task-list li {
  background: rgba(255, 255, 255, 0.1);
  margin-bottom: 15px;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s, transform 0.2s;
}
.task-list li:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  transform: translateY(-3px);
}
.status.completed {
  color: #22c55e;
}
.status.notcompleted {
  color: #ef4444;
}
</style>