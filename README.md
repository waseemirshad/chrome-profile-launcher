# 🔗 Chrome Profile Launcher

Python GUI app jo aapki **saari Chrome profiles** fetch karta hai, **email** dikhata hai, aur **one-click** mein us profile ke saath Chrome open karta hai.

> **50 profiles? Ek click, ek profile open. No manual extension, no cookies extension.**

---

## ✨ Features

- ✅ Saari Chrome profiles fetch karein (Default, Profile 1, Profile 2...)
- ✅ Har profile ka **Google email** dikhaye
- ✅ Ek button dabao → Real Chrome us profile ke saath open
- ✅ Clean GUI (Tkinter, built-in, no extra install)
- ✅ Windows support

---

## 🚀 Run (2 seconds)

### Option 1: Double-click `run.bat`
```
run.bat
```

### Option 2: Command line
```bash
python main.py
```

**Bas itna. Python installed hona chahiye (3.7+).**

---

## 📸 Screenshot

```
┌──────────────────────────────────────────┐
│     🔗 Chrome Profile Launcher          │
├──────────────────────────────────────────┤
│  Found 3 profile(s)                     │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ #1  Default                      │   │
│  │     user@gmail.com          [Open]│   │
│  └──────────────────────────────────┘   │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ #2  Profile 1                     │   │
│  │     test@gmail.com          [Open]│   │
│  └──────────────────────────────────┘   │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ #3  Profile 2                     │   │
│  │     work@gmail.com          [Open]│   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

---

## 🛠 How it works

1. `%LOCALAPPDATA%\Google\Chrome\User Data` folder scan karta hai
2. Har profile ka `Preferences` JSON read karta hai → **email extract**
3. GUI mein har profile card banata hai
4. `chrome.exe --profile-directory="Profile X"` se Chrome launch

---

## ⚙️ Requirements

- Python 3.7+
- Google Chrome installed
- Windows (Chrome ka path Windows ke hisaab se hai)

---

## 📝 Future ideas

- [ ] Profile mein auto-login ke baad cookies auto-extract
- [ ] Playwright integration for headless cookie fetching
- [ ] Export all cookies to JSON with one click
- [ ] Dark mode

---

MIT License
