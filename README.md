# 🏋️ سیستم مدیریت باشگاه ورزشی

یه وب‌اپلیکیشن کامل برای مدیریت باشگاه ورزشی، ساخته‌شده با Django.

---

## ✨ قابلیت‌ها

- 🔐 ثبت‌نام، ورود، و خروج کاربران
- 👤 پروفایل کاربری و ویرایش آن
- 📋 مدیریت دوره‌های ورزشی (CRUD)
- 📝 ثبت‌نام در دوره‌ها
- 🎫 سیستم پشتیبانی (تیکت و پاسخ)
- 🔍 جستجو در دوره‌ها
- 📄 صفحه‌بندی
- 📅 تاریخ شمسی
- 🛡️ محدودیت دسترسی بر اساس نقش (مدیر / کاربر)
- 🔗 API با Django REST Framework

---

## 🛠️ تکنولوژی‌ها

- **Backend:** Python, Django
- **API:** Django REST Framework
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap 5
- **تاریخ شمسی:** django-jalali

---

## 🚀 نصب و اجرا
```
۱. git clone URL
۲. python -m venv venv
۳. venv\Scripts\activate (ویندوز)
۴. pip install django djangorestframework django-jalali
۵. python manage.py makemigrations
۶. python manage.py migrate
۷. python manage.py createsuperuser
۸. python manage.py runserver
۹. برو به: http://127.0.0.1:8000/courses/

```
---

## 📂 ساختار پروژه

```
gym-management/
├── core/              # تنظیمات اصلی
├── members/           # مدیریت اعضا، دوره‌ها، تیکت‌ها
├── accounts/          # ورود و ثبت‌نام
└── templates/         # قالب‌های HTML
```

---

## 🔗 API

| آدرس | توضیح |
|------|-------|
| `/api/courses/` | لیست دوره‌ها |
| `/api/courses/<id>/` | جزئیات یک دوره |

---

## 👨‍💻 نویسنده

**Mohammad Babaei**  
[GitHub](https://github.com/mohammadbabaei04)

---

## 📄 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.