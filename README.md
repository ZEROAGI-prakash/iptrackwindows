# 🛡️ IPTrack - Windows Edition

Professional Security Monitoring & IP Management Tool for Windows

**Track. Block. Defend. - Your Windows Security Guardian**

## 🌟 What is IPTrack?

IPTrack is a powerful, Gemini-style command-line security tool designed specifically for Windows. It monitors unauthorized access attempts, automatically blocks suspicious IPs using Windows Firewall, and provides real-time geolocation tracking.

### ✨ Key Features

- 🔒 **Automatic IP Blocking** - Uses Windows Firewall (netsh) to block malicious IPs
- 🌍 **IP Geolocation** - Track attacker locations with city, country, ISP details
- 📊 **Real-time Monitoring** - Watch security logs as they happen
- 🎯 **Smart Auto-Block** - Blocks after 3 failed attempts (configurable)
- 🔄 **Easy Unblock** - Reverse blocks with a single command
- 📈 **Security Dashboard** - Visual overview of all security events
- 💾 **Export Logs** - Save all security data to JSON
- 🎨 **Beautiful CLI** - Gemini-style interface with colors and formatting

## 📋 Requirements

- **Windows 10/11** or Windows Server 2016+
- **Python 3.7+** - Download from [python.org](https://www.python.org/downloads/)
- **Administrator Privileges** - Required for blocking/unblocking IPs
- **Internet Connection** - For IP geolocation features

## 🚀 Quick Installation

### PowerShell (Recommended)

Right-click PowerShell and select "Run as Administrator", then:

\`\`\`powershell
cd path\to\iptrack-windows
powershell -ExecutionPolicy Bypass -File install.ps1
\`\`\`

### Command Prompt

Right-click CMD and select "Run as Administrator", then:

\`\`\`cmd
cd path\to\iptrack-windows
install.bat
\`\`\`

## 💻 Usage

\`\`\`powershell
iptrack --help                  # Show all commands
iptrack watch                   # Monitor logs in real-time
iptrack block 192.168.1.100     # Block an IP
iptrack unblock 192.168.1.100   # Unblock an IP
iptrack list                    # List blocked IPs
iptrack locate 8.8.8.8          # Find IP location
iptrack stats                   # Show statistics
iptrack dashboard               # Security dashboard
iptrack export                  # Export logs
\`\`\`

## 🔐 Windows Firewall Integration

IPTrack uses `netsh advfirewall firewall` commands to block IPs.

### When Blocking:
\`\`\`powershell
netsh advfirewall firewall add rule name="IPTrack_Block_IP" dir=in action=block remoteip=192.168.1.100
\`\`\`

### When Unblocking:
\`\`\`powershell
netsh advfirewall firewall delete rule name="IPTrack_Block_IP"
\`\`\`

## 🎯 Administrator Privileges

**Required for:**
- Blocking IPs (Windows Firewall modifications)
- Unblocking IPs

**How to Run as Admin:**
1. Right-click PowerShell/CMD
2. Select "Run as administrator"

**Without Admin:**
- View logs: `iptrack watch`
- Statistics: `iptrack stats`
- Find locations: `iptrack locate <ip>`
- Dashboard: `iptrack dashboard`

## ⚙️ Configuration

Edit \`config.json\`:

\`\`\`json
{
  "max_attempts": 3,
  "auto_block": true,
  "whitelist_ips": ["127.0.0.1", "::1"],
  "geolocation_enabled": true,
  "log_retention_days": 30
}
\`\`\`

## 🔧 Troubleshooting

### "iptrack not recognized"
- Restart terminal after installation
- Check Python Scripts folder in PATH

### "Access Denied"
- Run terminal as Administrator

### Python not found
- Install from python.org
- Check "Add Python to PATH" during installation

## 📚 Documentation

- **QUICK_REFERENCE.md** - Command reference
- **GLOBAL_CLI_GUIDE.md** - Complete guide
- **GitHub** - https://github.com/ZEROAGI-prakash/iptrackwindows

## 📄 License

MIT License

---

**Made with ❤️ for Windows Security**

*Stay Safe. Stay Secure. 🛡️*
