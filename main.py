import os
import json
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

# ===== CONFIG =====
# Agar Chrome kahin aur installed hai to ye path badlein
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]


def get_chrome_exe():
    """Chrome ka sahi path dhundho"""
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path
    # Try 'where chrome' as fallback
    try:
        result = subprocess.run(["where", "chrome"], capture_output=True, text=True, shell=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().split("\n")[0]
    except:
        pass
    return None


def get_chrome_profiles():
    """User Data folder se saari Chrome profiles fetch karo (email ke saath)"""
    user_data = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    profiles = []

    if not os.path.exists(user_data):
        return profiles

    for folder in sorted(os.listdir(user_data)):
        profile_path = os.path.join(user_data, folder)
        prefs_file = os.path.join(profile_path, "Preferences")

        # Sirf folders lein (Default, Profile 1, Profile 2, ...)
        if not os.path.isdir(profile_path):
            continue
        if not folder.startswith(("Default", "Profile")):
            continue
        if not os.path.exists(prefs_file):
            continue

        # Preferences JSON se email nikalo
        email = "—"
        display_name = ""
        try:
            with open(prefs_file, "r", encoding="utf-8") as f:
                prefs = json.load(f)
                account_info = prefs.get("account_info", [])
                if account_info and len(account_info) > 0:
                    ai = account_info[0]
                    email = ai.get("email", "—")
                    display_name = ai.get("full_name", "")
        except:
            pass

        profiles.append({
            "folder": folder,
            "email": email,
            "display_name": display_name,
            "path": profile_path
        })

    return profiles


def open_profile(profile_folder):
    """Real Chrome us profile ke saath open karo"""
    chrome = get_chrome_exe()
    if not chrome:
        messagebox.showerror("Error", "Chrome nahi mila!\nChrome installed hai?")
        return

    try:
        subprocess.Popen([chrome, f"--profile-directory={profile_folder}"])
    except Exception as e:
        messagebox.showerror("Error", f"Chrome open nahi ho paya:\n{e}")


def main():
    root = tk.Tk()
    root.title("Chrome Profile Launcher")
    root.geometry("550x650")
    root.configure(bg="#f0f0f0")

    # === Header ===
    header = tk.Frame(root, bg="#1a73e8", height=60)
    header.pack(fill="x")
    tk.Label(
        header, text="🔗 Chrome Profile Launcher",
        font=("Segoe UI", 16, "bold"), fg="white", bg="#1a73e8"
    ).pack(pady=15)

    # === Profile count ===
    profiles = get_chrome_profiles()

    if not profiles:
        tk.Label(
            root, text="❌ Koi Chrome profile nahi mili!",
            font=("Segoe UI", 12), fg="red", bg="#f0f0f0"
        ).pack(pady=40)
        tk.Label(
            root, text="Kya Chrome installed hai?",
            font=("Segoe UI", 10), fg="#666", bg="#f0f0f0"
        ).pack()
    else:
        tk.Label(
            root, text=f"Found {len(profiles)} profile(s)",
            font=("Segoe UI", 11), fg="#444", bg="#f0f0f0"
        ).pack(pady=(15, 5))

        # === Scrollable area ===
        canvas = tk.Canvas(root, bg="#f0f0f0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", tags="frame")

        # Canvas width track karo
        def on_canvas_configure(event):
            canvas.itemconfig("frame", width=event.width)
        canvas.bind("<Configure>", on_canvas_configure)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Mouse wheel scroll
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)

        # === Profile cards ===
        for i, p in enumerate(profiles):
            card = tk.Frame(scroll_frame, bg="white", relief="flat", bd=0, highlightthickness=1,
                          highlightbackground="#ddd", highlightcolor="#ddd")
            card.pack(fill="x", padx=25, pady=6, ipady=5)

            # Left: number + info
            left = tk.Frame(card, bg="white")
            left.pack(side="left", fill="both", expand=True, padx=12, pady=10)

            # Profile number badge
            badge = tk.Label(left, text=f"#{i+1}", font=("Segoe UI", 9, "bold"),
                           fg="white", bg="#1a73e8", width=3, height=1)
            badge.pack(side="left", padx=(0, 10))

            # Name + email
            text_info = tk.Frame(left, bg="white")
            text_info.pack(side="left")

            tk.Label(text_info, text=p["folder"], font=("Segoe UI", 11, "bold"),
                   fg="#222", bg="white", anchor="w").pack(anchor="w")
            tk.Label(text_info, text=p["email"], font=("Segoe UI", 9),
                   fg="#666", bg="white", anchor="w").pack(anchor="w")

            # Right: Open button
            btn = tk.Button(
                card, text="Open", font=("Segoe UI", 10, "bold"),
                bg="#1a73e8", fg="white", relief="flat",
                activebackground="#1557b0", activeforeground="white",
                padx=18, pady=4, cursor="hand2",
                command=lambda d=p["folder"]: open_profile(d)
            )
            btn.pack(side="right", padx=12, pady=10)

        canvas.pack(side="left", fill="both", expand=True, padx=(0, 0))
        scrollbar.pack(side="right", fill="y")

    # === Footer ===
    footer = tk.Frame(root, bg="#e8e8e8", height=30)
    footer.pack(side="bottom", fill="x")
    tk.Label(
        footer, text="Made for fast profile switching",
        font=("Segoe UI", 8), fg="#999", bg="#e8e8e8"
    ).pack(pady=6)

    root.mainloop()


if __name__ == "__main__":
    main()
