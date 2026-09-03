import openpyxl
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, "System_Design_Roadmap.xlsx")
readme_path = os.path.join(script_dir, "README.md")
svg_path = os.path.join(script_dir, "progress.svg")

if not os.path.exists(excel_path):
    print("Excel file not found at:", excel_path)
    exit(1)

wb = openpyxl.load_workbook(excel_path, data_only=True)
sheet = wb["Master Roadmap"]

modules = []
completed_count = 0

for r in range(2, sheet.max_row + 1):
    no_val = sheet.cell(row=r, column=1).value
    phase = sheet.cell(row=r, column=2).value
    category = sheet.cell(row=r, column=3).value
    name = sheet.cell(row=r, column=4).value
    skills = sheet.cell(row=r, column=5).value
    pri_video = sheet.cell(row=r, column=6).value
    sup_video = sheet.cell(row=r, column=7).value
    practice = sheet.cell(row=r, column=8).value
    status = sheet.cell(row=r, column=9).value
    
    if not name:
        continue
        
    try:
        no_val = int(no_val)
    except (TypeError, ValueError):
        continue
        
    is_completed = (status == "Completed" or status == "Solved")
    if is_completed:
        completed_count += 1
        
    modules.append({
        'no': no_val,
        'phase': phase,
        'category': category,
        'name': name,
        'skills': skills,
        'pri_video': pri_video,
        'sup_video': sup_video,
        'practice': practice,
        'status': "Completed" if is_completed else ("In Progress" if status == "In Progress" else "Not Started"),
        'completed': is_completed
    })

total_modules = len(modules)
pct = (completed_count / total_modules) * 100 if total_modules else 0
fill_width = 400 * (completed_count / total_modules) if total_modules else 0

# Count by phase
phase_stats = {}
for m in modules:
    p = m['phase']
    if p not in phase_stats:
        phase_stats[p] = {'total': 0, 'completed': 0}
    phase_stats[p]['total'] += 1
    if m['completed']:
        phase_stats[p]['completed'] += 1

# Find first unsolved module (Active Target)
active_module = None
for m in modules:
    if not m['completed']:
        active_module = m
        break

# Generate progress.svg
svg_content = f"""<svg width="400" height="60" viewBox="0 0 400 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .track {{
      fill: #e1e4e8;
    }}
    .fill {{
      fill: url(#grad);
      animation: load 2s cubic-bezier(0.4, 0, 0.2, 1) forwards;
      width: 0px;
    }}
    .text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-size: 14px;
      font-weight: 600;
      fill: #24292e;
      opacity: 0;
      animation: fadeIn 0.5s ease-out 1s forwards;
    }}
    @keyframes load {{
      to {{ width: {fill_width:.1f}px; }}
    }}
    @keyframes fadeIn {{
      to {{ opacity: 1; }}
    }}
    @media (prefers-color-scheme: dark) {{
      .track {{
        fill: #21262d;
        stroke: #30363d;
      }}
      .text {{
        fill: #c9d1d9;
      }}
    }}
  </style>
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF512F" />
      <stop offset="100%" stop-color="#DD2476" />
    </linearGradient>
  </defs>
  
  <text x="0" y="18" class="text" style="animation: fadeIn 0.5s ease-out forwards; opacity: 1;">System Design Mastery</text>
  <text x="360" y="18" class="text">{pct:.1f}%</text>

  <rect x="0" y="30" width="400" height="16" rx="8" class="track" />
  <rect x="0" y="30" height="16" rx="8" class="fill" />
</svg>
"""

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

# Target Module Card
active_card = ""
if active_module:
    a_no = active_module['no']
    a_phase = active_module['phase']
    a_cat = active_module['category']
    a_name = active_module['name']
    a_skills = active_module['skills']
    a_pri = active_module['pri_video']
    a_sup = active_module['sup_video']
    a_prac = active_module['practice']

    active_card = f"""---

## 🎯 Active Learning Module (Watch & Practice on the Go)

> **📱 Mobile Dashboard**: Watch your current video lesson and review the key concept flashcards straight from your phone!

### **Lesson #{a_no}: [{a_name}]({a_pri})**
* **Phase:** `{a_phase}` | **Category:** `{a_cat}`
* **Core Concepts:** `{a_skills}`

#### 🎥 Video Resources
* ▶️ **Primary Video (Coder Army):** [Watch Video #{a_no}]({a_pri})
* 💡 **Supplementary Visual Guide:** [Watch Supplementary Deep-Dive]({a_sup})

#### 🛠️ Hands-On Practice Task
> **Assignment:** {a_prac}

---
"""

