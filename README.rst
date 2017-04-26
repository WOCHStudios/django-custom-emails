=====
Django Custom Emails
=====

This is a simple django app to send emails through the django admin console.


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'emails',
    ]

2. Run `python manage.py migrate` to create the emails models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a email (you'll need the Admin app enabled).
