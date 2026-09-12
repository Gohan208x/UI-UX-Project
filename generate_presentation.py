import os

pages = [
    {
        "file": "title.html",
        "title": "Aura Audio Project",
        "tags": ["Introduction", "Amity University"],
        "desc": "Comprehensive UI/UX design project showcasing modern e-commerce flows, component scalability, and premium aesthetic execution."
    },
    {
        "file": "index.html",
        "title": "Home Page Strategy",
        "tags": ["Visual Hierarchy", "Call to Action", "First Impression"],
        "desc": "The home page acts as the primary hook for users. By utilizing a high-contrast, minimalist hero banner with immense negative space, we instantly convey the brand's 'premium luxury' positioning. The primary CTA (Shop Collection) is placed dead center, reducing cognitive load and driving immediate conversion."
    },
    {
        "file": "shop.html",
        "title": "Product Catalog UX",
        "tags": ["Grid Layout", "Information Architecture", "Scalability"],
        "desc": "The shop utilizes a consistent 3-column CSS Grid layout that scales perfectly across devices. Products are presented with vast white space to emphasize the hardware design. Pricing is displayed prominently below clear, legible typography to prevent 'price shock' and manage user expectations early in the flow."
    },
    {
        "file": "product-p1.html",
        "title": "Product Detail Page (PDP) - Pro Max",
        "tags": ["Tabbed Navigation", "Interactive Elements", "F-Pattern Reading"],
        "desc": "The PDP uses a split-screen design. The high-resolution product image remains fixed on the left while detailed, tabbed content (Description, Reviews, Warranty, Returns) scrolls on the right. This tab system prevents endless vertical scrolling (scroll fatigue) while providing deep, contextual information on demand."
    },
    {
        "file": "product-p2.html",
        "title": "Product Detail Page - Studio",
        "tags": ["Consistency", "Component Reusability", "Visual Anchor"],
        "desc": "Demonstrating the scalability of the PDP template. The exact same UI framework beautifully accommodates a completely different product aesthetic, proving that the underlying wireframe is robust and adaptable without requiring unique coding per item."
    },
    {
        "file": "product-p3.html",
        "title": "Product Detail Page - Lite",
        "tags": ["Grid Flexibility", "Content Reflow", "Hierarchy"],
        "desc": "The Aethereus Lite page continues the consistent user flow. The Add to Cart button remains persistently above the fold, ensuring that regardless of which tab the user interacts with, the primary conversion action is never obscured."
    },
    {
        "file": "product-p4.html",
        "title": "Product Detail Page - Soundbar",
        "tags": ["Cross-Category UX", "Responsive Images", "Whitespace"],
        "desc": "The Aura Soundbar X utilizes a vastly different aspect ratio for its primary image. The UI seamlessly adapts to this change by leveraging CSS flexbox constraints, ensuring the layout never breaks even when presenting non-standard hardware shapes."
    },
    {
        "file": "cart.html",
        "title": "Cart & Order Review",
        "tags": ["Friction Reduction", "Microcopy", "Clear Affordance"],
        "desc": "The cart interface is designed for absolute clarity. Large, distinct typography separates product names from their prices. A prominent, high-contrast 'Proceed to Checkout' button provides a clear next step, while dynamic JavaScript instantly updates sub-totals, reinforcing system status visibility."
    },
    {
        "file": "checkout-shipping.html",
        "title": "Checkout Flow: Shipping",
        "tags": ["Chunking", "Form UX", "Progress Disclosure"],
        "desc": "Checkout is broken into distinct phases (Shipping -> Payment) to prevent form fatigue. This concept, known as 'chunking', drastically reduces cart abandonment rates. The single-column form layout ensures a smooth vertical eye-tracking path for the user."
    },
    {
        "file": "checkout-payment.html",
        "title": "Checkout Flow: Payment",
        "tags": ["Trust Signals", "Visual Prompts", "Security"],
        "desc": "The payment page features a dummy QR code integration to simulate modern, frictionless mobile wallet payments. By simplifying the interface at the moment of transaction, we reduce user anxiety and increase the perception of platform security and stability."
    },
    {
        "file": "checkout-success.html",
        "title": "Post-Purchase Experience",
        "tags": ["Positive Reinforcement", "Next Steps", "Confirmation"],
        "desc": "The success page provides immediate emotional gratification and system confirmation. It clears the local cart state via JavaScript and offers clear navigational exits ('Return Home', 'View Orders') to keep the user engaged in the ecosystem."
    },
    {
        "file": "about.html",
        "title": "Brand Storytelling",
        "tags": ["Emotional Connection", "Typography", "Imagery"],
        "desc": "The 'About Us' page shifts the focus from conversion to brand building. A centered, narrow max-width text column optimizes reading length (ideal character count per line), while the high-end headphone imagery reinforces the engineering excellence narrative."
    },
    {
        "file": "reviews.html",
        "title": "Social Proof & Trust",
        "tags": ["Social Proof", "Authenticity", "Grid Alignment"],
        "desc": "User reviews are vital for high-ticket items. We utilize a masonry-style flex/grid hybrid to display authentic-looking avatars and distinct star ratings. The golden accent color for the stars draws the eye immediately, validating the product quality through community consensus."
    },
    {
        "file": "blog.html",
        "title": "Content Strategy Hub",
        "tags": ["Content Discovery", "Card UI", "Thumbnail Banners"],
        "desc": "The blog index uses a Card UI pattern. Distinct product banners act as thumbnails, creating strong visual anchors. Clear categorization ('Product Update', 'Education') above the titles helps users quickly scan and filter content based on their intent."
    },
    {
        "file": "blog-post-1.html",
        "title": "Article Readability",
        "tags": ["Typography Scaling", "Line Height", "Focus"],
        "desc": "The individual blog post layout heavily restricts the maximum width of the text block to around 800px. This prevents horizontal reading strain. Large, stylized blockquotes break up the monotony of the text and highlight key product features."
    },
    {
        "file": "blog-post-2.html",
        "title": "Educational Content",
        "tags": ["Value Addition", "Brand Authority", "Pacing"],
        "desc": "By providing educational content (e.g., explaining ANC physics), the brand establishes itself as an authority, not just a retailer. The clean layout ensures that complex information is easily digested, building long-term user trust."
    },
    {
        "file": "login.html",
        "title": "Authentication: Login",
        "tags": ["Frictionless Entry", "Form Design", "Error Prevention"],
        "desc": "The login page is aggressively simplified to prevent cognitive overload. Generous padding inside the input fields makes the targets easy to tap on mobile, while the centralized layout keeps focus entirely on the authentication task."
    },
    {
        "file": "register.html",
        "title": "Authentication: Register",
        "tags": ["Onboarding", "Clarity", "Minimal Fields"],
        "desc": "Registration requires the absolute minimum amount of information (Name, Email, Password) to lower the barrier to entry. This adherence to 'Hick’s Law' (reducing choices/fields) drastically improves user onboarding conversion rates."
    },
    {
        "file": "profile.html",
        "title": "User Dashboard",
        "tags": ["Dashboard UI", "Personalization", "Quick Actions"],
        "desc": "The account dashboard acts as a personalized command center. It uses an off-canvas or sidebar-style secondary navigation (Profile, Orders, Wishlist) to organize complex settings into manageable, distinct views."
    },
    {
        "file": "orders.html",
        "title": "Order History View",
        "tags": ["Data Visualization", "Status Indicators", "List Design"],
        "desc": "Orders are presented in a clean, chronological list. Key information (Order ID, Status, Total) is surfaced immediately without requiring clicks, allowing users to rapidly parse their past interactions and track current shipments."
    },
    {
        "file": "wishlist.html",
        "title": "Saved Items (Wishlist)",
        "tags": ["Retention Strategy", "Micro-Interactions", "Desire Paths"],
        "desc": "The wishlist functions as an intermediate step between 'browsing' and 'buying'. By allowing users to save items for later, we significantly decrease the hard bounce rate and create an organic reason for the user to return to the site."
    },
    {
        "file": "personas.html",
        "title": "UX Personas Documentation",
        "tags": ["Research Artifact", "Empathy", "Target Audience"],
        "desc": "This page documents the foundational UX research behind the project. Presenting personas in a card format makes the target demographic (e.g., audiophiles, professionals) easily scannable and grounds design decisions in user reality."
    },
    {
        "file": "design-system.html",
        "title": "Design System",
        "tags": ["Consistency", "Component Library", "Scalability"],
        "desc": "A dedicated design system page proves the project's scalability. By defining typography scales, color palettes (CSS variables), and button states in one place, we ensure absolute visual consistency across all 27 pages of the platform."
    },
    {
        "file": "terms.html",
        "title": "Terms of Service",
        "tags": ["Legibility", "Line Length", "Typography"],
        "desc": "Legal pages are notoriously difficult to read. By enforcing a strict maximum character width and increasing the line height (leading), we transform dense legal text into an accessible, readable document that respects the user's time."
    },
    {
        "file": "privacy.html",
        "title": "Privacy Policy",
        "tags": ["Trust Signals", "Transparency", "Formatting"],
        "desc": "In an era of data anxiety, presenting a clear, well-structured Privacy Policy is a vital UI/UX trust signal. Clear h3 sub-headers allow users to skim directly to the information they care about most regarding their personal data."
    },
    {
        "file": "faq.html",
        "title": "FAQ & Support",
        "tags": ["Self-Service", "Information Architecture", "Clarity"],
        "desc": "The FAQ reduces customer support friction by providing self-service answers. Bold question headers followed by slightly muted answer text creates a clear visual hierarchy, allowing users to rapidly scan for their specific issue."
    },
    {
        "file": "contact.html",
        "title": "Contact Interface",
        "tags": ["Accessibility", "Direct Communication", "Form UI"],
        "desc": "A straightforward contact form placed alongside physical/email addresses provides multiple avenues of support. The expansive message text area provides a clear affordance that the user is encouraged to explain their issue fully."
    },
    {
        "file": "404.html",
        "title": "404 Error State",
        "tags": ["Error Recovery", "Brand Voice", "Wayfinding"],
        "desc": "A 404 page should never be a dead end. By using on-brand messaging ('Lost in the Soundscape') and a clear primary CTA to return home, we transform user frustration into an opportunity for continued engagement."
    },
    {
        "file": "thank-you.html",
        "title": "Developer Credits",
        "tags": ["Submission", "Project End"],
        "desc": "Thank you for reviewing the Aura Audio UI/UX Project. Designed and developed by Shivam Tanwar."
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Aura Audio | UI/UX Project Presentation</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: #0f0f13; overflow: hidden; }
        
        .slides-container {
            width: 100vw;
            height: 100vh;
            position: relative;
        }

        .slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transform: scale(0.95);
            transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            pointer-events: none;
            z-index: 1;
        }

        .slide.active {
            opacity: 1;
            transform: scale(1);
            pointer-events: auto;
            z-index: 10;
        }

        .slide-inner {
            display: flex;
            width: 90vw;
            max-width: 1600px;
            height: 80vh;
            background: #fff;
            border-radius: 24px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.4);
            overflow: hidden;
        }

        .screenshot-container {
            width: 60%;
            height: 100%;
            background: #f4f4f7;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            border-right: 1px solid #eaeaea;
        }

        /* Responsive iframe scaling */
        .live-iframe {
            width: 1440px;
            height: 900px; 
            transform: scale(0.65); 
            transform-origin: center center;
            border: none;
            pointer-events: none;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border-radius: 8px;
            background: #fff;
        }

        @media (max-width: 1400px) { .live-iframe { transform: scale(0.55); } }
        @media (max-width: 1200px) { .live-iframe { transform: scale(0.45); } }

        .content-container {
            width: 40%;
            padding: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .page-url { font-size: 1.1rem; color: #888; margin-bottom: 20px; font-family: monospace; letter-spacing: 1px; }
        h2 { font-size: 3rem; margin-bottom: 25px; color: #111; line-height: 1.1; letter-spacing: -1px; }
        .tags { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 35px; }
        .ui-ux-tag { padding: 8px 18px; background: #f0f0f5; color: #333; border-radius: 30px; font-size: 1rem; font-weight: 600; }
        p { font-size: 1.3rem; line-height: 1.7; color: #444; }
        
        .pagination-bar {
            position: fixed;
            bottom: 30px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 10px;
            z-index: 100;
        }

        .dot {
            width: 12px;
            height: 12px;
            background: rgba(255,255,255,0.3);
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .dot.active { background: #fff; transform: scale(1.3); }

        .fullscreen-btn {
            position: fixed;
            top: 30px;
            right: 40px;
            background: rgba(255,255,255,0.1);
            color: #fff;
            border: none;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 100;
            transition: all 0.2s;
        }
        .fullscreen-btn:hover {
            background: rgba(255,255,255,0.3);
            transform: scale(1.1);
        }
        .fullscreen-btn svg {
            width: 20px;
            height: 20px;
        }

        /* Fullscreen overrides */
        :fullscreen .slide-inner {
            width: 100vw;
            height: 100vh;
            border-radius: 0;
            max-width: none;
        }
        :fullscreen .pagination-bar {
            display: none;
        }
        :fullscreen .fullscreen-btn {
            opacity: 0; /* Hide unless hovered */
        }
        :fullscreen .fullscreen-btn:hover {
            opacity: 1;
        }

        .controls-hint {
            position: fixed;
            top: 30px;
            right: 40px;
            color: rgba(255,255,255,0.5);
            font-size: 0.9rem;
            z-index: 100;
        }

        .download-btn {
            position: fixed;
            top: 30px;
            left: 40px;
            background: #fff;
            color: #111;
            padding: 10px 20px;
            border-radius: 30px;
            font-weight: 600;
            z-index: 100;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: transform 0.2s;
            font-family: inherit;
        }
        .download-btn:hover { transform: scale(1.05); }

        @media print {
            @page { size: A3 landscape; margin: 0; }
            body { background: #fff; overflow: visible !important; }
            .slides-container { position: static; height: auto; overflow: visible; }
            .slide { 
                position: relative !important; 
                opacity: 1 !important; 
                transform: none !important; 
                width: 420mm !important; 
                height: 297mm !important; 
                page-break-after: always;
                background: #fff;
            }
            .slide-inner { 
                width: 100% !important; 
                height: 100% !important; 
                max-width: none !important; 
                border-radius: 0 !important; 
                box-shadow: none !important; 
            }
            .screenshot-container { background: #f4f4f7 !important; border-right: 1px solid #eaeaea !important; }
            .pagination-bar, .controls-hint, .download-btn { display: none !important; }
        }
    </style>
</head>
<body>
    <button class="fullscreen-btn" onclick="toggleFullScreen()" title="Toggle Fullscreen">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path>
        </svg>
    </button>
    <div class="slides-container" id="slides-container">
"""

with open("presentation.html", "w", encoding="utf-8") as f:
    f.write(html_template)
    
    # Write slides
    for i, p in enumerate(pages):
        tags_html = "".join([f'<span class="ui-ux-tag">{t}</span>' for t in p["tags"]])
        active_class = "active" if i == 0 else ""
        
        if p["file"] in ["title.html", "thank-you.html"]:
            page_html = f"""
        <div class="slide {active_class}">
            <div class="slide-inner">
                <iframe style="width: 100%; height: 100%; flex: 1; border: none; background: #fff;" src="{p['file']}"></iframe>
            </div>
        </div>
"""
        else:
            page_html = f"""
        <div class="slide {active_class}">
            <div class="slide-inner">
                <div class="screenshot-container">
                    <iframe class="live-iframe" src="{p['file']}"></iframe>
                </div>
                <div class="content-container">
                    <div class="page-url">/{p['file']}</div>
                    <h2>{p['title']}</h2>
                    <div class="tags">
                        {tags_html}
                    </div>
                    <p>{p['desc']}</p>
                </div>
            </div>
        </div>
"""
        f.write(page_html)

    # Write pagination and scripts
    f.write('    </div>\n    <div class="pagination-bar">\n')
    for i in range(len(pages)):
        active_class = "active" if i == 0 else ""
        f.write(f'        <div class="dot {active_class}" onclick="goToSlide({i})"></div>\n')
        
    js_logic = """
    </div>
    
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const dots = document.querySelectorAll('.dot');
        const totalSlides = slides.length;

        function toggleFullScreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    console.log(`Error attempting to enable fullscreen: ${err.message}`);
                });
            } else {
                document.exitFullscreen();
            }
        }

        function goToSlide(index) {
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');
            
            currentSlide = index;
            
            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                if (currentSlide < totalSlides - 1) {
                    goToSlide(currentSlide + 1);
                }
            } else if (e.key === 'ArrowLeft') {
                if (currentSlide > 0) {
                    goToSlide(currentSlide - 1);
                }
            }
        });
    </script>
</body>
</html>
"""
    f.write(js_logic)

print("Interactive presentation.html slider has been generated successfully.")