# Phase descriptions
phase_titles = {
    "Phase 1": "🌐 Phase 1: Web, Networking & REST API Fundamentals (Lessons 1–8)",
    "Phase 2": "💾 Phase 2: Database Deep-Dive (SQL vs NoSQL & Indexing) (Lessons 9–18)",
    "Phase 3": "🏗️ Phase 3: High-Level Design (HLD) Building Blocks (Lessons 19–28)",
    "Phase 4": "📐 Phase 4: Low-Level Design (LLD) & OOP Design Patterns (Lessons 29–34)",
    "Phase 5": "🎯 Phase 5: Real-World Case Studies & Capstones (Lessons 35–40)"
}

content = f"""# 🏛️ System Design: 0 to Hero Placement Roadmap

Welcome to my personal **System Design & Distributed Systems** learning repository! This repo contains a comprehensive, 40-module structured path designed for SDE placement interviews, technical drives, and scalable backend architecture mastery.

<p align="left">
  <img src="https://img.shields.io/badge/System%20Design-{completed_count}%20%2F%20{total_modules}%20Completed-red?style=for-the-badge&logo=youtube" alt="Modules Completed">
  <img src="https://img.shields.io/badge/Track-SDE%20Placement-blue?style=for-the-badge" alt="Track">
  <img src="https://img.shields.io/badge/Focus-REST%20%7C%20SQL%20%7C%20HLD%20%7C%20LLD-orange?style=for-the-badge" alt="Focus">
</p>

---

## 📊 Progress Dashboard

Track my interactive progress through the 5 phases of System Design below:

<p align="left">
  <img src="./progress.svg" alt="System Design Progress" width="400">
</p>

| Phase | Modules Completed | Progress Percentage | Status |
| :--- | :---: | :---: | :---: |
"""

for p_name in ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"]:
    stats = phase_stats.get(p_name, {'total': 0, 'completed': 0})
    p_pct = (stats['completed'] / stats['total']) * 100 if stats['total'] else 0
    indicator = "🟢 Active" if stats['completed'] > 0 else "⚪ Not Started"
    if stats['completed'] == stats['total'] and stats['total'] > 0:
        indicator = "🏆 Completed"
    content += f"| **{p_name}** | {stats['completed']} / {stats['total']} | {p_pct:.1f}% | {indicator} |\n"

content += f"""| **TOTAL** | **{completed_count} / {total_modules}** | **{pct:.1f}%** | **🧠 Engineering Grind** |

{active_card}

## 📚 Repository Structure
```text
system-design/
├── notes/                # Comprehensive cheat-sheets for REST, SQL, Caching & HLD
├── practice/             # Hands-on API specifications, SQL queries & architecture tasks
├── lld-cpp/              # C++ implementations of SOLID design patterns and LRU Cache
├── System_Design_Roadmap.xlsx # Master tracking spreadsheet
└── generate_readme.py    # Auto-generates README and animated SVG
```

---

## 📂 Complete 40-Module Learning Path

"""

for p_name in ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"]:
    p_mods = [m for m in modules if m['phase'] == p_name]
    stats = phase_stats.get(p_name, {'total': 0, 'completed': 0})
    title = phase_titles.get(p_name, p_name)
    
    content += f"""
<details>
<summary><b>{title} ({stats['completed']}/{stats['total']} Completed)</b></summary>
<br>

| No. | Module Name | Key Concepts | Video Link | Practice Task | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
"""
    for m in p_mods:
        status_icon = "✅ Completed" if m['completed'] else ("⏳ In Progress" if m['status'] == "In Progress" else "⚪ Not Started")
        content += f"| {m['no']} | {m['name']} | `{m['skills']}` | [Watch Video]({m['pri_video']}) | {m['practice']} | {status_icon} |\n"
        
    content += "\n</details>\n"

content += """
---

## 🚀 How to Sync Progress

Whenever you finish a video or practice task:
1. Open `System_Design_Roadmap.xlsx` and change the Status to `Completed`.
2. Double-click `sync.bat` (or run `python generate_readme.py` and `git push`).

*“Simplicity is prerequisite for reliability.” – Edsger W. Dijkstra.* 💻🚀
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"SUCCESS: Re-generated README.md and progress.svg for System Design! (Completed: {completed_count}/{total_modules})")
