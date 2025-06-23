# OS Install 
- Ubuntu 22.04
- 2vCPU
- 8 GB RAM
- 100 GB NVMe

# Basic System Set-up
```bash
# Update apt
sudo apt update -y && sudo apt upgrade -y
sudo timedatectl set-timezone America/Denver
sudo hostnamectl set-hostname kshomebasedev
sudo apt install ufw -y
sudo ufw allow OpenSSH
sudo ufw enable
```

# Configure SSH
``` bash
sudo apt install openssh-server
sudo systemctl enable --now ssh
chmod 600 ~/.ssh/authorized_keys
ssh-keygen -t ed25519 -f ~/.ssh/mykey -N ""
cat ~/.ssh/mykey.pub >> ~/.ssh/authorized_keys
# Copy Private key to local machine
sudo vi /etc/ssh/sshd_config
```
/etc/ssh/sshd_config
```bash
Include /etc/ssh/sshd_config.d/*.conf

Port 22
AddressFamily any
ListenAddress 0.0.0.0
ListenAddress ::

PermitRootLogin no
PubkeyAuthentication yes
AuthorizedKeysFile      .ssh/authorized_keys .ssh/authorized_keys2

PasswordAuthentication no # Test ssh with this as yes, once confirmed working change to no
```
apply changes
```bash
sudo systemctl restart sshd
```

## SQLite Setup
``` bash
sudo apt install sqlite3 -y
sudo  mkdir /opt/kshomebase
sudo chown kris:kris /opt/kshomebase
cd /opt/kshomebase

# SCP schema.sql into this directory
touch  /opt/kshomebase/homebase.db
chown kris:kris /opt/kshomebase/homebase.db
chmod 660 /opt/kshomebase/homebase.db

# Apply schema
sqlite3 /opt/kshomebase/homebase.db < /opt/kshomebase/schema.sql

# Validate 
sqlite3 /opt/kshomebase/homebase.db
.tables
.schema users # or any other table
.quit
```