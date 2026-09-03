@echo off
echo ======================================================
echo   Syncing System Design Roadmap to GitHub...
echo ======================================================

echo [1/4] Pulling latest updates from GitHub (e.g. mobile edits)...
git pull origin main

echo [2/4] Updating README and Progress SVG (two-way sync with Excel)...
python generate_readme.py

echo [3/4] Adding changes to Git...
git add .

echo [4/4] Committing and Pushing to GitHub...
git commit -m "Update System Design progress in Excel and README"
git push origin main

echo.
echo ======================================================
echo   System Design sync completed successfully!
echo ======================================================
pause
