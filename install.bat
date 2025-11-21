@echo off
REM IPTrack Windows Installation Script (Batch)
REM Run with: install.bat

echo ========================================
echo    IPTrack Security Monitor Installer
echo         Windows Version v1.0
echo ========================================
echo.

REM Check if running as Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo WARNING: Not running as Administrator
    echo Some features (Windows Firewall) require admin privileges
    echo.
    set /p continue="Continue anyway? (y/n): "
    if /i not "%continue%"=="y" exit /b
)

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    pause
    exit /b 1
)
echo Python found!

REM Check pip
echo Checking pip...
pip --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: pip not found!
    pause
    exit /b 1
)
echo pip found!

REM Install dependencies
echo.
echo Installing dependencies...
pip install requests --upgrade

REM Create logs directory
echo.
echo Creating logs directory...
if not exist "logs" mkdir logs
echo Logs directory created!

REM Install IPTrack package
echo.
echo Installing IPTrack...
pip install --user -e .

REM Create configuration file
echo.
echo Creating default configuration...
if not exist "config.json" (
    echo { > config.json
    echo   "max_attempts": 3, >> config.json
    echo   "block_duration_minutes": 60, >> config.json
    echo   "monitor_auth_log": true, >> config.json
    echo   "auto_block": true, >> config.json
    echo   "alert_email": null, >> config.json
    echo   "whitelist_ips": ["127.0.0.1", "::1"], >> config.json
    echo   "geolocation_enabled": true, >> config.json
    echo   "log_retention_days": 30 >> config.json
    echo } >> config.json
    echo Configuration file created!
) else (
    echo Configuration file already exists
)

REM Display important information
echo.
echo ========================================
echo         IMPORTANT INFORMATION
echo ========================================
echo.
echo Windows Firewall Integration:
echo   * IPTrack requires Administrator privileges to block IPs
echo   * Run your terminal as Administrator when blocking
echo   * Or use 'runas' command for specific operations
echo.

REM Installation complete
echo ========================================
echo    Installation Complete!
echo ========================================
echo.
echo Quick Start:
echo    iptrack --help                   # Show all commands
echo    iptrack watch                    # Monitor logs in real-time
echo    iptrack block [ip]              # Block an IP address
echo    iptrack unblock [ip]            # Unblock an IP address
echo    iptrack list                    # Show blocked IPs
echo    iptrack locate [ip]             # Find IP location
echo    iptrack dashboard               # View security dashboard
echo.
echo Documentation:
echo    README.md                        # Complete documentation
echo    QUICK_REFERENCE.md              # Command reference
echo.
echo Remember: Restart your terminal to use 'iptrack' command!
echo.
pause
