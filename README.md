# 🕵️‍♂️ Subdomain Finder CLI

A simple, interactive CLI tool to enumerate and resolve subdomains with DNS resolution check and pretty output.

---

## 🚀 Features
- 🔍 **Subdomain enumeration from `crt.sh`**
- 🌐 **Optional DNS resolution** to check if subdomains resolve to valid IP addresses
- 🎨 **Beautiful CLI UI** powered by `rich`: progress bar, table, colored output
- 🛡️ **Graceful error handling** for API and DNS failures

---

## 📦 Installation

```bash
git clone https://github.com/justhalooo/subdomain-finder-cli.git
cd subdomain-finder-cli
pip install -r requirements.txt
```

---

## 🕹️ Usage

```bash
python main.py
```

Example session:

```
Subdomain Finder CLI
Input domain finder: example.com
Check DNS resolution? (y/n): y
[+] Found 20 subdomains.
[+] 15 active subdomains resolved.
```

---

## ⚡ Dependencies
- Python 3.x
- requests
- rich

---

## 📝 License
MIT License — feel free to use, modify, and share.

---

## 🙌 Contributing
PRs welcome! If you want to add additional APIs, export to file, or more features, feel free to fork and submit a pull request.

---

## 📫 Contact
Made with ❤️ by [justhalooo](https://github.com/justhalooo)
