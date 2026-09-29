#!/bin/bash
set -e

GH_USER="ram133"
REPO_NAME="digital_factory"

if command -v gh &> /dev/null; then
    gh repo create "$GH_USER/$REPO_NAME" --public --confirm 2>/dev/null || true
fi

git init
git checkout -b main 2>/dev/null || git checkout main
git remote add origin "https://github.com/$GH_USER/$REPO_NAME.git" 2>/dev/null || git remote set-url origin "https://github.com/$GH_USER/$REPO_NAME.git"

cat << 'GITIGNORE' > .gitignore
venv/
__pycache__/
*.pyc
.DS_Store
GITIGNORE

git add .
git commit -m "Initialize Digital Factory core with GitHub Actions daily automation" || echo "No changes to commit"
git push -u origin main

echo "Repository deployed to GitHub. Cloud Actions active."
