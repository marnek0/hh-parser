@echo off
chcp 65001 >nul
title HH Parser

:: Проверяем наличие Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ============================================
    echo  Python не найден!
    echo  Скачай и установи Python 3.11 отсюда:
    echo  https://www.python.org/downloads/
    echo  При установке поставь галочку:
    echo  "Add Python to PATH"
    echo ============================================
    pause
    exit /b 1
)

:: Папка для виртуального окружения рядом со скриптом
set VENV_DIR=%~dp0venv

:: Создаём виртуальное окружение при первом запуске
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo ============================================
    echo  Первый запуск — установка зависимостей...
    echo  Это займёт 3-5 минут. Больше не повторится.
    echo ============================================
    python -m venv "%VENV_DIR%"
    call "%VENV_DIR%\Scripts\activate.bat"
    python -m pip install --upgrade pip --quiet
    pip install gradio playwright openpyxl --quiet
    playwright install chromium
    echo ============================================
    echo  Установка завершена!
    echo ============================================
) else (
    call "%VENV_DIR%\Scripts\activate.bat"
)

:: Запускаем парсер
echo Запускаю HH Parser...
start "" http://localhost:7860
python "%~dp0hh_gradio.py"

pause
