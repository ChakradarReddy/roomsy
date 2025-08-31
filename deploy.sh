#!/bin/bash

echo "🚀 Roomsy App - Render Deployment Preparation"
echo "=============================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found!"
    echo "Please initialize git and push your code to GitHub first."
    echo ""
    echo "Commands to run:"
    echo "  git init"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
    echo "  git remote add origin <your-github-repo-url>"
    echo "  git push -u origin main"
    exit 1
fi

echo "✅ Git repository found"
echo ""

# Check if all required files exist
echo "📋 Checking deployment files..."
required_files=("requirements.txt" "render.yaml" "Procfile" "runtime.txt")

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file (missing)"
    fi
done

echo ""
echo "🔧 Next Steps:"
echo "1. Push your code to GitHub:"
echo "   git add ."
echo "   git commit -m 'Prepare for Render deployment'"
echo "   git push"
echo ""
echo "2. Go to [render.com](https://render.com) and:"
echo "   - Create a PostgreSQL database"
echo "   - Deploy your web service"
echo "   - Set environment variables"
echo ""
echo "3. Follow the detailed guide in DEPLOYMENT.md"
echo ""
echo "🎯 Your app will be live at: https://your-app-name.onrender.com"
