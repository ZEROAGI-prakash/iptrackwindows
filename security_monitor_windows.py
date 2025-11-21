#!/usr/bin/env python3
"""
Security Monitor System for Windows
Tracks unauthorized access attempts, blocks IPs using Windows Firewall
"""

import os
import sys
import json
import logging
import subprocess
import hashlib
import platform
from datetime import datetime
from pathlib import Path
import socket
import re

class SecurityMonitor:
    def __init__(self, log_dir="logs", config_file="config.json"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.config_file = config_file
        self.config = self.load_config()
        self.is_windows = platform.system() == 'Windows'
        
        # Setup logging
        log_file = self.log_dir / f"security_{datetime.now().strftime('%Y%m%d')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Initialize tracking files
        self.blocked_ips_file = self.log_dir / "blocked_ips.json"
        self.attempts_file = self.log_dir / "login_attempts.json"
        self.blocked_ips = self.load_blocked_ips()
        self.login_attempts = self.load_login_attempts()
        
        self.logger.info(f"Security Monitor initialized on {platform.system()}")
    
    def load_config(self):
        """Load configuration settings"""
        default_config = {
            "max_attempts": 3,
            "block_duration_minutes": 60,
            "monitor_auth_log": True,
            "auto_block": True,
            "alert_email": None,
            "whitelist_ips": ["127.0.0.1", "::1"]
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return {**default_config, **json.load(f)}
            except Exception as e:
                print(f"Error loading config: {e}, using defaults")
        
        # Save default config
        with open(self.config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        
        return default_config
    
    def load_blocked_ips(self):
        """Load blocked IPs from file"""
        if self.blocked_ips_file.exists():
            try:
                with open(self.blocked_ips_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.error(f"Error loading blocked IPs: {e}")
        return {}
    
    def save_blocked_ips(self):
        """Save blocked IPs to file"""
        try:
            with open(self.blocked_ips_file, 'w') as f:
                json.dump(self.blocked_ips, f, indent=2)
        except Exception as e:
            self.logger.error(f"Error saving blocked IPs: {e}")
    
    def load_login_attempts(self):
        """Load login attempts from file"""
        if self.attempts_file.exists():
            try:
                with open(self.attempts_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.error(f"Error loading login attempts: {e}")
        return {}
    
    def save_login_attempts(self):
        """Save login attempts to file"""
        try:
            with open(self.attempts_file, 'w') as f:
                json.dump(self.login_attempts, f, indent=2)
        except Exception as e:
            self.logger.error(f"Error saving login attempts: {e}")
    
    def log_attempt(self, ip_address, username="unknown", status="failed"):
        """Log an access attempt"""
        timestamp = datetime.now().isoformat()
        
        if ip_address not in self.login_attempts:
            self.login_attempts[ip_address] = []
        
        attempt_record = {
            "timestamp": timestamp,
            "username": username,
            "status": status,
            "attempt_number": len(self.login_attempts[ip_address]) + 1
        }
        
        self.login_attempts[ip_address].append(attempt_record)
        self.save_login_attempts()
        
        self.logger.warning(
            f"Access attempt from {ip_address} - User: {username} - "
            f"Status: {status} - Attempt #{attempt_record['attempt_number']}"
        )
        
        # Auto-block if threshold exceeded
        if (self.config['auto_block'] and 
            len(self.login_attempts[ip_address]) >= self.config['max_attempts']):
            self.block_ip(ip_address, reason="Too many failed attempts")
        
        return attempt_record
    
    def block_ip_windows(self, ip_address, rule_name):
        """Block IP using Windows Firewall"""
        try:
            # Add firewall rule using netsh
            cmd = [
                'netsh', 'advfirewall', 'firewall', 'add', 'rule',
                f'name={rule_name}',
                'dir=in',
                'action=block',
                f'remoteip={ip_address}',
                'enable=yes'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                self.logger.info(f"Windows Firewall rule added for {ip_address}")
                return True
            else:
                self.logger.error(f"Failed to add Windows Firewall rule: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error blocking IP with Windows Firewall: {e}")
            return False
    
    def block_ip_unix(self, ip_address):
        """Block IP using iptables/pfctl (Linux/macOS)"""
        try:
            # Create a firewall rules file
            if sys.platform == 'darwin':  # macOS
                pf_rules_file = self.log_dir / "blocked_ips.pf"
                with open(pf_rules_file, 'a') as f:
                    f.write(f"block drop from {ip_address} to any\n")
                self.logger.info(f"To activate: sudo pfctl -f {pf_rules_file}")
            else:  # Linux
                # iptables command
                cmd = ['iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP']
                self.logger.info(f"To block: sudo {' '.join(cmd)}")
            
            return True
        except Exception as e:
            self.logger.error(f"Error creating firewall rule: {e}")
            return False
    
    def block_ip(self, ip_address, reason="Unauthorized access attempt"):
        """Block an IP address using OS-appropriate firewall"""
        # Check whitelist
        if ip_address in self.config.get('whitelist_ips', []):
            self.logger.info(f"IP {ip_address} is whitelisted, not blocking")
            return False
        
        if ip_address in self.blocked_ips:
            self.logger.info(f"IP {ip_address} is already blocked")
            return False
        
        timestamp = datetime.now().isoformat()
        
        # Add to blocked list
        self.blocked_ips[ip_address] = {
            "blocked_at": timestamp,
            "reason": reason,
            "attempts": len(self.login_attempts.get(ip_address, [])),
            "method": "windows_firewall" if self.is_windows else "unix_firewall"
        }
        
        self.save_blocked_ips()
        
        # Block using appropriate method
        if self.is_windows:
            rule_name = f"IPTrack_Block_{ip_address.replace('.', '_')}"
            self.block_ip_windows(ip_address, rule_name)
        else:
            self.block_ip_unix(ip_address)
        
        self.logger.critical(
            f"🚫 BLOCKED IP: {ip_address} - Reason: {reason} - "
            f"Attempts: {self.blocked_ips[ip_address]['attempts']}"
        )
        
        return True
    
    def unblock_ip_windows(self, ip_address):
        """Unblock IP on Windows"""
        try:
            rule_name = f"IPTrack_Block_{ip_address.replace('.', '_')}"
            cmd = [
                'netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                f'name={rule_name}'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            
            if result.returncode == 0:
                self.logger.info(f"Windows Firewall rule removed for {ip_address}")
                return True
            else:
                self.logger.warning(f"No Windows Firewall rule found for {ip_address}")
                return True  # Still return True to remove from our list
                
        except Exception as e:
            self.logger.error(f"Error unblocking IP: {e}")
            return False
    
    def unblock_ip(self, ip_address):
        """Unblock an IP address"""
        if ip_address not in self.blocked_ips:
            self.logger.info(f"IP {ip_address} is not blocked")
            return False
        
        # Remove from blocked list
        blocked_info = self.blocked_ips.pop(ip_address)
        self.save_blocked_ips()
        
        # Remove firewall rule if Windows
        if self.is_windows:
            self.unblock_ip_windows(ip_address)
        else:
            # For Unix, rebuild rules file
            pf_rules_file = self.log_dir / "blocked_ips.pf"
            if pf_rules_file.exists():
                with open(pf_rules_file, 'r') as f:
                    rules = f.readlines()
                
                with open(pf_rules_file, 'w') as f:
                    for rule in rules:
                        if ip_address not in rule:
                            f.write(rule)
        
        self.logger.info(
            f"✅ UNBLOCKED IP: {ip_address} - Was blocked at: {blocked_info['blocked_at']}"
        )
        
        return True
    
    def get_blocked_ips(self):
        """Get list of all blocked IPs"""
        return self.blocked_ips
    
    def get_statistics(self):
        """Get security statistics"""
        total_attempts = sum(len(attempts) for attempts in self.login_attempts.values())
        unique_ips = len(self.login_attempts)
        blocked_count = len(self.blocked_ips)
        
        stats = {
            "total_attempts": total_attempts,
            "unique_ips_attempted": unique_ips,
            "blocked_ips_count": blocked_count,
            "blocked_ips": list(self.blocked_ips.keys()),
            "platform": platform.system()
        }
        
        return stats
    
    def simulate_attack(self, ip_address, username="attacker", attempts=5):
        """Simulate an attack for testing purposes"""
        self.logger.info(f"🔴 Simulating attack from {ip_address}")
        
        for i in range(attempts):
            self.log_attempt(ip_address, username=username, status="failed")
        
        return self.get_statistics()


def main():
    """Main function for CLI usage"""
    monitor = SecurityMonitor()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python security_monitor_windows.py log <ip> <username> - Log an attempt")
        print("  python security_monitor_windows.py block <ip> - Block an IP")
        print("  python security_monitor_windows.py unblock <ip> - Unblock an IP")
        print("  python security_monitor_windows.py list - List blocked IPs")
        print("  python security_monitor_windows.py stats - Show statistics")
        print("  python security_monitor_windows.py simulate <ip> - Simulate attack")
        return
    
    command = sys.argv[1]
    
    if command == "log" and len(sys.argv) >= 3:
        ip = sys.argv[2]
        username = sys.argv[3] if len(sys.argv) > 3 else "unknown"
        monitor.log_attempt(ip, username)
    
    elif command == "block" and len(sys.argv) >= 3:
        ip = sys.argv[2]
        monitor.block_ip(ip)
    
    elif command == "unblock" and len(sys.argv) >= 3:
        ip = sys.argv[2]
        monitor.unblock_ip(ip)
    
    elif command == "list":
        blocked = monitor.get_blocked_ips()
        print("\n🚫 Blocked IPs:")
        print(json.dumps(blocked, indent=2))
    
    elif command == "stats":
        stats = monitor.get_statistics()
        print("\n📊 Security Statistics:")
        print(json.dumps(stats, indent=2))
    
    elif command == "simulate" and len(sys.argv) >= 3:
        ip = sys.argv[2]
        stats = monitor.simulate_attack(ip)
        print("\n📊 Attack Simulation Complete:")
        print(json.dumps(stats, indent=2))
    
    else:
        print("Invalid command or missing arguments")


if __name__ == "__main__":
    main()
