# 🛡️ IPTrack - Windows Edition# 🛡️ IPTrack - Windows Edition



**Professional Security Monitoring & IP Management Tool for Windows**Professional Security Monitoring & IP Management Tool for Windows



[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows)**Track. Block. Defend. - Your Windows Security Guardian**

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)## 🌟 What is IPTrack?



> Track unauthorized access attempts, automatically block malicious IPs, and geolocate attackers - all from your Windows terminal.IPTrack is a powerful, Gemini-style command-line security tool designed specifically for Windows. It monitors unauthorized access attempts, automatically blocks suspicious IPs using Windows Firewall, and provides real-time geolocation tracking.



---### ✨ Key Features



## 🌟 Features- 🔒 **Automatic IP Blocking** - Uses Windows Firewall (netsh) to block malicious IPs

- 🌍 **IP Geolocation** - Track attacker locations with city, country, ISP details

- 🔒 **Automatic IP Blocking** - Integrates with Windows Firewall (netsh advfirewall)- 📊 **Real-time Monitoring** - Watch security logs as they happen

- 🌍 **IP Geolocation** - Track attacker locations (city, country, ISP, coordinates)- 🎯 **Smart Auto-Block** - Blocks after 3 failed attempts (configurable)

- 📊 **Real-time Monitoring** - Watch security logs as events happen- 🔄 **Easy Unblock** - Reverse blocks with a single command

- 🎯 **Smart Auto-Block** - Automatically blocks after 3 failed attempts (configurable)- 📈 **Security Dashboard** - Visual overview of all security events

- 🔄 **Easy Unblock** - Reverse blocks with a single command- 💾 **Export Logs** - Save all security data to JSON

- 📈 **Security Dashboard** - Comprehensive overview of all security events- 🎨 **Beautiful CLI** - Colorful terminal interface with clear formatting

- 💾 **Export Logs** - Save security data to JSON for analysis

- 🎨 **Beautiful CLI** - Colorful terminal interface with clear formatting## 📋 Requirements

- ⚡ **Global Command** - Use `iptrack` from anywhere in your system

- **Windows 10/11** or Windows Server 2016+

