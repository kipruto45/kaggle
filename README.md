# KaggleKE MVP

A Kenya-only Kaggle-like platform for data science competitions, dataset sharing, and collaboration.

## Tech Stack
- Python, Django (HTML templates)
- PostgreSQL
- M-Pesa integration for prize payouts
- Mobile-friendly, lightweight design

## Features
- User registration/login (email/phone, Kenya-only)
- Dataset hosting (Kenya-relevant datasets)
- Competitions (host, join, submit solutions)
- Leaderboard (auto-scoring)
- Collaboration (discussion board, notebook/code sharing)
- M-Pesa payouts

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Configure PostgreSQL in `kaggleke/settings.py`.
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the server:
   ```sh
   python manage.py runserver
   ```

## Legal
- All datasets must comply with Kenya's Data Protection Act.
- See `terms.md` and `privacy.md` for details.
# kaggle
