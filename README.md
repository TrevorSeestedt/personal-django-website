# Personal Website

A modern, responsive personal website built with Django that features a clean design, dark mode support, and smooth transitions.

## Features

- Simplistic UI design
- Dark/Light mode toggle
- Responsive layout
- Page transitions
- Project showcase section
- About me section
- Resume section
- Contact section
- Social media integration (GitHub, LinkedIn)

## Tech Stack

- **Backend**: Django 5.1.5
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Deployment**: Heroku-ready

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd mywebsite
```

2. Create and activate a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`
