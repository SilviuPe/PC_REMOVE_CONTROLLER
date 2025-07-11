# 🧠 Client-Side Documentation

The **Client Application** is designed to connect **automatically** to the server — **only if the server is already running**. Below is a breakdown of its features and behavior:

---

## 🎮 Features

### 🖱️ **mouseDown / mouseUp**
- Simulates mouse press and release.
- If the mouse is **released at a different position** than it was pressed, the client **detects dragging** and triggers a **drag function**.

---

### ⌨️ **keyDown / keyUp**
- When a key is pressed, the client **keeps it pressed** until it receives a release command.
- Supports:
  - Keyboard shortcuts
  - Key combinations (e.g. Ctrl+C, Alt+Tab)
  - Instant keystroke sending

---

### 🖱️📜 **scroll**
- Standard scroll functionality.
- To scroll **horizontally**, the server user must **hold `Shift` and scroll**.

---

## ⚠️ Mouse Movement Limitations

Unfortunately, due to Python's limitations:
- Sending continuous mouse movement (e.g., moving ~500px rapidly) can generate **a large volume of data**.
- Python cannot handle that amount of real-time data transfer efficiently.
- This may affect **mouse movement precision** and responsiveness.

---

## 💡 Suggestions for Best Experience

- ✅ Use the **same operating system and programs** as the host.
- This ensures better compatibility and **no UI positioning mismatches**.

---

🛠️ *Last updated: July 2025*

