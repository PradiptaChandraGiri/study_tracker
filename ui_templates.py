# ui_templates.py
# This file stores all templates as Python strings.
# We map them in a dictionary so Flask can load them without .html files.

TEMPLATE_BASE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Smart Study Tracker{% endblock %}</title>
  <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
  --primary: #2563eb;
  --primary-hover: #1e40af;
  --sidebar-bg: #111827;
  --bg-main: #f5f7fb;
  --text-dark: #111827;
  --text-muted: #6b7280;
  --bg-card: #ffffff;
  --border: #e5e7eb;
}

body {
  font-family: "Poppins", sans-serif;
  margin: 0;
  background: var(--bg-main);
  display: flex;
  color: var(--text-dark);
}

/* ── Sidebar ────────────────────────────────────────── */
.sidebar {
  width: 230px;
  background: var(--sidebar-bg);
  height: 100vh;
  padding: 24px 20px;
  color: white;
  position: fixed;
  box-sizing: border-box;
  z-index: 100;
}
.sidebar .logo {
  font-size: 24px;
  margin-bottom: 40px;
  font-weight: 700;
  color: white;
  text-decoration: none;
  display: block;
}
.sidebar a.nav-link {
  display: block;
  color: #cbd5e1;
  padding: 12px 16px;
  text-decoration: none;
  border-radius: 8px;
  margin-bottom: 8px;
  transition: 0.2s;
  font-weight: 500;
}
.sidebar a.nav-link:hover, .sidebar a.nav-link.active {
  background: var(--primary);
  color: white;
}
.sidebar a.logout {
  color: #fca5a5;
  margin-top: 30px;
}
.sidebar a.logout:hover {
  background: rgba(239, 68, 68, 0.2);
  color: #fee2e2;
}

/* ── Main Layout ────────────────────────────────────── */
.main {
  margin-left: 230px;
  width: calc(100% - 230px);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.main.full-width {
  margin-left: 0;
  width: 100%;
}

/* ── Header ─────────────────────────────────────────── */
header.top-header {
  background: white;
  padding: 20px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
  position: sticky;
  top: 0;
  z-index: 10;
}
header.top-header h1 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
}
.profile {
  display: flex;
  align-items: center;
  gap: 12px;
}
.profile span {
  color: var(--text-muted);
  font-weight: 500;
  font-size: 14px;
}
.avatar {
  background: var(--primary);
  color: white;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 16px;
}

/* ── Content Area ───────────────────────────────────── */
.content {
  padding: 30px;
  flex: 1;
}

/* ── Cards Grid ─────────────────────────────────────── */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}
.card {
  background: var(--bg-card);
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
  text-align: center;
  border: 1px solid var(--border);
}
.card.align-left { text-align: left; }
.card h3, .card-title {
  color: var(--text-muted);
  margin: 0 0 10px 0;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.card p, .card-value {
  font-size: 28px;
  font-weight: 700;
  color: var(--text-dark);
  margin: 0;
}

/* ── Suggestions & Highlighting ─────────────────────── */
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 30px;
}
.suggestion-item {
  background: #eff6ff;
  border-left: 4px solid var(--primary);
  padding: 12px 16px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 12px;
  font-size: 14px;
  color: var(--text-dark);
}
.highlight-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}
.highlight-row:last-child { border-bottom: none; }
.highlight-label { color: var(--text-muted); font-size: 14px; }
.highlight-value { font-weight: 600; font-size: 15px; }

/* ── Forms ──────────────────────────────────────────── */
.form-container {
  background: white;
  padding: 35px 40px;
  margin: 0 auto;
  width: 400px;
  max-width: 100%;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.04);
  border: 1px solid var(--border);
  box-sizing: border-box;
}
.form-container.wide { width: 600px; }
.form-container h2 { margin-top: 0; margin-bottom: 24px; font-weight: 600; text-align: center; }
.form-group { margin-bottom: 18px; }
label { display: block; color: var(--text-muted); font-size: 13px; margin-bottom: 6px; font-weight: 500; }
input, select, textarea {
  width: 100%;
  padding: 12px 14px;
  border-radius: 8px;
  border: 1px solid var(--border);
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
  font-size: 14px;
  color: var(--text-dark);
  background: #f9fafb;
}
input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: var(--primary);
  background: white;
  box-shadow: 0 0 0 3px rgba(37,99,235,0.1);
}
textarea { resize: vertical; min-height: 80px; }

