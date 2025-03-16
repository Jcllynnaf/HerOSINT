![2025-03-06_11-33](banner-gt)
# HerOSINT - OSINT IP Scanner  

HerOSINT is a tool OSINT (Open Source Intelligence) based on python designed for investigation, IP analysis, reconnaissance, and collection of target information. This tool provides various techniques to help you gather valuable information about certain targets.  

## 📌 Feature  

This tool includes the following features:  

- **DNS Enumeration:** Identifying IP leaks through DNS enumeration.  
- **Historical IP Lookup:** Looking for a history of IP using API security ( API key required ) 
- **Direct IP Leak:** Trying to find the original IP directly.  
- **WHOIS Lookup:** Get whois information about the target domain.  
- **Port Scanning:** Scan an open port on the target to identify running services.  

---

## ⚙️ Installation  

Follow the steps below to install and run this tool.  

### Requirements 

- **Python 3:** Make sure Python 3 has been installed. You can download it from [situs web Python](https://www.python.org/downloads/).  
- **pip:** `pip` is a package manager for python and is usually included.  

### Clone Repository (Opsional)  

If you clone repository from github, run the following command:  

```bash
git clone https://github.com/jcllynnaf/HerOSINT.git
cd HerOSINT
```

### Create a virtual environment (recommended)  

Make a virtual environment recommended to isolate project dependencies:  

```bash
python3 -m venv venv
```

Activate the virtual environment:  

- **Linux/macOS:**  
  ```bash
  source venv/bin/activate
  ```
- **Windows:**  
  ```bash
  .\venv\Scripts\activate
  ```

### Install dependence  

Use `pip` to install the required dependencies:  

```bash
pip install -r requirements.txt
```

### Run the tool  

After the installation is complete, run this tool with:  

```bash
python3 herosint.py
```

---

## 📌 Installation by Operating System  

### **🖥 Windows**  

- Ensure **Python** has been added to **PATH** during installation.  
- **Install Nmap (Opsional):** If you want to use features **Port Scanning**, install [Nmap](https://nmap.org/download.html) and add the installation directory to **PATH**.  
- Run the terminal as **Administrator** If required.  
- Update `pip` If required:  
  ```bash
  python -m pip install --upgrade pip
  ```

### **🐧 Linux**  

- Install **Nmap** using the following command:  
  ```bash
  sudo apt update && sudo apt install nmap  # Debian/Ubuntu
  sudo yum install nmap  # Fedora/CentOS/RHEL
  ```
- JRun with Root access rights if required:  
  ```bash
  sudo python3 herosint.py
  ```

### **🍎 macOS**  

- Install **Homebrew** jIf not there:  
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
- Install **Nmap** Using Homebrew:  
  ```bash
  brew install nmap
  ```

### **📱 Termux (Android)**  

- Install **Termux** from the Google Play Store or F-Droid.  
- Update the package:  
  ```bash
  pkg update
  ```
- Install **Python** and **Git**:  
  ```bash
  pkg install python git
  ```
- Instal **Nmap**:  
  ```bash
  pkg install nmap
  ```

---

## 📚 Consumption  

1. Run this tool and select the option from the main menu.  
2. Some features require a domain or target IP address.  
3. Follow the instructions on the screen to enter the required information.  

---

## ⚠️ Disclaimer 

- **This tool is only for educational and testing purposes.**  
- **Use only on the system you have permission to be tested.**  
- **Abuse of this tool can cause legal consequences.**  

---

## 🤝 Contribution  

Contribution is very accepted!If you find a problem or have suggestions for improvement, Please make **issue** or **pull request** in our Github repository.  

---

## 📞 Contact & Support  

🔗 **GitHub:** [jcllynnaf](https://github.com/jcllynnaf)  
📸 **Instagram:** [@jcllynnaf](https://instagram.com/jcllynnaf)  
🍵 **Dukung Saya:** [Linktree](https://linktr.ee/jcllynnaf)  

**Made by:** 🛠 **HEROINFATHER-FSOCIETY / JCLLYNNAF**  

---

