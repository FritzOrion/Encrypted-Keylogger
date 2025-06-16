# 🔐 Encrypted Keylogger: Python Learning Project

This project is a personal learning exercise in developing a **keylogger** in Python that logs keyboard activity and securely sends reports via email. The code implements best practices such as environment variable management, threading for efficiency, and **Fernet encryption** for securing logged data.

> ⚠️ **Disclaimer**: This project is for **educational purposes only**. Unauthorized use of keyloggers is illegal and unethical.

---

## 🧠 Project Overview

This project showcases the evolution of a basic keylogger into a more secure and modular application:

- Logs keystrokes in the background
- Sends logs to an email address every 60 seconds
- Stores email credentials securely with `.env` files
- Uses **threading** for efficient background operation
- Implements **Fernet encryption** for privacy
- Automatically decrypts logs for local review
- Includes hotkey-based termination (Alt + X)

---

## 🛠️ Features

- ⌨️ Keystroke logging
- 📧 Email reporting with encryption
- 🔒 Environment variable management
- 🧵 Efficient threading with `daemon` mode
- 🛑 Graceful exit via hotkey combo
- 🔐 Fernet AES-128 encryption of logs
- 📁 Encrypted file attachment instead of plain text body

---

## 📂 Project Structure

