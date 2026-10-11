# Update IT — Educational Institute Management System

A Django-based platform for running an educational institute. It brings students, faculty, attendance, academics, fees, payroll, notices, admissions, achievements, galleries, and everyday administration together in a single central dashboard.

## Features

### Student Management
- Student profiles and academic history
- Class and batch organization
- Guardian contact details
- Admission records

### Attendance
- Daily attendance for students
- Attendance management for faculty
- Present, Absent, and Late statuses
- Summaries and reports

### Faculty Management
- Faculty profiles
- Subject assignments
- Class schedules
- Faculty activity overview

### Teacher Salaries
- Monthly payroll processing
- Deductions based on attendance
- Pay calculated per class taken
- Bonuses and manual deductions
- Printable salary slips

### Student Payments
- Monthly fee collection
- Admission and exam fees
- Printable receipts
- Several payment methods

### Academics
- Classes and batches
- Subjects and academic years
- Exam setup
- Result entry and grading

### Result Portal
- Students look up their own results
- Attendance summary
- Access protected by Student ID and registered phone number

### Admissions
- Inquiry handling
- Online admission information
- Application tracking and verification

### Notices and Achievements
- Publishing notices
- Showcasing achievements
- Public announcement pages

### Gallery
- Photo gallery with sections and subsections
- Media organized by event or category

### Contact
- Public contact form
- Message management

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Django 5.2 |
| Language | Python |
| Database | PostgreSQL |
| Cloud Database | Supabase |
| Frontend | HTML, CSS, JavaScript, Django Templates |
| Web Server | Gunicorn |
| Static Files | WhiteNoise |
| Media Storage | Supabase Storage / S3-compatible storage |
| Cache | Redis |
| PDF Generation | ReportLab |
| Excel Support | openpyxl |

## Project Structure

```text
Update_IT/
├── config/
├── core/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── Procfile
└── start.sh
```

## Installation

### Get the Code

```bash
git clone https://github.com/<your-username>/Update_IT.git
cd Update_IT
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate It

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the Database

The application tables are not managed by Django. Run `update_it_supabase_schema.sql` once in the Supabase SQL Editor, then create Django's own tables:

```bash
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

## Environment Variables

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=your-host
DB_PORT=5432
REDIS_URL=redis://localhost:6379/1
CSRF_TRUSTED_ORIGINS=https://your-domain.example
AWS_STORAGE_BUCKET_NAME=update-it-media
```

## Security

- Django authentication
- CSRF protection
- Secure cookies
- HTTPS support
- Secrets kept in environment variables
- Rate limiting
- Redis caching

## Deployment

Works on platforms such as:

- Render
- Railway
- A VPS
- Docker-compatible environments

Production server:

```bash
gunicorn config.wsgi
```

## Main Modules

- Student Management
- Faculty Management
- Attendance Management
- Teacher Salary System
- Payment Management
- Exam & Result Management
- Admissions
- Notices
- Achievements
- Gallery
- Contact System

## Developer

**Rafsan Hasan Pronay**

GitHub: https://github.com/rafsanhasanpronoy

## License

This project is maintained as an institute management solution. Add an open-source license if you plan to share or redistribute it.
