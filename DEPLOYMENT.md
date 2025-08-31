# 🚀 Roomsy App - Render Deployment Guide

## 📋 Prerequisites

1. **GitHub Account**: Your code should be in a GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **PostgreSQL Database**: We'll create this on Render

## 🔧 Step-by-Step Deployment

### 1. Prepare Your GitHub Repository

Make sure your code is pushed to GitHub with these files:
- `requirements.txt`
- `render.yaml`
- `Procfile`
- `runtime.txt`
- All application code

### 2. Create PostgreSQL Database on Render

1. **Go to Render Dashboard**
2. **Click "New +" → "PostgreSQL"**
3. **Configure Database:**
   - **Name**: `roomsy-db`
   - **Database**: `roomsy_db`
   - **User**: `roomsy_user`
   - **Region**: Choose closest to you
   - **Plan**: Free (for testing)
4. **Click "Create Database"**
5. **Copy the connection string** (you'll need this later)

### 3. Deploy Your Web Service

1. **In Render Dashboard, click "New +" → "Web Service"**
2. **Connect your GitHub repository**
3. **Configure the service:**
   - **Name**: `roomsy-app`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
   - **Plan**: Free

### 4. Set Environment Variables

In your web service settings, add these environment variables:

```
FLASK_ENV=production
RENDER=true
DATABASE_URL=<your_postgresql_connection_string>
SECRET_KEY=<generate_a_secure_random_string>
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=chakradarreddy12@gmail.com
MAIL_EMAIL_PASSWORD=<your_email_password>
```

### 5. Deploy

1. **Click "Create Web Service"**
2. **Wait for build to complete** (usually 5-10 minutes)
3. **Your app will be available at**: `https://your-app-name.onrender.com`

## 🔐 Environment Variables Explained

| Variable | Description | Example |
|----------|-------------|---------|
| `FLASK_ENV` | Environment mode | `production` |
| `RENDER` | Indicates Render deployment | `true` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host:port/db` |
| `SECRET_KEY` | Flask secret key | `your-secure-random-string` |
| `MAIL_SERVER` | SMTP server | `smtp.gmail.com` |
| `MAIL_PORT` | SMTP port | `587` |
| `MAIL_USE_TLS` | Use TLS encryption | `true` |
| `MAIL_USERNAME` | Email username | `chakradarreddy12@gmail.com` |
| `MAIL_EMAIL_PASSWORD` | Email password | `your-app-password` |

## 🗄️ Database Setup

After deployment, you'll need to create the database tables:

1. **Access your app URL**
2. **The app will automatically create tables** on first run
3. **Or run the sample data script** to populate with test data

## 📱 Testing Your Deployed App

1. **Visit your app URL**
2. **Test user registration**
3. **Test apartment creation**
4. **Test booking functionality**
5. **Verify all features work**

## 🔍 Troubleshooting

### Common Issues:

1. **Build Fails**: Check `requirements.txt` and `runtime.txt`
2. **Database Connection Error**: Verify `DATABASE_URL` format
3. **App Won't Start**: Check `startCommand` in render.yaml
4. **CSRF Errors**: Ensure `SECRET_KEY` is set

### Debug Commands:

- Check build logs in Render dashboard
- Verify environment variables are set
- Test database connection locally

## 🚀 Post-Deployment

1. **Set up custom domain** (optional)
2. **Configure SSL certificates** (automatic on Render)
3. **Set up monitoring** and alerts
4. **Configure backups** for your database

## 📞 Support

For deployment issues:
- Check Render documentation
- Review build logs
- Verify environment variables
- Test locally first

## 🎉 Success!

Once deployed, your Roomsy app will be:
- ✅ **Live on the internet**
- ✅ **Accessible 24/7**
- ✅ **Automatically scaled**
- ✅ **SSL secured**
- ✅ **Database backed**

Your app will be available at: `https://your-app-name.onrender.com`
