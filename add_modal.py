import os

# 1. Update css/styles.css
css_code = """
/* ==========================================================================
   CREDITS MODAL
   ========================================================================== */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}
.modal-overlay.active {
    opacity: 1;
    pointer-events: all;
}
.modal-content {
    background: var(--bg-main);
    padding: 3rem;
    border-radius: var(--radius-md);
    text-align: center;
    max-width: 400px;
    width: 90%;
    box-shadow: var(--shadow-hover);
    transform: translateY(20px);
    transition: transform 0.3s ease;
}
.modal-overlay.active .modal-content {
    transform: translateY(0);
}
.modal-content p {
    color: var(--text-muted);
    margin-bottom: 0.5rem;
}
.modal-content h3 {
    margin-bottom: 0.5rem;
}
"""

with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

# 2. Update js/app.js
js_code = """
// 7. CREDITS MODAL LOGIC
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('project-credits-modal');
    const closeBtn = document.getElementById('close-credits-btn');
    
    if (modal && closeBtn) {
        // Show modal on load
        setTimeout(() => {
            modal.classList.add('active');
        }, 100);
        
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });
    }
});
"""

with open('js/app.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

# 3. Update generate_pages.py to inject the modal into index.html
with open('generate_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

modal_html = """
        <div id="project-credits-modal" class="modal-overlay">
            <div class="modal-content">
                <p style="margin-bottom: 20px; color: var(--text-main); font-weight: 500;">This is a Minor/Major Project by:</p>
                <h3>Shivam Tanwar</h3>
                <p>A2305324022</p>
                <p>B.Tech - IT</p>
                <p>2024-2028</p>
                <button id="close-credits-btn" class="btn btn-primary" style="margin-top: 25px; width: 100%;">OK</button>
            </div>
        </div>
        """

# Find where index.html content starts and inject
target = '''    "index.html": {
        "title": "Home",
        "content": """'''

replacement = target + modal_html

new_content = content.replace(target, replacement)

with open('generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Modal code injected successfully.")
