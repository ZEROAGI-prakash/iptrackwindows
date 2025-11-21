# IPTrack Windows Installation Script (PowerShell)
# Run with: powershell -ExecutionPolicy Bypass -File install.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   IPTrack Security Monitor Installer  " -ForegroundColor Cyan
Write-Host "        Windows Version v1.0           " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "⚠️  WARNING: Not running as Administrator" -ForegroundColor Yellow
    Write-Host "Some features (Windows Firewall) require admin privileges" -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne 'y') {
        exit
    }
}

# Check Python installation
Write-Host "🔍 Checking Python installation..." -ForegroundColor Green
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found!" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ from https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Check pip
Write-Host "🔍 Checking pip..." -ForegroundColor Green
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✅ Found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ pip not found!" -ForegroundColor Red
    exit 1
}

# Install dependencies
Write-Host ""
Write-Host "📦 Installing dependencies..." -ForegroundColor Green
pip install requests --upgrade

# Create logs directory
Write-Host ""
Write-Host "📁 Creating logs directory..." -ForegroundColor Green
New-Item -ItemType Directory -Force -Path "logs" | Out-Null
Write-Host "✅ Logs directory created" -ForegroundColor Green

# Install IPTrack package
Write-Host ""
Write-Host "📦 Installing IPTrack..." -ForegroundColor Green
pip install --user -e .

# Get Python Scripts directory
$pythonScripts = python -c "import sysconfig; print(sysconfig.get_path('scripts'))"
Write-Host "Python Scripts directory: $pythonScripts" -ForegroundColor Cyan

# Add to PATH if not already there
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($currentPath -notlike "*$pythonScripts*") {
    Write-Host ""
    Write-Host "🔧 Adding to PATH..." -ForegroundColor Green
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$currentPath;$pythonScripts",
        "User"
    )
    Write-Host "✅ Added to PATH: $pythonScripts" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠️  Please restart your terminal for PATH changes to take effect" -ForegroundColor Yellow
} else {
    Write-Host "✅ Python Scripts already in PATH" -ForegroundColor Green
}

# Create configuration file
Write-Host ""
Write-Host "⚙️  Creating default configuration..." -ForegroundColor Green
if (-not (Test-Path "config.json")) {
    $config = @{
        max_attempts = 3
        block_duration_minutes = 60
        monitor_auth_log = $true
        auto_block = $true
        alert_email = $null
        whitelist_ips = @("127.0.0.1", "::1")
        geolocation_enabled = $true
        log_retention_days = 30
    } | ConvertTo-Json -Depth 10
    
    Set-Content -Path "config.json" -Value $config
    Write-Host "✅ Configuration file created" -ForegroundColor Green
} else {
    Write-Host "ℹ️  Configuration file already exists" -ForegroundColor Cyan
}

# Display firewall permissions notice
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "        IMPORTANT INFORMATION           " -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🛡️  Windows Firewall Integration:" -ForegroundColor Yellow
Write-Host "   • IPTrack requires Administrator privileges to block IPs" -ForegroundColor White
Write-Host "   • Run your terminal as Administrator when blocking" -ForegroundColor White
Write-Host "   • Or use 'runas' command for specific operations" -ForegroundColor White
Write-Host ""

# Installation complete
Write-Host "========================================" -ForegroundColor Green
Write-Host "   ✅ Installation Complete!            " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Quick Start:" -ForegroundColor Cyan
Write-Host "   iptrack --help                   # Show all commands" -ForegroundColor White
Write-Host "   iptrack watch                    # Monitor logs in real-time" -ForegroundColor White
Write-Host "   iptrack block <ip>              # Block an IP address" -ForegroundColor White
Write-Host "   iptrack unblock <ip>            # Unblock an IP address" -ForegroundColor White
Write-Host "   iptrack list                    # Show blocked IPs" -ForegroundColor White
Write-Host "   iptrack locate <ip>             # Find IP location" -ForegroundColor White
Write-Host "   iptrack dashboard               # View security dashboard" -ForegroundColor White
Write-Host ""
Write-Host "📚 Documentation:" -ForegroundColor Cyan
Write-Host "   README.md                        # Complete documentation" -ForegroundColor White
Write-Host "   QUICK_REFERENCE.md              # Command reference" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  Remember: Restart your terminal to use 'iptrack' command!" -ForegroundColor Yellow
Write-Host ""
