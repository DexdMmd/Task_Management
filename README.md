Task Management App 🤔
Overview
The Task Management App is a simple web application built using Django and Python for the backend, with a Vue.js frontend. It allows users to create, read, update, and delete tasks efficiently with a user-friendly interface.

Features
User-friendly interface for managing tasks

Create, read, update, and delete tasks (CRUD operations)

Admin panel for task management

REST API powered by Django REST Framework

Vue.js frontend for reactive task management

Task status tracking (completed or not)

Responsive design with modern UI/UX

Technologies Used
Python 3.8+

Django 3.0+

Django REST Framework

SQLite (default database)

Vue.js 3

Axios (for API requests)

HTML5, CSS3 with modern styling

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/DexdMmd/Task_Management.git
cd Task_Management
Create and activate a virtual environment:

On Windows:

bash
Copy
Edit
python -m venv env
env\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
python -m venv env
source env/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser for admin access:

bash
Copy
Edit
python manage.py createsuperuser
Run the backend server:

bash
Copy
Edit
python manage.py runserver
Set up and run the Vue frontend (in a separate directory):

bash
Copy
Edit
git clone https://github.com/DexdMmd/task-manager-frontend.git
cd task-manager-frontend
npm install
npm run dev
Usage
Access the Django backend API at http://127.0.0.1:8000/

Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage tasks directly

Access the Vue.js frontend at http://localhost:5173 to interact with tasks in a modern UI

Use the task form to add new tasks, mark completed, and delete tasks

All task data is synced via the Django REST API

GitHub Branch Info
The main branch holds the backend Django code.

The vue-integration branch contains the Vue.js frontend integration.

Make sure to pull or switch branches appropriately:

bash
Copy
Edit
git checkout vue-integration
فارسی — معرفی برنامه مدیریت وظایف
معرفی
برنامه مدیریت وظایف یک برنامه وب ساده است که با استفاده از Django و Python برای بک‌اند و Vue.js برای فرانت‌اند ساخته شده است. کاربران می‌توانند وظایف خود را ایجاد، مشاهده، به‌روزرسانی و حذف کنند.

ویژگی‌ها
رابط کاربری آسان برای مدیریت وظایف

عملیات CRUD روی وظایف

پنل مدیریت ادمین

API قدرتمند با Django REST Framework

رابط کاربری مدرن با Vue.js

امکان پیگیری وضعیت انجام وظایف

فناوری‌های استفاده شده
Python 3.8+

Django 3.0+

Django REST Framework

SQLite

Vue.js 3

Axios

نصب
کلون کردن مخزن:

bash
Copy
Edit
git clone https://github.com/DexdMmd/Task_Management.git
cd Task_Management
ایجاد و فعال‌سازی محیط مجازی:

در ویندوز:

bash
Copy
Edit
python -m venv env
env\Scripts\activate
در مک/لینوکس:

bash
Copy
Edit
python -m venv env
source env/bin/activate
نصب بسته‌ها:

bash
Copy
Edit
pip install -r requirements.txt
اجرای مهاجرت‌ها:

bash
Copy
Edit
python manage.py migrate
ایجاد کاربر ادمین:

bash
Copy
Edit
python manage.py createsuperuser
اجرای سرور:

bash
Copy
Edit
python manage.py runserver
اجرای فرانت‌اند Vue (در پوشه جداگانه):

bash
Copy
Edit
git clone https://github.com/DexdMmd/task-manager-frontend.git
cd task-manager-frontend
npm install
npm run dev
استفاده
دسترسی به API در http://127.0.0.1:8000/

پنل مدیریت در http://127.0.0.1:8000/admin/

رابط کاربری Vue در http://localhost:5173

