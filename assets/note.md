### 🔧 What is the Azure CLI?

The **Azure Command-Line Interface (CLI)** is a cross-platform tool used to manage Azure resources directly from the command line. It can be run on Windows locally, via **PowerShell**, **Command Prompt**, **WSL**, **Docker**, or the **Azure Cloud Shell**.

---

### ✅ How to Install or Update on Windows

You can install or update the Azure CLI using:

* **MSI installer** (recommended)
* **ZIP archive**
* **WinGet (Windows Package Manager):**

  ```powershell
  winget install --exact --id Microsoft.AzureCLI
  ```

  To install a specific version:

  ```powershell
  winget install --exact --id Microsoft.AzureCLI --version 2.67.0
  ```

**Note:** After installing, restart the terminal window to use the `az` command.

---

### 🔐 Getting Started

* Log in using:

  ```powershell
  az login
  ```
* View your subscription:

  ```powershell
  az account show
  ```

---

### 🛠 Troubleshooting Common Issues

* **PATH not set**: Restart your terminal.
* **Proxy issues**: Ensure proxy settings allow HTTPS access to `https://aka.ms/` and `https://azcliprod.blob.core.windows.net/`.
* **Slow performance**: Migrate to the **64-bit version** (from v2.51.0+).

---

### ⚡ Optional: Tab Completion in PowerShell

* Add a script to your PowerShell profile to enable **tab completion** for Azure CLI commands.
* Use:

  ```powershell
  Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete
  ```

---

### 🔄 Updating & Migrating

* Use this command to upgrade:

  ```powershell
  az upgrade
  ```
* **Switch to 64-bit CLI** for better performance. Backup your extensions folder beforehand:

  ```powershell
  %userprofile%\.azure\cliextensions
  ```

---

### ❌ Uninstalling Azure CLI

* Remove from **Apps & Features** in Windows.
* Optional: Delete CLI data in:

  ```
  C:\Users\<username>\.azure\
  ```

---

Let me know if you'd like a shorter or more visual one-pager version!
