# Setup and Deployment Guide

## Development Setup

### Quick Start

1. **Clone and Navigate**
   ```bash
   git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
   cd scaling-palm-tree
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set:
   - `SECRET_KEY`: Generate a secure random key
   - `DATABASE_URL`: Your database connection string
   - `FLASK_ENV`: Set to `development` for development

5. **Initialize Database**
   ```bash
   python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

6. **Run Development Server**
   ```bash
   python app.py
   ```
   
   Access at: http://localhost:5000

## Production Deployment

### Using Gunicorn (Recommended)

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

### Using uWSGI

1. **Install uWSGI**
   ```bash
   pip install uwsgi
   ```

2. **Create uWSGI config** (`uwsgi.ini`):
   ```ini
   [uwsgi]
   module = app:app
   master = true
   processes = 4
   socket = /tmp/legal-advocacy.sock
   chmod-socket = 660
   vacuum = true
   die-on-term = true
   ```

3. **Run uWSGI**
   ```bash
   uwsgi --ini uwsgi.ini
   ```

### Environment Variables for Production

```bash
SECRET_KEY=<your-secure-secret-key>
DATABASE_URL=postgresql://user:password@localhost/legal_advocacy
FLASK_ENV=production
```

### Database Migration

For production databases (PostgreSQL):

1. **Install psycopg2**
   ```bash
   pip install psycopg2-binary
   ```

2. **Update DATABASE_URL** in `.env`
   ```
   DATABASE_URL=postgresql://username:password@host:port/database
   ```

3. **Create tables**
   ```bash
   python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

## Nginx Configuration

Example Nginx configuration for reverse proxy:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/scaling-palm-tree/static;
    }
}
```

## SSL/TLS Configuration

Use Let's Encrypt for free SSL certificates:

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Monitoring and Logging

### Application Logging

Add to `app.py`:
```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

## Backup Strategy

### Database Backups

For SQLite:
```bash
cp legal_advocacy.db backups/legal_advocacy_$(date +%Y%m%d).db
```

For PostgreSQL:
```bash
pg_dump legal_advocacy > backups/legal_advocacy_$(date +%Y%m%d).sql
```

### Automated Backups

Add to crontab:
```bash
0 2 * * * /path/to/backup-script.sh
```

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find and kill process
   lsof -ti:5000 | xargs kill -9
   ```

2. **Database connection errors**
   - Check DATABASE_URL is correct
   - Ensure database server is running
   - Verify credentials

3. **Template not found errors**
   - Ensure templates/ directory exists
   - Check file names match route references

4. **Static files not loading**
   - Verify static/ directory structure
   - Check Nginx configuration for /static location

## Security Checklist

- [ ] Change SECRET_KEY to a strong random value
- [ ] Use HTTPS in production
- [ ] Keep dependencies updated
- [ ] Enable CSRF protection (already configured)
- [ ] Use environment variables for sensitive data
- [ ] Regular database backups
- [ ] Monitor application logs
- [ ] Implement rate limiting for API endpoints
- [ ] Regular security audits

## Performance Optimization

1. **Database Indexing**
   - Indexes are defined in models.py
   - Add more indexes based on query patterns

2. **Caching**
   - Consider Redis for session storage
   - Cache frequently accessed data

3. **Static Files**
   - Use CDN for static assets in production
   - Enable gzip compression

## Maintenance

### Regular Tasks

- Update dependencies monthly
- Review and rotate logs
- Monitor disk space
- Check for security updates
- Backup database regularly
- Review user feedback

### Updating Dependencies

```bash
pip list --outdated
pip install --upgrade package-name
pip freeze > requirements.txt
```
