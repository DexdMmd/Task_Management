
# Task Management App 🤔

## Overview
The Task Management App is a simple web application built using Django and Python. It allows users to create, read, update, and delete tasks. This branch integrates a Vue.js frontend for a more dynamic user experience.

## Features
- User-friendly interface for managing tasks
- Create, read, update, and delete tasks (CRUD operations)
- Admin panel for managing tasks
- Vue.js frontend integration with Axios for API calls

## Technologies Used
- 🐍 Python 3.8 or newer
- Django 3.0 or newer
- SQLite (default database)
- Django REST Framework for API functionality
- Vue.js 3 for frontend
- Axios for HTTP requests

## Installation

1. Clone the repository and switch to this branch:
   ```bash
   git clone https://github.com/DexdMmd/Task_Management.git
   cd Task_Management
   git checkout vue-integration
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

8. In a separate directory, set up the Vue.js frontend:
   ```bash
   npm create vite@latest task-manager-frontend -- --template vue
   cd task-manager-frontend
   npm install
   npm run dev
   ```

## Usage
- Access the Django backend API at `http://127.0.0.1:8000/`
- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Access the Vue.js frontend at `http://localhost:5173`
- Use the frontend to manage tasks with live updates via API calls.

---

# برنامه مدیریت وظایف

## معرفی
برنامه مدیریت وظایف یک برنامه وب ساده است که با استفاده از Django و Python ساخته شده است. این نسخه شامل یک فرانت‌اند Vue.js برای تجربه کاربری بهتر است.

### ویژگی‌ها
- رابط کاربری آسان برای مدیریت وظایف
- ایجاد، خواندن، به‌روزرسانی و حذف وظایف (عملیات CRUD)
- پنل مدیریت برای مدیریت وظایف
- ادغام Vue.js و استفاده از Axios برای ارتباط با API

## فناوری‌های مورد استفاده
- Python 3.8 یا جدیدتر
- Django 3.0 یا جدیدتر
- SQLite (پایگاه داده پیش‌فرض)
- Django REST Framework برای عملکرد API
- Vue.js 3 برای فرانت‌اند
- Axios برای ارسال درخواست‌های HTTP

## نصب

1. مخزن را کلون کرده و به این شاخه بروید:
   ```bash
   git clone https://github.com/DexdMmd/Task_Management.git
   cd Task_Management
   git checkout vue-integration
   ```

2. یک محیط مجازی ایجاد کنید:
   ```bash
   python -m venv env
   ```

3. محیط مجازی را فعال کنید:
   - در ویندوز:
     ```bash
     env\Scripts\activate
     ```
   - در macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. بسته‌های مورد نیاز را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```

5. تغییرات را اعمال کنید:
   ```bash
   python manage.py migrate
   ```

6. یک کاربر ادمین ایجاد کنید:
   ```bash
   python manage.py createsuperuser
   ```

7. سرور توسعه Django را اجرا کنید:
   ```bash
   python manage.py runserver
   ```

8. در دایرکتوری جداگانه، فرانت‌اند Vue.js را راه‌اندازی کنید:
   ```bash
   npm create vite@latest task-manager-frontend -- --template vue
   cd task-manager-frontend
   npm install
   npm run dev
   ```
## استفاده
- دسترسی به پنل مدیریت در `http://127.0.0.1:8000/admin/`
- دسترسی به فرانت‌اند Vue.js در `http://localhost:5173`
- از فرانت‌اند برای مدیریت وظایف با به‌روزرسانی‌های زنده از طریق تماس‌های API استفاده کنید.

---
