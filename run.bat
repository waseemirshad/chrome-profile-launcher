@echo off
title Chrome Profile Launcher
echo.
echo ==============================
echo   Chrome Profile Launcher
echo ==============================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python install nahi hai!
    echo Python yahan se download karein: https://python.org
    pause
    exit /b 1
)

:: Run the app
echo Starting...
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] App crash ho gayi. Upar error check karein.
    pause
)
