@echo off
echo ======================================================
echo   Syncing System Design Roadmap to GitHub...
echo ======================================================

echo [1/3] Updating README and Progress SVG from Excel...
python generate_readme.py

echo [2/3] Adding changes to Git...
git add .

echo [3/3] Committing and Pushing to GitHub...
git commit -m "Update System Design progress in Excel and README"
git push origin main

echo.
echo ======================================================
echo   System Design sync completed successfully!
echo ======================================================
pause