/* ── Buttons ────────────────────────────────────────── */
.btn {
  background: var(--primary);
  color: white;
  padding: 12px;
  width: 100%;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  cursor: pointer;
  transition: 0.2s;
  font-family: "Poppins", sans-serif;
  font-weight: 600;
}
.btn:hover { background: var(--primary-hover); transform: translateY(-1px); box-shadow: 0 4px 10px rgba(37,99,235,0.2); }
.btn-outline { background: transparent; border: 1px solid var(--primary); color: var(--primary); }
.btn-outline:hover { background: #eff6ff; }
.btn-danger { background: #fee2e2; color: #ef4444; }
.btn-danger:hover { background: #fecaca; }
.btn-inline { width: auto; padding: 10px 20px; }

/* ── Tables ─────────────────────────────────────────── */
.chart-box {
  background: white; padding: 25px; border-radius: 12px;
  border: 1px solid var(--border); margin-bottom: 30px;
}
.data-table {
  width: 100%; border-collapse: collapse; background: white;
  border-radius: 12px; overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
  border: 1px solid var(--border);
}
.data-table th, .data-table td { padding: 14px 20px; text-align: left; border-bottom: 1px solid var(--border); font-size: 14px; }
.data-table th { background: #f8fafc; color: var(--text-muted); font-weight: 600; text-transform: uppercase; font-size: 12px; letter-spacing: 0.5px; }
.data-table tr:hover td { background: #f8fafc; }

/* ── Messages & Toasts ──────────────────────────────── */
.alert { padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 14px; }
.alert-error { background: #fee2e2; color: #b91c1c; border: 1px solid #fca5a5; }
.alert-success { background: #d1fae5; color: #047857; border: 1px solid #6ee7b7; }

.toast-notification {
  display: flex; align-items: center; gap: 12px;
  background: white; border-left: 5px solid #f59e0b;
  padding: 14px 20px; border-radius: 8px; margin-bottom: 20px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  animation: slideDownToast 0.4s ease forwards;
}
.toast-notification.success { border-left-color: #10b981; }
.toast-icon { font-size: 1.5rem; }
.toast-body { flex: 1; font-size: 14px; color: var(--text-dark); }
.toast-close { background: none; border: none; color: var(--text-muted); font-size: 1.2rem; cursor: pointer; }
@keyframes slideDownToast {
  0% { transform: translateY(-20px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

/* ── Auto-Layout Classes ────────────────────────────── */
.flex { display: flex; }
.justify-between { justify-content: space-between; }
.align-center { align-items: center; }
.gap-10 { gap: 10px; }
.gap-20 { gap: 20px; }
.text-center { text-align: center; }
.mt-20 { margin-top: 20px; }
.mb-20 { margin-bottom: 20px; }
.muted { color: var(--text-muted); }

/* ── Chatbot UI Extension ───────────────────────────── */
.ai-chat-widget {
  position: fixed; bottom: 20px; right: 20px; width: 360px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.15);
  z-index: 1000; display: flex; flex-direction: column;
  overflow: hidden; transition: all 0.3s ease;
  border: 1px solid var(--border);
}
.chat-header {
  padding: 14px 20px;
  background: var(--sidebar-bg); color: white;
  display: flex; justify-content: space-between; align-items: center;
  cursor: pointer;
}
.chat-title { font-weight: 600; font-size: 14px; }
.chat-title small { font-weight: 400; opacity: 0.8; }
.chat-body { display: flex; flex-direction: column; height: 400px; background: #f8fafc; }
.chat-messages {
  flex: 1; padding: 16px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px;
}
.chat-message {
  padding: 10px 14px; border-radius: 12px; font-size: 13px; line-height: 1.4; max-width: 85%;
}
.chat-message.model { background: white; border: 1px solid var(--border); align-self: flex-start; border-bottom-left-radius: 2px; }
.chat-message.user { background: var(--primary); color: white; align-self: flex-end; border-bottom-right-radius: 2px; }
.chat-message.loading { background: transparent; font-style: italic; color: var(--text-muted); border: none; }
.chat-input-area {
  display: flex; padding: 12px; border-top: 1px solid var(--border); gap: 8px; background: white;
}
.chat-input-area input { flex: 1; margin: 0; }
.chat-btn { background: var(--primary); color: white; border: none; border-radius: 8px; padding: 0 14px; font-weight: 600; cursor: pointer; }

/* ── Focus Timer Popup ──────────────────────────────── */
.focus-btn { background: var(--primary); color: white; padding: 12px 18px; border: none; border-radius: 8px; font-size: 15px; font-weight: 600; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 10px rgba(37,99,235,0.2); }
.focus-btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 6px 15px rgba(37,99,235,0.3); }
.popup { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(17,24,39,0.7); justify-content: center; align-items: center; z-index: 2000; backdrop-filter: blur(4px); }
.popup-content { background: white; padding: 30px; border-radius: 12px; width: 320px; box-shadow: 0 10px 40px rgba(0,0,0,0.2); transform: scale(0.95); animation: popupAnim 0.3s forwards ease-out; box-sizing: border-box; }
@keyframes popupAnim { to { transform: scale(1); } }
.popup-content h2 { margin-top: 0; margin-bottom: 20px; text-align: center; }
.popup-content input { width: 100%; padding: 10px; margin-top: 6px; margin-bottom: 16px; box-sizing: border-box; }
.popup-btn-row { display: flex; gap: 10px; margin-top: 10px; }
.close-btn { background: #e11d48; } .close-btn:hover { background: #be123c; }

.floating-timer-widget { position: fixed; bottom: 20px; left: 20px; width: 260px; background: white; border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 10px 40px rgba(0,0,0,0.15); z-index: 2000; display: flex; flex-direction: column; align-items: center; padding: 20px; box-sizing: border-box; animation: slideUpWidget 0.4s ease forwards; transform-origin: bottom left; transition: all 0.3s ease; }
@keyframes slideUpWidget { 0%{transform:translateY(30px);opacity:0} 100%{transform:translateY(0);opacity:1} }
.floating-timer-widget h3 { margin: 0; font-size: 13px; color: var(--text-muted); text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px; text-align: center; }
#popupTimerDisplay { font-size: 36px; font-weight: 700; color: var(--text-dark); font-family: monospace; margin: 10px 0; }
.smart-suggestion { font-size: 13px; background: #eff6ff; color: var(--primary); padding: 10px 14px; border-radius: 8px; text-align: center; width: 100%; box-sizing: border-box; line-height: 1.4; margin-bottom: 15px; }
.tree-container { position: relative; width: 80px; height: 100px; margin-bottom: 15px; display: flex; align-items: flex-end; justify-content: center; }
.tree-bg { font-size: 80px; line-height: 1; filter: grayscale(100%); opacity: 0.2; position: absolute; bottom: 0; }
.tree-progress { position: absolute; bottom: 0; height: 0%; overflow: hidden; transition: height 1s linear; width: 100%; display: flex; justify-content: center; left: 0; right: 0; }
.tree-fg { font-size: 80px; line-height: 1; position: absolute; bottom: 0; }
#btnAbandon { font-size: 12px; padding: 8px; font-weight: 600; width: 100%; }

/* ── Responsive ─────────────────────────────────────── */
@media(max-width:900px){
  .cards, .two-col { grid-template-columns: 1fr; }
  .sidebar { transform: translateX(-100%); transition: 0.3s; }
  .sidebar.open { transform: translateX(0); }
  .main { margin-left: 0; width: 100%; }
}
  </style>
  {% block head %}{% endblock %}
</head>
<body>

{% if session.user_id %}
<!-- Sidebar Navigation -->
<div class="sidebar" id="sidebar">
  <a href="/dashboard" class="logo">StudyAI</a>
  <a href="{{ url_for('dashboard') }}" class="nav-link {% if request.endpoint=='dashboard' %}active{% endif %}">Dashboard</a>
  <a href="{{ url_for('timer') }}" class="nav-link {% if request.endpoint=='timer' %}active{% endif %}">Focus Timer ⏱️</a>
  <a href="{{ url_for('add_session') }}" class="nav-link {% if request.endpoint=='add_session' %}active{% endif %}">Add Session</a>
  <a href="{{ url_for('forest') }}" class="nav-link {% if request.endpoint=='forest' %}active{% endif %}">My Forest 🌲</a>
  <a href="{{ url_for('analytics') }}" class="nav-link {% if request.endpoint=='analytics' %}active{% endif %}">Analytics</a>
  <a href="{{ url_for('academic') }}" class="nav-link {% if request.endpoint=='academic' %}active{% endif %}">Academics</a>
  <a href="{{ url_for('history') }}" class="nav-link {% if request.endpoint=='history' %}active{% endif %}">History</a>
  <a href="{{ url_for('profile') }}" class="nav-link {% if request.endpoint=='profile' %}active{% endif %}">Profile</a>
  <a href="{{ url_for('logout') }}" class="nav-link logout">Logout</a>
</div>
{% endif %}

<div class="main {% if not session.user_id %}full-width{% endif %}">
  <header class="top-header">
    <h1>Smart Study Tracker</h1>
    {% if session.user_id %}
    <div class="profile">
      <span>Welcome, {{ session.user_name.split()[0] if session.user_name else 'User' }}</span>
      <div class="avatar">{{ session.user_name[0]|upper if session.user_name else 'U' }}</div>
    </div>
    {% endif %}
  </header>

  <section class="content">
    {% set messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      {% for category, message in messages %}
        <div class="alert alert-{{ category }}">{{ message }}</div>
      {% endfor %}
    {% endif %}

    {% block content %}
    {% endblock %}
  </section>

  <footer style="text-align: center; padding: 20px; font-size: 13px; color: var(--text-muted); border-top: 1px solid var(--border); margin-top: auto; background: white;">
    <a href="{{ url_for('privacy') }}" style="color: var(--primary); text-decoration: none; margin-right: 15px; font-weight: 500;">Privacy Policy</a>
    <span>&copy; 2026 Smart Study Tracker. All Rights Reserved.</span>
  </footer>
</div>

{% if session.user_id %}
<!-- Floating Forest Timer Widget -->
<div id="activePopupSession" class="floating-timer-widget" style="display:none;">
   <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 5px;">
     <h3 id="popupFocusSubject" style="margin: 0; flex: 1; text-align: left;"></h3>
     <button class="btn btn-outline" style="padding: 2px 6px; font-size: 14px; border: none; cursor: pointer; color: var(--text-muted); background: transparent; border-radius: 4px; box-shadow: none;" onclick="togglePiP()" title="Pop out to floating window">🪟</button>
   </div>
   <div id="popupTimerDisplay">25:00</div>
   
   <div class="tree-container">
     <div class="tree-bg">🌲</div>
     <div id="treeProgress" class="tree-progress">
       <div class="tree-fg">🌲</div>
     </div>
   </div>
   
   <div id="smartSuggestion" class="smart-suggestion">Ready to focus?</div>
   <button class="btn btn-danger btn-inline" id="btnAbandon" onclick="abandonPopupTimer()" style="width: 100%;">Give Up 🍂</button>
</div>

<!-- Modal Popup -->
<div id="timerPopupModal" class="popup">
  <div class="popup-content">
    <h2>Focus Timer</h2>
    <label>Subject Name</label>
    <input type="text" id="popupSubjectName" placeholder="Example: Python">
    <label>Focus Duration (minutes)</label>
    <input type="number" id="popupFocusMinutes" value="25">
    <div class="popup-btn-row">
      <button onclick="startPopupTimer()" class="btn">Start Focus</button>
      <button onclick="closePopupTimer()" class="btn close-btn">Cancel</button>
    </div>
  </div>
</div>

<!-- Floating Chat Widget -->
<div id="aiChatWidget" class="ai-chat-widget">
  <div class="chat-header" onclick="toggleChat()">
    <span class="chat-title">🎓 Prof. AI <small>(B.Tech CSE)</small></span>
    <span id="chatToggleIcon" class="chat-icon">▲</span>
  </div>
  <div id="chatBody" class="chat-body" style="display: none;">
    <div id="chatMessages" class="chat-messages">
      <div class="chat-message model">Class is in session. What academic or technical inquiry do you have today?</div>
    </div>
    <div class="chat-input-area">
      <input type="text" id="chatInput" placeholder="Ask your professor..." onkeypress="handleChatKey(event)">
      <button onclick="sendChatMessage()" class="chat-btn">Send</button>
    </div>
  </div>
</div>
{% endif %}

<script>
// script.js – Client-side functionality for Smart Study Tracker

document.addEventListener('DOMContentLoaded', () => {

  // Auto-dismiss alerts after 5 seconds
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.opacity = '0';
      alert.style.transform = 'translateY(-8px)';
      alert.style.transition = 'all .4s ease';
      setTimeout(() => alert.remove(), 400);
    }, 5000);
  });

  // Auto-dismiss goal toast after 7 seconds
  const goalToast = document.getElementById('goalNotification');
  if (goalToast) {
    setTimeout(() => {
      goalToast.style.transition = 'all 0.4s ease';
      goalToast.style.opacity = '0';
      goalToast.style.transform = 'translateY(-10px)';
      setTimeout(() => goalToast.remove(), 400);
    }, 7000);
  }

  // Simple animation effect on hover for cards (As requested)
  document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("mouseenter", () => {
      card.style.transform = "translateY(-4px)";
      card.style.transition = "transform 0.3s ease, box-shadow 0.3s ease";
      card.style.boxShadow = "0 8px 25px rgba(0,0,0,0.06)";
    });
    card.addEventListener("mouseleave", () => {
      card.style.transform = "translateY(0)";
      card.style.boxShadow = "0 4px 15px rgba(0,0,0,0.03)";
    });
  });

  // Highlight active sidebar link
  const currentPath = window.location.pathname;
  document.querySelectorAll('.sidebar a').forEach(link => {
    if (link.getAttribute('href') === currentPath && !link.classList.contains('logout') && !link.classList.contains('logo')) {
      link.classList.add('active');
    }
  });
});

// ── AI Chatbot Logic ──────────────────────────────────────
const chatHistory = [];

function toggleChat() {
  const body = document.getElementById('chatBody');
  const icon = document.getElementById('chatToggleIcon');
  if (body.style.display === 'none') {
    body.style.display = 'flex';
    icon.style.transform = 'rotate(180deg)';
  } else {
    body.style.display = 'none';
    icon.style.transform = 'rotate(0deg)';
  }
}

function handleChatKey(e) {
  if (e.key === 'Enter') sendChatMessage();
}

async function sendChatMessage() {
  const input = document.getElementById('chatInput');
  const text = input.value.trim();
  if (!text) return;
  input.value = '';

  const messagesDiv = document.getElementById('chatMessages');

  // Add user message
  chatHistory.push({ role: 'user', content: text });
  const userMsg = document.createElement('div');
  userMsg.className = 'chat-message user';
  userMsg.textContent = text;
  messagesDiv.appendChild(userMsg);

  // Add loading
  const loading = document.createElement('div');
  loading.className = 'chat-message model loading';
  loading.textContent = 'Professor is typing...';
  messagesDiv.appendChild(loading);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: chatHistory })
    });
    const data = await res.json();

    // Remove loading
    if(messagesDiv.contains(loading)) messagesDiv.removeChild(loading);

    // Add model response
    const replyText = data.reply || "No response";
    chatHistory.push({ role: 'model', content: replyText });

    const modelMsg = document.createElement('div');
    modelMsg.className = 'chat-message model';
    modelMsg.innerHTML = replyText.replace(/\n/g, '<br/>');
    messagesDiv.appendChild(modelMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  } catch(e) {
    if(messagesDiv.contains(loading)) messagesDiv.removeChild(loading);
    const err = document.createElement('div');
    err.className = 'chat-message model';
    err.style.color = '#ef4444';
    err.textContent = "Professor's connection timed out.";
    messagesDiv.appendChild(err);
  }
}

// ── Focus Timer Popup Logic ────────────────────────────────
const STORAGE_KEY = 'studyai_focus_session';
let popupCountdown;
let suggestionInterval;
let endTime = null;
let totalDuration = null;
let focusSubject = "";

// PiP Variables
let pipWindow = null;
let originalWidgetParent = null;
let originalWidgetNextSibling = null;

async function togglePiP() {
  const widget = document.getElementById("activePopupSession");
  if (!widget) return;

  if (pipWindow) {
    pipWindow.close();
    return;
  }

  if ('documentPictureInPicture' in window) {
    try {
      pipWindow = await documentPictureInPicture.requestWindow({
        width: 300,
        height: 380,
      });

      // copy styles
      [...document.styleSheets].forEach((styleSheet) => {
        try {
           const cssRules = [...styleSheet.cssRules].map((rule) => rule.cssText).join('');
           const style = document.createElement('style');
           style.textContent = cssRules;
           pipWindow.document.head.appendChild(style);
        } catch (e) {
           const link = document.createElement('link');
           link.rel = 'stylesheet';
           link.type = styleSheet.type;
           link.media = styleSheet.media;
           link.href = styleSheet.href;
           pipWindow.document.head.appendChild(link);
        }
      });

      pipWindow.document.body.style.margin = '0';
      pipWindow.document.body.style.display = 'flex';
      pipWindow.document.body.style.justifyContent = 'center';
      pipWindow.document.body.style.alignItems = 'center';
      pipWindow.document.body.style.background = 'white';

      originalWidgetParent = widget.parentNode;
      originalWidgetNextSibling = widget.nextSibling;
      pipWindow.document.body.appendChild(widget);

      widget.style.position = 'relative'; 
      widget.style.bottom = 'auto';
      widget.style.left = 'auto';
      widget.style.width = '100%';
      widget.style.height = '100vh';
      widget.style.boxShadow = 'none';
      widget.style.borderRadius = '0';
      widget.style.border = 'none';

      pipWindow.addEventListener("pagehide", () => {
         widget.style.position = 'fixed';
         widget.style.bottom = '20px';
         widget.style.left = '20px';
         widget.style.width = '260px';
         widget.style.height = 'auto';
         widget.style.boxShadow = '0 10px 40px rgba(0,0,0,0.15)';
         widget.style.borderRadius = '16px';
         widget.style.border = '1px solid var(--border)';
         
         if(originalWidgetParent) originalWidgetParent.insertBefore(widget, originalWidgetNextSibling);
         pipWindow = null;
      });
    } catch (err) {
      console.error(err);
      alert("Failed to open PiP window. Please ensure your browser supports Document Picture-in-Picture.");
    }
  } else {
    alert("Your browser does not cleanly support Document Picture-in-Picture API. Please try Google Chrome or Edge.");
  }
}

const HEALTH_TIPS = [
  "Take a sip of water! 💧",
  "Postural check: sit up straight! 🪑",
  "Rest your eyes for 20 seconds. 👁️",
  "Don't forget to breathe deeply. 🌬️",
  "You're doing great! Keep it up. 🚀",
  "A clear desk is a clear mind. ✨",
  "Stretch your arms and neck! 🧘"
];

function updateSuggestion() {
  const tip = HEALTH_TIPS[Math.floor(Math.random() * HEALTH_TIPS.length)];
  const el = document.getElementById("smartSuggestion");
  if(el) el.innerText = tip;
}

function renderTimerState() {
  const now = Date.now();
  if (!endTime || now >= endTime) return false; // expired

  let timeLeft = Math.floor((endTime - now) / 1000);
  let min = Math.floor(timeLeft / 60);
  let sec = timeLeft % 60;
  
  const display = document.getElementById("popupTimerDisplay");
  if(display) display.innerText = min + ":" + (sec<10?"0":"") + sec;
  document.title = `(${min}:${sec<10?"0":""}${sec}) Focusing`;
  
  // Tree Progress
  let elapsed = totalDuration - timeLeft;
  let percent = Math.min(100, (elapsed / totalDuration) * 100);
  const prog = document.getElementById("treeProgress");
  if(prog) prog.style.height = percent + "%";
  
  return true;
}

function openPopupTimer(){
  const modal = document.getElementById("timerPopupModal");
  if(modal) modal.style.display="flex";
}

function closePopupTimer(){
  const modal = document.getElementById("timerPopupModal");
  if(modal) modal.style.display="none";
}

function startPopupTimer(){
  let subj = document.getElementById("popupSubjectName").value || "Focus Session";
  let mins = parseInt(document.getElementById("popupFocusMinutes").value);
  if(!mins || mins <= 0) mins = 25;
  
  focusSubject = subj;
  totalDuration = mins * 60;
  endTime = Date.now() + (totalDuration * 1000);
  
  // Save state
  localStorage.setItem(STORAGE_KEY, JSON.stringify({
    subject: focusSubject,
    endTime: endTime,
    totalDuration: totalDuration
  }));
  
  closePopupTimer();
  beginCountdown();
}

function beginCountdown() {
  const subjEl = document.getElementById("popupFocusSubject");
  if(subjEl) subjEl.innerText = "Focusing on: " + focusSubject;
  
  const activeSess = document.getElementById("activePopupSession");
  if(activeSess) activeSess.style.display="flex";
  
  const fb = document.querySelector('.focus-btn');
  if(fb) fb.style.display="none"; // hide start btn if on dashboard
  
  if(popupCountdown) clearInterval(popupCountdown);
  if(suggestionInterval) clearInterval(suggestionInterval);

  renderTimerState();
  updateSuggestion();
  suggestionInterval = setInterval(updateSuggestion, 60000); // Tip every 60s
  
  popupCountdown = setInterval(()=>{
    const active = renderTimerState();
    if(!active) {
      completePopupTimer();
    }
  }, 1000);
}

function completePopupTimer() {
  clearInterval(popupCountdown);
  clearInterval(suggestionInterval);
  localStorage.removeItem(STORAGE_KEY);
  
  document.title = "Smart Study Tracker";
  const prog = document.getElementById("treeProgress");
  if(prog) prog.style.height = "100%";
  
  try { new Audio("https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3").play(); } catch(e){}
  
  if (pipWindow) {
    pipWindow.close();
  }

  setTimeout(() => {
    alert("Focus session completed! Your tree is fully grown! 🌲");
    const activeSess = document.getElementById("activePopupSession");
    if(activeSess) activeSess.style.display="none";
    const fb = document.querySelector('.focus-btn');
    if(fb) fb.style.display="block";
    
    savePopupSession(focusSubject, totalDuration);
  }, 500);
}

function abandonPopupTimer() {
  if(!confirm("Are you sure you want to give up? Your tree will die! 🍂")) return;
  clearInterval(popupCountdown);
  clearInterval(suggestionInterval);
  localStorage.removeItem(STORAGE_KEY);
  
  if (pipWindow) {
    pipWindow.close();
  }

  document.title = "Smart Study Tracker";
  const activeSess = document.getElementById("activePopupSession");
  if(activeSess) activeSess.style.display="none";
  const fb = document.querySelector('.focus-btn');
  if(fb) fb.style.display="block";
}

function savePopupSession(subject, durationSecs){
  fetch("/save-session",{
    method:"POST",
    headers:{ "Content-Type":"application/json" },
    body:JSON.stringify({ subject: subject, hours: parseFloat((durationSecs/3600).toFixed(4)) })
  }).then(res => res.json()).then(data => {
    if(data.status === 'saved') {
      window.location.reload(); 
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
   const stateStr = localStorage.getItem(STORAGE_KEY);
   if(stateStr) {
     const state = JSON.parse(stateStr);
     if(Date.now() < state.endTime) {
        focusSubject = state.subject;
        endTime = state.endTime;
        totalDuration = state.totalDuration;
        beginCountdown();
     } else {
        localStorage.removeItem(STORAGE_KEY);
     }
   }
});
</script>
{% block scripts %}{% endblock %}
</body>
</html>
"""

TEMPLATE_LOGIN = r"""{% extends "base.html" %}
{% block content %}
<div class="form-container">
  <h2>Login</h2>
  {% if error %}
  <div class="alert alert-error">{{ error }}</div>
  {% endif %}
  <form method="POST">
    <div class="form-group">
      <label>Email</label>
      <input type="email" name="email" placeholder="Enter your email" required autofocus>
    </div>
    <div class="form-group">
      <label>Password</label>
      <input type="password" name="password" placeholder="Enter your password" required>
    </div>
    <button class="btn" type="submit">Login</button>
    <p class="text-center mt-20 muted">New user? <a href="/register">Register</a></p>
  </form>
</div>
{% endblock %}
"""

TEMPLATE_REGISTER = r"""{% extends "base.html" %}
{% block content %}
<div class="form-container">
  <h2>Create Account</h2>
  {% if error %}
  <div class="alert alert-error">{{ error }}</div>
  {% endif %}
  <form method="POST">
    <div class="form-group">
      <label>Full Name</label>
      <input type="text" name="name" placeholder="John Doe" required autofocus>
    </div>
    <div class="form-group">
      <label>Email</label>
      <input type="email" name="email" placeholder="example@college.edu" required>
    </div>
    <div class="form-group">
      <label>Password</label>
      <input type="password" name="password" placeholder="At least 6 characters" required>
    </div>
    <button class="btn" type="submit">Register</button>
    <p class="text-center mt-20 muted">Already have an account? <a href="/login">Login</a></p>
  </form>
</div>
{% endblock %}
"""

TEMPLATE_DASHBOARD = r"""{% extends "base.html" %}
{% block title %}Dashboard – Smart Study Tracker{% endblock %}
{% block content %}

<!-- Daily Goal Notification Toast -->
{% if stats.hours_today is defined and stats.hours_today > 0 and stats.hours_today < 2.0 %}
<div class="toast-notification" id="goalNotification">
  <div class="toast-icon">🎯</div>
  <div class="toast-body">
    <strong>Keep going!</strong> You're only {{ (2.0 - stats.hours_today)|round(1) }} hours away from your daily goal.
  </div>
  <button class="toast-close" onclick="this.parentElement.style.display='none'">&times;</button>
</div>
{% elif stats.hours_today is defined and stats.hours_today >= 2.0 %}
<div class="toast-notification success" id="goalNotification">
  <div class="toast-icon">🎉</div>
  <div class="toast-body">
    <strong>Goal reached!</strong> You've studied {{ stats.hours_today }} hours today. Great work!
    {% if stats.current_streak > 0 %} <span style="margin-left:8px; color:#f59e0b; font-weight:600;">🔥 {{ stats.current_streak }} Day Streak!</span>{% endif %}
  </div>
  <button class="toast-close" onclick="this.parentElement.style.display='none'">&times;</button>
</div>
{% endif %}

<button onclick="openPopupTimer()" class="focus-btn" style="margin-bottom: 20px;">
  Start Focus Session ⏱️
</button>



<div class="cards">
  <div class="card">
    <h3>Total Study Hours</h3>
    <p>{{ stats.total_hours }}h</p>
  </div>
  <div class="card">
    <h3>Avg Daily Hours</h3>
    <p>{{ stats.avg_daily }}h</p>
  </div>
  <div class="card">
    <h3>Productivity Score</h3>
    <p>{{ stats.productivity_score }}%</p>
  </div>
  <div class="card">
    <h3>Daily Streak</h3>
    <p>🔥 {{ stats.current_streak }} <span style="font-size:14px; color:#6b7280; font-weight:500;">Days</span></p>
  </div>
</div>

<div class="two-col">
  <div class="card align-left">
    <h3 class="card-title">Subject Highlights</h3>
    <div class="highlight-row">
      <span class="highlight-label">🔥 Most Studied</span>
      <span class="highlight-value" style="color:var(--primary)">{{ stats.most_studied }}</span>
    </div>
    <div class="highlight-row">
      <span class="highlight-label">💤 Needs Attention</span>
      <span class="highlight-value" style="color:#ef4444">{{ stats.least_studied }}</span>
    </div>
    <div class="highlight-row">
      <span class="highlight-label">⭐ Avg Rating</span>
      <span class="highlight-value">
        {% for i in range(stats.avg_rating|int) %}★{% endfor %}
        {% for i in range(5 - stats.avg_rating|int) %}☆{% endfor %}
        ({{ stats.avg_rating }})
      </span>
    </div>
    <div class="highlight-row">
      <span class="highlight-label">✅ Total Sessions</span>
      <span class="highlight-value">{{ stats.total_sessions }}</span>
    </div>
  </div>

  <div class="card align-left">
    <h3 class="card-title">💡 Smart Suggestions</h3>
    <div id="aiSuggestionsLoader">
      <p class="muted">Loading Professor's suggestions...</p>
    </div>
    <div id="aiSuggestionsList" style="display:none; flex-direction:column;"></div>
  </div>
</div>

<div class="card align-left" id="deadlineCard">
  <h3 class="card-title">⏰ Upcoming Deadlines</h3>
  <div id="deadlineList"><span class="muted">Loading…</span></div>
</div>
{% endblock %}

{% block scripts %}
<script>
fetch('/api/deadlines')
  .then(r => r.json())
  .then(data => {
    const el = document.getElementById('deadlineList');
    if (!data.length) { el.innerHTML = '<span class="muted">No upcoming deadlines set.</span>'; return; }
    el.innerHTML = data.map(d => {
      const cls = d.days < 0 ? 'color: #ef4444' : d.days <= 3 ? 'color: #f59e0b' : 'color: #10b981';
      const label = d.days < 0 ? `${Math.abs(d.days)}d overdue` : d.days === 0 ? 'Today!' : `${d.days} days left`;
      return `<div class="highlight-row"><span>${d.subject}</span> <span class="muted" style="margin-left:auto; margin-right:10px">${d.deadline}</span><span style="font-weight:600;${cls}">${label}</span></div>`;
    }).join('');
  });

fetch('/api/ai_suggestions')
  .then(r => r.json())
  .then(data => {
    const loader = document.getElementById('aiSuggestionsLoader');
    const list = document.getElementById('aiSuggestionsList');
    loader.style.display = 'none';
    list.style.display = 'flex';
    if (!data.suggestions || data.suggestions.length === 0) {
      list.innerHTML = '<p class="muted">Add sessions to see personalized tips.</p>';
      return;
    }
    list.innerHTML = data.suggestions.map(s => `<div class="suggestion-item">${s}</div>`).join('');
  })
  .catch(err => {
    document.getElementById('aiSuggestionsLoader').innerHTML = '<p class="muted" style="color:#ef4444">Professor is currently offline.</p>';
  });
</script>
{% endblock %}
"""

TEMPLATE_TIMER = r"""{% extends "base.html" %}
{% block title %}Focus Timer – Smart Study Tracker{% endblock %}
{% block content %}
<div class="flex justify-between align-center mb-20">
  <h2 style="margin:0; color:var(--text-dark)">Focus Timer ⏱️</h2>
</div>

<div class="card text-center" style="max-width: 500px; margin: 0 auto; padding: 40px;">
  <div class="form-group mb-20">
    <label>What are you focusing on?</label>
    <input type="text" id="focusSubject" list="subjectList" placeholder="e.g. Operating Systems" class="text-center" style="font-size: 16px; font-weight: 500;">
    <datalist id="subjectList">
      {% for s in subjects %}
      <option value="{{ s }}">
      {% endfor %}
    </datalist>
  </div>

  <div id="timerDisplay" style="font-size: 80px; font-weight: 700; font-family: monospace; color: var(--primary); margin: 20px 0;">
    25:00
  </div>

  <div class="flex justify-center gap-10 mb-20">
    <button class="btn btn-inline" id="btnStart" onclick="startTimer()">Start Focus</button>
    <button class="btn btn-outline btn-inline" id="btnPause" onclick="pauseTimer()" style="display:none;">Pause</button>
    <button class="btn btn-danger btn-inline" id="btnReset" onclick="resetTimer()">Reset</button>
  </div>

  <div class="flex justify-center gap-10">
    <button class="btn btn-outline btn-inline text-sm" style="padding: 6px 12px; font-size: 13px;" onclick="setMode(25)">25m</button>
    <button class="btn btn-outline btn-inline text-sm" style="padding: 6px 12px; font-size: 13px;" onclick="setMode(50)">50m</button>
    <button class="btn btn-outline btn-inline text-sm" style="padding: 6px 12px; font-size: 13px;" onclick="setMode(5)">5m Break</button>
  </div>
</div>

<!-- Hidden form to log session natively -->
<form id="logSessionForm" action="{{ url_for('add_session') }}" method="POST" style="display:none;">
    <input type="hidden" name="subject" id="logSubject">
    <input type="hidden" name="hours" id="logHours">
    <input type="hidden" name="date" id="logDate">
    <input type="hidden" name="rating" value="5">
    <input type="hidden" name="notes" value="Logged automatically via Focus Timer">
</form>

<script>
  let defaultTime = 25 * 60;
  let timeLeft = defaultTime;
  let timerInterval = null;

  function updateDisplay() {
    const m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
    const s = (timeLeft % 60).toString().padStart(2, '0');
    document.getElementById('timerDisplay').textContent = `${m}:${s}`;
    document.title = `(${m}:${s}) Focus Timer`;
  }

  function setMode(mins) {
    pauseTimer();
    defaultTime = mins * 60;
    timeLeft = defaultTime;
    updateDisplay();
  }

  function startTimer() {
    if(!document.getElementById('focusSubject').value && defaultTime > 5 * 60) {
      alert("Please specify what you are focusing on first!");
      document.getElementById('focusSubject').focus();
      return;
    }
    if(timerInterval) return;
    document.getElementById('btnStart').style.display = 'none';
    document.getElementById('btnPause').style.display = 'block';

    timerInterval = setInterval(() => {
      if(timeLeft > 0) {
        timeLeft--;
        updateDisplay();
      } else {
        clearInterval(timerInterval);
        timerInterval = null;
        playAlarm();
        handleTimerComplete();
      }
    }, 1000);
  }

  function pauseTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
    document.getElementById('btnStart').style.display = 'block';
    document.getElementById('btnPause').style.display = 'none';
  }

  function resetTimer() {
    pauseTimer();
    timeLeft = defaultTime;
    updateDisplay();
  }

  function playAlarm() {
    try {
      const audio = new Audio('https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3');
      audio.play();
    } catch(e) {}
  }

  function handleTimerComplete() {
    document.getElementById('btnStart').style.display = 'block';
    document.getElementById('btnPause').style.display = 'none';

    if(defaultTime >= 25 * 60) {
        if(confirm("Focus session complete! 🍅 Would you like to log this time to your Study Tracker?")) {
            const subj = document.getElementById('focusSubject').value || 'Deep Work';
            const logHrs = parseFloat((defaultTime / 3600).toFixed(2));

            document.getElementById('logSubject').value = subj;
            document.getElementById('logHours').value = Math.max(0.5, logHrs); // min 0.5 hours for DB constraint
            document.getElementById('logDate').value = new Date().toISOString().split('T')[0];

            document.getElementById('logSessionForm').submit();
        }
    } else {
        alert("Break complete! Time to get back to work.");
        setMode(25);
    }
  }

  updateDisplay();
</script>
{% endblock %}
"""

TEMPLATE_ADD_SESSION = r"""{% extends "base.html" %}
{% block title %}Add Session – Smart Study Tracker{% endblock %}
{% block content %}
<div class="form-container wide">
  <h2>Add Study Session</h2>
  {% if error %}
  <div class="alert alert-error">{{ error }}</div>
  {% endif %}
  {% if success %}
  <div class="alert alert-success">{{ success }}</div>
  {% endif %}
  <form method="POST">
    <div class="flex gap-20">
      <div class="form-group" style="flex:1">
        <label>Subject</label>
        <input type="text" name="subject" required autofocus placeholder="e.g. Data Structures">
      </div>
      <div class="form-group" style="flex:1">
        <label>Study Hours</label>
        <input type="number" name="hours" id="hours" step="0.5" min="0.5" max="24" required placeholder="2.5">
      </div>
    </div>
    <div class="flex gap-20">
      <div class="form-group" style="flex:1">
        <label>Date</label>
        <input type="date" name="date" value="{{ today }}" required>
      </div>
      <div class="form-group" style="flex:1">
        <label>Productivity Rating <small>(1-5)</small></label>
        <select name="rating" required>
          <option value="5">5 - Excellent focus</option>
          <option value="4">4 - Good session</option>
          <option value="3">3 - Average</option>
          <option value="2">2 - Distracted</option>
          <option value="1">1 - Poor</option>
        </select>
      </div>
    </div>
    <div class="form-group">
      <label>Notes <small>(Optional)</small></label>
      <textarea name="notes" placeholder="What did you study?"></textarea>
    </div>
    <div class="form-group">
      <label>Upcoming Deadline <small>(Optional)</small></label>
      <input type="date" name="deadline">
    </div>
    <div class="flex justify-between align-center mt-20">
      <a href="{{ url_for('dashboard') }}" class="btn btn-outline btn-inline">Cancel</a>
      <button class="btn btn-inline" type="submit">Save Session</button>
    </div>
  </form>
</div>
{% endblock %}
"""

TEMPLATE_HISTORY = r"""{% extends "base.html" %}
{% block title %}History – Smart Study Tracker{% endblock %}
{% block content %}
<div class="flex justify-between align-center mb-20">
  <h2 style="margin:0; color:var(--text-dark)">Study History</h2>
  <a href="{{ url_for('history') }}" class="btn btn-outline btn-inline text-sm">Clear Filters</a>
</div>

<div class="card align-left mb-20" style="padding: 20px;">
  <form method="GET" class="flex gap-20 align-center">
    <div style="flex:1">
      <label>Filter by Subject</label>
      <select name="subject" onchange="this.form.submit()" style="margin-bottom:0">
        <option value="">All Subjects</option>
        {% for subj in subjects %}
        <option value="{{ subj }}" {% if subj == filter_subject %}selected{% endif %}>{{ subj }}</option>
        {% endfor %}
      </select>
    </div>
    <div style="flex:1">
      <label>Filter by Date</label>
      <input type="date" name="date" value="{{ filter_date }}" onchange="this.form.submit()" style="margin-bottom:0">
    </div>
  </form>
</div>

<div class="chart-box" style="padding:0; border:none; box-shadow:none;">
  <table class="data-table">
    <thead>
      <tr>
        <th>Subject</th>
        <th>Date</th>
        <th>Hours</th>
        <th>Rating</th>
        <th>Notes</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      {% for s in sessions %}
      <tr id="row-{{ s.id }}">
        <td style="font-weight:600">{{ s.subject }}</td>
        <td class="muted">{{ s.date }}</td>
        <td><span style="background:#eff6ff; color:var(--primary); padding:2px 8px; border-radius:4px; font-weight:600">{{ s.hours }}h</span></td>
        <td>{{ s.rating }}/5</td>
        <td class="muted" style="max-width:300px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
          {{ s.notes or '—' }}
        </td>
        <td>
          <button class="btn btn-danger btn-inline" onclick="deleteSession('{{ s.id }}')" style="padding:6px 12px; font-size:12px;">Delete</button>
        </td>
      </tr>
      {% else %}
      <tr>
        <td colspan="6" class="text-center muted" style="padding:40px;">No sessions found matching your criteria.</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<script>
async function deleteSession(id) {
  if (!confirm("Are you sure you want to delete this session?")) return;
  try {
    const res = await fetch(`/api/delete_session/${id}`, { method: 'DELETE' });
    const data = await res.json();
    if (data.status === 'ok') {
      const row = document.getElementById(`row-${id}`);
      if (row) {
        row.style.display = 'none';
      }
    } else {
      alert("Failed: " + data.message);
    }
  } catch (err) {
    alert("An error occurred.");
  }
}
</script>
{% endblock %}
"""

TEMPLATE_ANALYTICS = r"""{% extends "base.html" %}
{% block title %}Analytics – Smart Study Tracker{% endblock %}
{% block head %}
  <!-- Plotly.js -->
  <script src="https://cdn.plot.ly/plotly-2.32.0.min.js" charset="utf-8"></script>
{% endblock %}

{% block content %}
<div class="flex justify-between align-center mb-20">
  <h2 style="margin:0; color:var(--text-dark)">Study Analytics</h2>
</div>

{% if not has_data %}
<div class="card text-center" style="padding: 60px;">
  <p class="muted">No study sessions found. Add some sessions to see your analytics.</p>
  <br>
  <a href="{{ url_for('add_session') }}" class="btn btn-inline">Add Session</a>
</div>
{% else %}

<div class="chart-box">
  <h3 class="card-title">Daily Study Hours (Last 7 Days)</h3>
  <div id="dailyChart" style="width:100%; height:400px; margin-top:20px;"></div>
</div>

<div class="two-col">
  <div class="chart-box" style="margin-bottom:0">
    <h3 class="card-title">Subject Distribution</h3>
    <div id="subjectChart" style="width:100%; height:300px; margin-top:20px;"></div>
  </div>

  <div class="chart-box" style="margin-bottom:0">
    <h3 class="card-title">Productivity by Subject</h3>
    <div id="productivityChart" style="width:100%; height:300px; margin-top:20px;"></div>
  </div>
</div>

<script>
  const chartData = {{ chart_data|safe }};

  // Apply light theme layout modifications dynamically to Plotly
  const lightLayout = {
    font: { family: 'Poppins, sans-serif', color: '#6b7280' },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    margin: { t: 10, r: 10, b: 40, l: 40 },
    xaxis: { gridcolor: '#e5e7eb', zerolinecolor: '#e5e7eb' },
    yaxis: { gridcolor: '#e5e7eb', zerolinecolor: '#e5e7eb' }
  };

  if(chartData.daily) {
    const dailyLayout = Object.assign({}, chartData.daily.layout, lightLayout);
    Plotly.newPlot('dailyChart', chartData.daily.data, dailyLayout, {responsive: true});
  }

  if(chartData.subject) {
    const subjLayout = Object.assign({}, chartData.subject.layout, lightLayout, {margin: { t:10, b:10, l:10, r:10}});
    Plotly.newPlot('subjectChart', chartData.subject.data, subjLayout, {responsive: true});
  }

  if(chartData.productivity) {
    const prodLayout = Object.assign({}, chartData.productivity.layout, lightLayout);
    Plotly.newPlot('productivityChart', chartData.productivity.data, prodLayout, {responsive: true});
  }
</script>
{% endif %}
{% endblock %}
"""

TEMPLATE_ACADEMIC = r"""{% extends "base.html" %}
{% block title %}Academics – Smart Study Tracker{% endblock %}
{% block content %}
<div class="flex justify-between align-center mb-20">
  <h2 style="margin:0; color:var(--text-dark)">Semester Academic Tracker 🎓</h2>
</div>

<!-- Alert for AI -->
<div class="alert" style="background: #e0e7ff; color: #3730a3; border-left: 4px solid #4f46e5;">
  <strong>Professor AI Active:</strong> Enter your Mid-Sem marks below. The AI Chatbot is tracking these and will mathematically calculate your rigorous End-Sem survival plan!
</div>

{% if error %}
<div class="alert alert-error">{{ error }}</div>
{% endif %}
{% if success %}
<div class="alert alert-success">{{ success }}</div>
{% endif %}

<div class="two-col mt-20">
    <div class="form-container" style="margin:0">
      <h3 style="margin-top:0">Log Mid-Sem Score</h3>
      <form method="POST">
        <div class="form-group">
          <label>Subject</label>
          <input type="text" name="subject" required placeholder="e.g. Operating Systems">
        </div>
        <div class="form-row">
            <div class="form-group">
                <label>Semester</label>
                <input type="number" name="semester" min="1" max="8" value="4" required>
            </div>
            <div class="form-group">
                <label>Mid-Sem Marks <small>(out of 30)</small></label>
                <input type="number" name="mid_sem" step="0.5" min="0" max="30" required>
            </div>
        </div>
        <div class="form-group">
          <label>Target End Grade</label>
          <select name="target" required>
            <option value="O">O (90+ / Outstanding)</option>
            <option value="A+">A+ (85+ / Excellent)</option>
            <option value="A">A (80+ / Very Good)</option>
            <option value="B">B (70+ / Good)</option>
            <option value="C">C (60+ / Average)</option>
            <option value="PASS">PASS (40+ / Bare Minimum)</option>
          </select>
        </div>

        <button class="btn btn-inline mt-10" type="submit" style="width:100%">Calculate Target</button>
      </form>
    </div>

    <!-- Marks Table -->
    <div class="chart-box" style="margin:0; padding:0; border:none; box-shadow:none;">
      <table class="data-table">
        <thead>
          <tr>
            <th>Sem</th>
            <th>Subject</th>
            <th>Mid-Sem (/30)</th>
            <th>Target</th>
            <th>Required End-Sem (/60)</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for m in marks %}
          <tr id="row-{{ m.record_id }}">
            <td class="muted">{{ m.semester }}</td>
            <td style="font-weight:600">{{ m.subject }}</td>
            <td><span style="font-size:14px; font-weight:600; color:var(--text-dark)">{{ m.mid_sem_score }}</span></td>
            <td><span style="background:#f3f4f6; color:#4b5563; padding:2px 8px; border-radius:4px; font-weight:600; font-size:12px">{{ m.target_grade }}</span></td>
            <td>
                {% if m.required_end_sem > 60 %}
                    <span style="color:#ef4444; font-weight:700;">Impossible 💀</span>
                {% elif m.required_end_sem > 50 %}
                    <span style="color:#f59e0b; font-weight:700;">{{ m.required_end_sem }} ⚠️</span>
                {% else %}
                    <span style="color:#10b981; font-weight:700;">{{ m.required_end_sem }} ✓</span>
                {% endif %}
            </td>
            <td>
              <button class="btn btn-danger btn-inline" onclick="deleteMark('{{ m.record_id }}')" style="padding:4px 8px; font-size:11px;">Drop</button>
            </td>
          </tr>
          {% else %}
          <tr>
            <td colspan="6" class="text-center muted" style="padding:40px;">No marks recorded. Begin tracking to trigger AI strategy!</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
</div>

<script>
async function deleteMark(id) {
  if (!confirm("Are you sure you want to drop this subject requirement?")) return;
  try {
    const res = await fetch(`/api/delete_mark/${id}`, { method: 'DELETE' });
    const data = await res.json();
    if (data.status === 'ok') {
      const row = document.getElementById(`row-${id}`);
      if (row) {
        row.style.display = 'none';
      }
    } else {
      alert("Failed: " + data.message);
    }
  } catch (err) {
    alert("An error occurred.");
  }
}
</script>
{% endblock %}
"""

TEMPLATE_PROFILE = r"""{% extends "base.html" %}
{% block title %}Profile Settings – Smart Study Tracker{% endblock %}
{% block content %}
<div class="form-container wide">
  <h2>Profile & Settings</h2>

  {% if success %}
  <div class="alert alert-success">{{ success }}</div>
  {% endif %}

  <form method="POST">
    <div class="form-group">
      <label>Your Name</label>
      <input type="text" name="name" value="{{ user['name']|default('') }}" required>
    </div>

    <div class="form-group">
      <label>Email <small>(Read-only)</small></label>
      <input type="email" value="{{ user['email'] }}" disabled>
    </div>

    <hr style="border:0; border-top:1px solid var(--border); margin:30px 0;">
    <h3 style="margin-top:0">Academic Goals</h3>
    <p class="muted" style="font-size:14px">Set your daily target so the Professor can track your progress.</p>

    <div class="form-group">
      <label>Daily Minimum Study Goal (Hours)</label>
      <input type="number" name="min_daily_hrs" step="0.5" min="0" value="{{ user.get('min_daily_hrs', 2.0) }}" required>
    </div>

    <div class="flex justify-between align-center mt-20">
      <a href="{{ url_for('dashboard') }}" class="btn btn-outline btn-inline">Cancel</a>
      <button class="btn btn-inline" type="submit">Update Profile</button>
    </div>
  </form>
</div>
{% endblock %}
"""

TEMPLATE_PRIVACY = r"""{% extends "base.html" %}
{% block title %}Privacy Policy – Smart Study Tracker{% endblock %}
{% block content %}
<div class="form-container wide" style="text-align: left;">
  <h2>Privacy Policy & Copyright Info</h2>
  <div style="font-size: 14px; line-height: 1.6; color: var(--text-dark);">
    <h3>1. Data Collection</h3>
    <p>We collect your name, email, and study session records (subject, duration, notes, and academic scores). This information is solely used to track your study habits and generate personalized productivity insights using our built-in AI tools.</p>

    <h3>2. Data Security</h3>
    <p>We use standard hashing and session guarding to keep your study data private. Your sessions remain attached only to your account and are never sold to third parties.</p>

    <h3>3. Copyright & Intellectual Property</h3>
    <p>&copy; 2026 Smart Study Tracker. All Rights Reserved. This application and its interface structure are protected by copyright laws.</p>

    <div style="margin-top: 30px; text-align: center;">
      <a href="{{ url_for('login') if not session.user_id else url_for('dashboard') }}" class="btn btn-inline">Back</a>
    </div>
  </div>
</div>
{% endblock %}
"""

TEMPLATE_FOREST = r"""{% extends "base.html" %}
{% block title %}My Forest – Smart Study Tracker{% endblock %}
{% block content %}
<div class="cards" style="grid-template-columns: 1fr;">
  <div class="card" style="text-align: center; border-left: 5px solid #10b981;">
    <h2>Your Productivity Forest 🌲</h2>
    <p style="font-size: 16px; color: var(--text-muted); margin-top: 10px;">You have planted <strong>{{ tree_count }}</strong> trees and spent <strong>{{ total_hours }}</strong> hours growing!</p>
  </div>
</div>

<div class="forest-container" style="margin-top: 30px; padding: 40px; background: linear-gradient(to bottom, #dbeafe 0%, #bbf7d0 100%); border-radius: 16px; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; min-height: 400px; border: 1px solid #86efac; box-shadow: inset 0 0 20px rgba(22,163,74,0.05); position: relative; overflow: hidden;">
  <!-- Decorational Sun -->
  <div style="position: absolute; top: 30px; left: 40px; font-size: 60px; filter: drop-shadow(0 0 20px rgba(250,204,21,0.5)); opacity: 0.9;">☀️</div>
  
  {% if tree_count == 0 %}
    <div style="width: 100%; text-align: center; color: #166534; font-weight: 500; font-size: 18px; align-self: center; z-index: 10;">
      Your forest is empty! Start a Focus Session to plant your first tree. 🌱
    </div>
  {% else %}
    {% for i in range(tree_count) %}
       <div class="planted-tree" style="font-size: 54px; animation: popIn 0.5s {{ (i % 20) * 0.05 }}s both; transform-origin: bottom center; z-index: {{ loop.index }}; position: relative;">
         {{ ['🌲', '🌳', '🌴', '🌲', '🌳', '🍎'] | random }}
       </div>
    {% endfor %}
  {% endif %}
</div>

<style>
@keyframes popIn {
  0% { transform: scale(0); opacity: 0; }
  60% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}
.planted-tree {
  margin: -8px 2px;
  filter: drop-shadow(2px 6px 4px rgba(0,0,0,0.15));
  transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.planted-tree:hover {
  transform: scale(1.2) translateY(-10px) !important;
  cursor: pointer;
  z-index: 9999 !important;
}
</style>
{% endblock %}
"""

templates_dict = {
    "base.html": TEMPLATE_BASE,
    "login.html": TEMPLATE_LOGIN,
    "register.html": TEMPLATE_REGISTER,
    "dashboard.html": TEMPLATE_DASHBOARD,
    "timer.html": TEMPLATE_TIMER,
    "add_session.html": TEMPLATE_ADD_SESSION,
    "history.html": TEMPLATE_HISTORY,
    "analytics.html": TEMPLATE_ANALYTICS,
    "academic.html": TEMPLATE_ACADEMIC,
    "profile.html": TEMPLATE_PROFILE,
    "privacy.html": TEMPLATE_PRIVACY,
    "forest.html": TEMPLATE_FOREST,
}