---- **Python 3.7+** - Download from [python.org](https://www.python.org/downloads/)

- **Administrator Privileges** - Required for blocking/unblocking IPs

## 📋 Requirements- **Internet Connection** - For IP geolocation features



| Requirement | Version/Details |## 🚀 Quick Installation

|------------|----------------|

| **Operating System** | Windows 10/11 or Windows Server 2016+ |### PowerShell (Recommended)

| **Python** | 3.7 or higher ([Download](https://www.python.org/downloads/)) |

| **Privileges** | Administrator rights (for blocking/unblocking IPs) |Right-click PowerShell and select "Run as Administrator", then:

| **Internet** | Required for IP geolocation features |

| **Firewall** | Windows Firewall must be enabled |\`\`\`powershell

cd path\to\iptrack-windows

---powershell -ExecutionPolicy Bypass -File install.ps1

\`\`\`

## 🚀 Installation

### Command Prompt

### Step 1: Clone the Repository

Right-click CMD and select "Run as Administrator", then:

```powershell

# Open PowerShell and run:\`\`\`cmd

git clone https://github.com/ZEROAGI-prakash/iptrackwindows.gitcd path\to\iptrack-windows

cd iptrackwindowsinstall.bat

```\`\`\`



### Step 2: Run Installer## 💻 Usage



**Option A: PowerShell (Recommended)**\`\`\`powershell

iptrack --help                  # Show all commands

Right-click PowerShell → Select "Run as Administrator"iptrack watch                   # Monitor logs in real-time

iptrack block 192.168.1.100     # Block an IP

```powershelliptrack unblock 192.168.1.100   # Unblock an IP

# Run the PowerShell installeriptrack list                    # List blocked IPs

powershell -ExecutionPolicy Bypass -File install.ps1iptrack locate 8.8.8.8          # Find IP location

```iptrack stats                   # Show statistics

iptrack dashboard               # Security dashboard

**Option B: Command Prompt**iptrack export                  # Export logs

\`\`\`

Right-click Command Prompt → Select "Run as Administrator"

## 🔐 Windows Firewall Integration

```cmd

# Run the batch installerIPTrack uses `netsh advfirewall firewall` commands to block IPs.

install.bat

```### When Blocking:

\`\`\`powershell

### Step 3: Restart Your Terminalnetsh advfirewall firewall add rule name="IPTrack_Block_IP" dir=in action=block remoteip=192.168.1.100

\`\`\`

Close and reopen your terminal for PATH changes to take effect.

### When Unblocking:

### Step 4: Verify Installation\`\`\`powershell

netsh advfirewall firewall delete rule name="IPTrack_Block_IP"

```powershell\`\`\`

# Check if iptrack is installed

iptrack --help## 🎯 Administrator Privileges

```

**Required for:**

---- Blocking IPs (Windows Firewall modifications)

- Unblocking IPs

## 💻 Usage

**How to Run as Admin:**

### Basic Commands1. Right-click PowerShell/CMD

2. Select "Run as administrator"

```powershell

# Show all available commands**Without Admin:**

iptrack --help- View logs: `iptrack watch`

- Statistics: `iptrack stats`

# Monitor security logs in real-time- Find locations: `iptrack locate <ip>`

iptrack watch- Dashboard: `iptrack dashboard`



# Block an IP address (requires admin)## ⚙️ Configuration

iptrack block 192.168.1.100

Edit \`config.json\`:

# Unblock an IP address (requires admin)

iptrack unblock 192.168.1.100\`\`\`json

{

# List all currently blocked IPs  "max_attempts": 3,

iptrack list  "auto_block": true,

  "whitelist_ips": ["127.0.0.1", "::1"],

# Find location of an IP address  "geolocation_enabled": true,

iptrack locate 8.8.8.8  "log_retention_days": 30

}

# Show security statistics\`\`\`

iptrack stats

## 🔧 Troubleshooting

# Open security dashboard

iptrack dashboard### "iptrack not recognized"

- Restart terminal after installation

# Export logs to JSON- Check Python Scripts folder in PATH

iptrack export

### "Access Denied"

# Export with custom filename- Run terminal as Administrator

iptrack export -o security_report.json

```### Python not found

- Install from python.org

### Real-World Examples- Check "Add Python to PATH" during installation



**Example 1: Monitor and Block Suspicious Activity**## 📚 Documentation



```powershell- **QUICK_REFERENCE.md** - Command reference

# Start monitoring in real-time- **GLOBAL_CLI_GUIDE.md** - Complete guide

iptrack watch- **GitHub** - https://github.com/ZEROAGI-prakash/iptrackwindows



# In another terminal window (as Administrator):## 📄 License

# Block the suspicious IP

iptrack block 45.123.67.89MIT License



# Check where the attacker is from---

iptrack locate 45.123.67.89

```**Made with ❤️ for Windows Security**



**Example 2: Review Security Status***Stay Safe. Stay Secure. 🛡️*


```powershell
# Check overall statistics
iptrack stats

# View detailed dashboard
iptrack dashboard

# List all blocked IPs
iptrack list
```

**Example 3: Unblock a False Positive**

```powershell
# View blocked IPs
iptrack list

# Unblock a legitimate IP (as Administrator)
iptrack unblock 203.45.67.89
```

**Example 4: Export Security Data**

```powershell
# Export all logs with timestamp
iptrack export -o security_report_2024-11-21.json
```

---

## 🔐 Windows Firewall Integration

### How It Works

IPTrack uses Windows Firewall's `netsh advfirewall firewall` commands to create and manage firewall rules.

### Blocking an IP Address

When you run `iptrack block 192.168.1.100`, IPTrack executes:

```powershell
netsh advfirewall firewall add rule `
  name="IPTrack_Block_192_168_1_100" `
  dir=in `
  action=block `
  remoteip=192.168.1.100 `
  enable=yes
```

**What This Does:**
- Creates a firewall rule named `IPTrack_Block_192_168_1_100`
- Direction: Inbound (`dir=in`)
- Action: Block traffic (`action=block`)
- Target: Specific IP address (`remoteip=192.168.1.100`)
- Status: Enabled immediately

### Unblocking an IP Address

When you run `iptrack unblock 192.168.1.100`, IPTrack executes:

```powershell
netsh advfirewall firewall delete rule `
  name="IPTrack_Block_192_168_1_100"
```

### Manual Firewall Management

**View all IPTrack firewall rules:**

```powershell
netsh advfirewall firewall show rule name=all | Select-String "IPTrack"
```

**Remove all IPTrack rules manually:**

```powershell
# List all IPTrack rules
netsh advfirewall firewall show rule name=all | Select-String "IPTrack_Block"

# Delete each rule (replace with actual rule name)
netsh advfirewall firewall delete rule name="IPTrack_Block_192_168_1_100"
```

**Check Windows Firewall status:**

```powershell
# PowerShell method
Get-NetFirewallProfile | Format-Table Name, Enabled

# Or using netsh
netsh advfirewall show allprofiles
```

---

## 🎯 Administrator Privileges

### Why Administrator Access is Required

- **Firewall Modifications**: Windows Firewall requires elevated privileges to add/remove rules
- **System Security**: Blocking network traffic is a protected operation
- **NetSH Commands**: The `netsh advfirewall` command requires admin rights

### How to Run as Administrator

**Method 1: PowerShell**
1. Press `Windows + X`
2. Select "Windows PowerShell (Admin)" or "Terminal (Admin)"

**Method 2: Search Menu**
1. Press `Windows` key
2. Type "PowerShell"
3. Right-click "Windows PowerShell"
4. Click "Run as administrator"

**Method 3: From File Explorer**
1. Navigate to the iptrack-windows folder
2. Hold `Shift` + Right-click in the folder
3. Select "Open PowerShell window here as administrator"

### Features Available Without Admin

You can use these commands **without** administrator privileges:

```powershell
iptrack watch       # Monitor logs in real-time
iptrack stats       # View security statistics
iptrack locate <ip> # Find IP geolocation
iptrack dashboard   # View security dashboard
iptrack export      # Export logs to JSON
```

### Features Requiring Admin

These commands **require** administrator privileges:

```powershell
iptrack block <ip>    # Block an IP address
iptrack unblock <ip>  # Unblock an IP address
```

---

## ⚙️ Configuration

### Edit Configuration File

The `config.json` file controls IPTrack's behavior:

```json
{
  "max_attempts": 3,
  "block_duration_minutes": 60,
  "monitor_auth_log": true,
  "auto_block": true,
  "alert_email": null,
  "whitelist_ips": ["127.0.0.1", "::1"],
  "geolocation_enabled": true,
  "log_retention_days": 30
}
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `max_attempts` | Integer | `3` | Number of failed attempts before auto-blocking |
| `block_duration_minutes` | Integer | `60` | How long to block an IP (minutes) |
| `auto_block` | Boolean | `true` | Enable automatic blocking after max_attempts |
| `whitelist_ips` | Array | `["127.0.0.1", "::1"]` | IPs that will never be blocked |
| `geolocation_enabled` | Boolean | `true` | Enable IP location tracking |
| `log_retention_days` | Integer | `30` | How long to keep logs |

### Modify Configuration

```powershell
# Open config.json in Notepad
notepad config.json

# Or use your preferred editor
code config.json  # VS Code
```

---

## 🔧 Troubleshooting

### "iptrack is not recognized as a command"

**Problem**: Terminal can't find the `iptrack` command.

**Solutions**:

1. **Restart your terminal** after installation
2. Check if Python Scripts folder is in PATH:
   ```powershell
   $env:Path -split ';' | Select-String "Python"
   ```
3. Find Python Scripts location:
   ```powershell
   python -c "import sysconfig; print(sysconfig.get_path('scripts'))"
   ```
4. Manually add to PATH if needed:
   ```powershell
   # Add temporarily (this session only)
   $env:Path += ";C:\Users\YourName\AppData\Local\Programs\Python\Python3XX\Scripts"
   
   # Add permanently (requires admin)
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Path\To\Python\Scripts", "User")
   ```

### "Access Denied" when blocking/unblocking

**Problem**: Insufficient privileges for firewall operations.

**Solution**:
- Close your current terminal
- Right-click PowerShell/CMD
- Select "Run as administrator"
- Try the command again

### Python not found

**Problem**: Python is not installed or not in PATH.

**Solutions**:

1. **Install Python**:
   - Download from [python.org](https://www.python.org/downloads/)
   - **Important**: Check "Add Python to PATH" during installation
   
2. **Verify Python installation**:
   ```powershell
   python --version
   pip --version
   ```

3. **If Python is installed but not found**:
   ```powershell
   # Find Python installation
   where.exe python
   
   # Add to PATH manually (see above)
   ```

### Windows Firewall is disabled

**Problem**: Windows Firewall must be enabled for IPTrack to work.

**Solution**:

```powershell
# Check firewall status
Get-NetFirewallProfile | Format-Table Name, Enabled

# Enable Windows Firewall (requires admin)
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# Or use GUI: Control Panel → Windows Defender Firewall → Turn Windows Firewall on or off
```

### "requests" module not found

**Problem**: Required Python package not installed.

**Solution**:

```powershell
# Install requests library
pip install requests

# Or reinstall all requirements
pip install -r requirements.txt
```

### IPTrack installed but commands don't work

**Problem**: Package might not be installed correctly.

**Solution**:

```powershell
# Reinstall IPTrack
cd path\to\iptrack-windows
pip uninstall iptrack-security -y
pip install --user -e .

# Verify installation
pip show iptrack-security
```

---

## 📂 File Structure

```
iptrack-windows/
├── iptrack                      # Main CLI executable
├── security_monitor.py          # Windows Firewall integration
├── ip_locator.py               # IP geolocation engine
├── defender_control.py         # Security dashboard & controls
├── install.ps1                 # PowerShell installer
├── install.bat                 # Batch installer
├── setup.py                    # Python package configuration
├── config.json                 # Configuration file
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── QUICK_REFERENCE.md          # Quick command reference
├── GLOBAL_CLI_GUIDE.md         # Complete documentation
├── LICENSE                     # MIT License
└── logs/                       # Security logs directory
    ├── security_YYYYMMDD.log   # Daily security logs
    ├── blocked_ips.json        # Blocked IP records
    ├── login_attempts.json     # Login attempt tracking
    └── ip_locations.json       # Cached IP locations
```

---

## 🌐 IP Geolocation

### How It Works

IPTrack uses **free public APIs** (no API key required) to get IP location data:

1. **ip-api.com** (Primary source)
2. **ipapi.co** (Backup)
3. **ipwhois.app** (Secondary backup)

### Information Retrieved

```powershell
# Example output from: iptrack locate 8.8.8.8
```

```
Location Found:

  IP Address: 8.8.8.8
  City: Mountain View
  Region: California
  Country: United States (US)
  Timezone: America/Los_Angeles
  ISP: Google LLC
  Organization: Google Public DNS
  Coordinates: 37.4056, -122.0775

  Map: https://www.google.com/maps?q=37.4056,-122.0775
```

### Privacy Note

- Geolocation queries are sent to public APIs
- No personal data is transmitted
- Results are cached locally in `logs/ip_locations.json`
- Cached results reduce API calls and speed up repeated lookups

---

## 📊 Security Dashboard

### View Dashboard

```powershell
iptrack dashboard
```

### Dashboard Features

- **Total Attempts**: All unauthorized access attempts
- **Unique IPs**: Number of different IPs that attempted access
- **Blocked IPs**: Currently blocked IP addresses
- **Recent Activity**: Latest security events with locations
- **Top Attackers**: Most frequent offenders
- **Geographic Distribution**: Where attacks are coming from

---

## 🚨 Security Best Practices

1. **Regular Monitoring**: Run `iptrack watch` regularly to stay informed
2. **Review Blocked IPs**: Use `iptrack list` to review what's blocked
3. **Whitelist Trusted IPs**: Add your own IPs to `config.json` whitelist
4. **Export Logs**: Regularly export logs for audit trails
5. **Update Whitelist**: Keep your whitelist current
6. **Monitor Statistics**: Check `iptrack stats` for unusual patterns
7. **Backup Configuration**: Save your `config.json` settings

### Example Security Routine

```powershell
# Morning security check
iptrack stats                    # Check overnight activity
iptrack dashboard                # Review dashboard
iptrack export -o daily_$(Get-Date -Format 'yyyy-MM-dd').json  # Backup logs

# Real-time monitoring (optional)
iptrack watch                    # Monitor during the day
```

---

## 🎓 Quick Start Tutorial

### First-Time Setup

```powershell
# 1. Clone and install
git clone https://github.com/ZEROAGI-prakash/iptrackwindows.git
cd iptrackwindows
powershell -ExecutionPolicy Bypass -File install.ps1

# 2. Close and reopen terminal as Administrator

# 3. Verify installation
iptrack --help

# 4. Test geolocation
iptrack locate 8.8.8.8

# 5. Check statistics
iptrack stats

# 6. Start monitoring
iptrack watch
```

### Test Blocking (Practice)

```powershell
# Block a test IP
iptrack block 192.168.1.100

# Verify it's blocked
iptrack list

# Unblock it
iptrack unblock 192.168.1.100

# Verify it's unblocked
iptrack list
```

---

## 📚 Additional Documentation

- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick command cheat sheet
- **[GLOBAL_CLI_GUIDE.md](GLOBAL_CLI_GUIDE.md)** - Complete CLI documentation
- **[GitHub Repository](https://github.com/ZEROAGI-prakash/iptrackwindows)** - Source code and updates
- **[Issue Tracker](https://github.com/ZEROAGI-prakash/iptrackwindows/issues)** - Report bugs or request features

---

## 🤝 Contributing

Found a bug? Have a feature request? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚡ Performance Tips

### 1. Clean Old Firewall Rules

```powershell
# View all IPTrack rules
netsh advfirewall firewall show rule name=all | Select-String "IPTrack"

# Remove old rules if needed
netsh advfirewall firewall delete rule name="IPTrack_Block_OLD_IP"
```

### 2. Manage Log Files

```powershell
# View log file sizes
Get-ChildItem -Path .\logs -Recurse | Select-Object Name, Length | Sort-Object Length -Descending

# Clear old logs (older than 30 days)
Get-ChildItem -Path .\logs\*.log | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-30)} | Remove-Item

# Clear location cache (if needed)
Remove-Item .\logs\ip_locations.json
```

### 3. Optimize Geolocation

- Locations are automatically cached
- Clear cache only if data seems stale
- Cache file: `logs/ip_locations.json`

---

## 🔮 Roadmap

Future features planned:

- [ ] GUI Dashboard (Windows Forms/WPF)
- [ ] Email/SMS Alerts
- [ ] Integration with Windows Event Viewer
- [ ] Machine Learning threat detection
- [ ] Cloud sync for logs
- [ ] Multi-language support
- [ ] Scheduled reports
- [ ] Custom alert rules

---

## 📞 Support

Need help? Here's how to get support:

1. **Documentation**: Check this README and other docs first
2. **Issues**: [Open an issue](https://github.com/ZEROAGI-prakash/iptrackwindows/issues) on GitHub
3. **Discussions**: Join [GitHub Discussions](https://github.com/ZEROAGI-prakash/iptrackwindows/discussions)

---

## 🙏 Acknowledgments

- **Windows Firewall** - For robust network security
- **Free IP APIs** - ip-api.com, ipapi.co, ipwhois.app
- **Python Community** - For excellent libraries and tools
- **Contributors** - Thank you to everyone who helps improve IPTrack

---

<div align="center">

**Made with ❤️ for Windows Security**

🛡️ **Stay Safe. Stay Secure.** 🛡️

[⭐ Star on GitHub](https://github.com/ZEROAGI-prakash/iptrackwindows) | [🐛 Report Bug](https://github.com/ZEROAGI-prakash/iptrackwindows/issues) | [💡 Request Feature](https://github.com/ZEROAGI-prakash/iptrackwindows/issues)

</div>
