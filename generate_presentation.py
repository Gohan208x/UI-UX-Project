import os

pages = [
    {
        "file": "title.html",
        "title": "Aura Audio Project",
        "tags": ["Introduction", "Amity University"],
        "desc": "Comprehensive UI/UX design project showcasing modern e-commerce flows, component scalability, and premium aesthetic execution.\n\nThis report documents the end-to-end design process, from wireframing to high-fidelity prototyping, emphasizing cognitive load reduction, accessibility standards, and seamless user journeys."
    },
    {
        "file": "index.html",
        "title": "Home Page Strategy",
        "tags": ["Visual Hierarchy", "Call to Action", "First Impression"],
        "desc": "The home page acts as the primary hook for users. By utilizing a high-contrast, minimalist hero banner with immense negative space, we instantly convey the brand's 'premium luxury' positioning.\n\nThe primary CTA (Shop Collection) is placed dead center, reducing cognitive load and driving immediate conversion. The typography uses Inter (a highly legible geometric sans-serif) to ensure maximum readability across all screen sizes.\n\nFurthermore, the navigation bar is kept intentionally sparse. By removing unnecessary links, we prevent decision fatigue and seamlessly funnel users toward the product catalog, which is the primary business objective."
    },
    {
        "file": "shop.html",
        "title": "Product Catalog UX",
        "tags": ["Grid Layout", "Information Architecture", "Scalability"],
        "desc": "The shop utilizes a consistent 3-column CSS Grid layout that scales perfectly across devices. Products are presented with vast white space to emphasize the hardware design.\n\nPricing is displayed prominently below clear, legible typography to prevent 'price shock' and manage user expectations early in the flow. Hover states provide immediate visual feedback, slightly lifting the product cards to signify interactivity without causing jarring layout shifts.\n\nFiltering and sorting mechanisms are implicitly handled through clear category delineations, ensuring that users do not feel overwhelmed when browsing the curated selection of high-end audio equipment."
    },
    {
        "file": "product-p1.html",
        "title": "Product Detail Page (PDP) - Pro Max",
        "tags": ["Tabbed Navigation", "Interactive Elements", "F-Pattern Reading"],
        "desc": "The PDP uses a split-screen design. The high-resolution product image remains fixed on the left while detailed, tabbed content scrolls on the right. This prevents endless vertical scrolling (scroll fatigue) while providing deep, contextual information on demand.\n\nBy adopting an F-Pattern reading hierarchy, the user's eye naturally scans from the bold product title, down to the price, and immediately to the Add to Cart button. This creates a frictionless path to purchase.\n\nThe tabbed interface (Description, Reviews, Warranty, Returns) organizes dense technical specifications into digestible chunks, respecting the user's cognitive limits while still catering to audiophiles who demand extensive details."
    },
    {
        "file": "product-p2.html",
        "title": "Product Detail Page - Studio",
        "tags": ["Consistency", "Component Reusability", "Visual Anchor"],
        "desc": "Demonstrating the scalability of the PDP template. The exact same UI framework beautifully accommodates a completely different product aesthetic, proving that the underlying wireframe is robust and adaptable.\n\nMaintaining UI consistency across all product pages drastically reduces the learning curve for the user. Once they understand how to navigate the 'Pro Max' page, they inherently know how to interact with the 'Studio' page.\n\nThe stark white background acts as a visual anchor, making the sleek black product photography pop, drawing immediate attention to the physical design of the headphones."
    },
    {
        "file": "product-p3.html",
        "title": "Product Detail Page - Lite",
        "tags": ["Grid Flexibility", "Content Reflow", "Hierarchy"],
        "desc": "The Aethereus Lite page continues the consistent user flow. The Add to Cart button remains persistently above the fold, ensuring that regardless of which tab the user interacts with, the primary conversion action is never obscured.\n\nThe breadcrumb navigation at the top provides critical wayfinding, allowing users to easily backtrack to the main shop without relying on the browser's back button. This significantly improves the overall sense of user control and freedom.\n\nMicro-interactions on the color selection swatches provide immediate visual confirmation, assuring the user of their choice before they commit to adding the item to their cart."
    },
    {
        "file": "product-p4.html",
        "title": "Product Detail Page - Soundbar",
        "tags": ["Cross-Category UX", "Responsive Images", "Whitespace"],
        "desc": "The Aura Soundbar X utilizes a vastly different aspect ratio for its primary image. The UI seamlessly adapts to this change by leveraging CSS flexbox constraints, ensuring the layout never breaks even when presenting non-standard hardware shapes.\n\nBy surrounding the wide product image with generous padding, we maintain the luxurious, uncluttered aesthetic established by the headphone pages. This proves the design system is capable of cross-category expansion.\n\nThe 'Add to Cart' workflow remains identically positioned, leveraging muscle memory and established behavioral patterns to drive the final conversion."
    },
    {
        "file": "cart.html",
        "title": "Cart & Order Review",
        "tags": ["Friction Reduction", "Microcopy", "Clear Affordance"],
        "desc": "The cart interface is designed for absolute clarity. Large, distinct typography separates product names from their prices. A prominent, high-contrast 'Proceed to Checkout' button provides a clear next step.\n\nDynamic JavaScript instantly updates sub-totals when quantities are changed, reinforcing system status visibility. This immediate feedback loop builds trust and prevents user anxiety regarding final costs.\n\nNegative actions, such as removing an item, are intentionally styled with lower visual weight (a simple text link) to prevent accidental clicks while still remaining accessible for users who wish to edit their order."
    },
    {
        "file": "checkout-shipping.html",
        "title": "Checkout Flow: Shipping",
        "tags": ["Form UX", "Progress Indicators", "Validation"],
        "desc": "The checkout process is broken down into manageable, logical steps to prevent form abandonment. A clear progress indicator at the top of the screen provides wayfinding, letting the user know exactly where they are in the process.\n\nInput fields feature large hit areas and clear, permanent labels (rather than relying solely on disappearing placeholders). This is a critical accessibility feature that prevents users from losing context while typing.\n\nThe layout heavily prioritizes the form on the left while anchoring a persistent order summary on the right, ensuring the user always has a clear view of their impending purchase."
    },
    {
        "file": "checkout-payment.html",
        "title": "Checkout Flow: Payment",
        "tags": ["Security Signals", "Trust UX", "Error Prevention"],
        "desc": "Payment screens require a high degree of user trust. We utilize standard, recognizable input formats for credit card details, reducing the cognitive load required to fill out the form.\n\nVisual security signals, such as padlock icons and clear, legible font choices, subtly reassure the user that their transaction is secure. The persistent order summary remains visible, providing final confirmation of the total cost before the irreversible 'Pay Now' action.\n\nThe 'Pay Now' button utilizes the primary accent color, ensuring it is the undeniable focal point of the page, guiding the user to the successful completion of their journey."
    },
    {
        "file": "checkout-success.html",
        "title": "Checkout Success State",
        "tags": ["Delight", "Confirmation", "Next Steps"],
        "desc": "The success screen is a crucial moment for user delight. A large, reassuring checkmark icon instantly communicates that the complex transaction was successful, satisfying the heuristic of system status visibility.\n\nClear, concise microcopy thanks the user and provides immediate next steps (e.g., checking their email for a receipt). This prevents the user from feeling abandoned after completing the primary conversion.\n\nA secondary CTA to 'Continue Shopping' gently guides the user back into the product ecosystem, encouraging further engagement without being overly aggressive."
    },
    {
        "file": "about.html",
        "title": "About Us: Brand Story",
        "tags": ["Storytelling", "Brand Identity", "Typography"],
        "desc": "The About page shifts focus from conversion to brand storytelling. Large, immersive photography is paired with expansive typography to create an emotional connection with the user.\n\nThe layout is deliberately asymmetrical in places to create visual interest, breaking away from the rigid grids of the shop page. This signals to the user that they are in a different context—one focused on narrative rather than transactional logic.\n\nHigh contrast and generous line-height ensure that the long-form text remains highly readable, reducing eye strain and encouraging users to read the full brand history."
    },
    {
        "file": "reviews.html",
        "title": "Customer Testimonials",
        "tags": ["Social Proof", "Trust Building", "Card UI"],
        "desc": "Testimonials are crucial for establishing social proof. This page utilizes a clean, modular card UI to present reviews in a scannable, digestible format.\n\nBy isolating each review into its own visual container with subtle drop shadows, we reduce clutter and make it easy for users to read individual opinions. The consistent use of star icons provides instant, universally recognizable visual summaries of the feedback.\n\nThis dedicated page serves as a trust-building destination for users who are in the consideration phase of the sales funnel, directly addressing potential anxieties before they reach the checkout."
    },
    {
        "file": "blog.html",
        "title": "Blog / News Hub",
        "tags": ["Content Strategy", "Grid Systems", "Hover States"],
        "desc": "The blog hub organizes content using a dynamic masonry-style grid. This layout allows for varied image dimensions while maintaining a strict vertical rhythm, keeping the page looking organized and intentional.\n\nHover states on the article cards darken the images and reveal read-more prompts. This interactive feedback clearly communicates clickability, satisfying the heuristic of discoverability.\n\nBy providing valuable, non-sales content, the blog increases user retention and establishes Aura Audio as an authority in the audio space, deepening brand loyalty over time."
    },
    {
        "file": "blog-post-1.html",
        "title": "Blog Article Layout",
        "tags": ["Reading Experience", "Line Length", "Typography Scale"],
        "desc": "The article layout is aggressively optimized for the reading experience. We strictly limit the maximum line width (measure) to around 70 characters. This prevents eye fatigue caused by tracking long lines of text across a wide monitor.\n\nThe typography scale is carefully tuned, with a distinct visual hierarchy between the article title, subheadings, and body copy. This allows users to easily scan the content before committing to reading it deeply.\n\nA massive, immersive hero image sets the tone for the article, while the minimalist header ensures that navigation remains accessible without distracting from the content itself."
    },
    {
        "file": "blog-post-2.html",
        "title": "Secondary Blog Article",
        "tags": ["Template Scalability", "Editorial Design", "Focus"],
        "desc": "This page further demonstrates the robustness of the blog article template. The layout seamlessly handles different lengths of content and varying image assets without requiring structural changes.\n\nThe stark, minimalist aesthetic strips away all sidebar distractions, focusing the user's absolute attention on the editorial content. This is a deliberate rejection of cluttered, ad-heavy web layouts.\n\nConsistent spacing (margin and padding) between paragraphs ensures a steady vertical rhythm, propelling the reader down the page effortlessly."
    },
    {
        "file": "login.html",
        "title": "Authentication: Login",
        "tags": ["Form Design", "Authentication", "Frictionless"],
        "desc": "The login screen is stripped of all non-essential elements. The user's focus is entirely directed toward the authentication form. This brutalist simplicity drastically reduces cognitive load during a critical access phase.\n\nInput fields are large and clearly labeled. The primary action button ('Sign In') spans the full width of the form, maximizing the hit area for both mouse and touch interactions.\n\nClear links for account recovery and registration are provided contextually below the primary action, ensuring that users who encounter friction have an immediate escape hatch."
    },
    {
        "file": "register.html",
        "title": "Authentication: Registration",
        "tags": ["Onboarding", "Data Collection", "Clarity"],
        "desc": "Similar to the login screen, registration is presented in an isolated, distraction-free environment. We only ask for the absolute minimum data required to create an account, reducing form abandonment rates.\n\nPassword requirements (if any) would be clearly stated upfront, preventing frustrating validation errors after submission. This adheres to the UX heuristic of error prevention rather than just error recovery.\n\nThe transition between login and registration is seamless, utilizing identical layout structures to prevent disorientation and maintain a cohesive onboarding experience."
    },
    {
        "file": "profile.html",
        "title": "User Dashboard / Profile",
        "tags": ["Account Management", "Navigation", "Personalization"],
        "desc": "The user dashboard serves as the central hub for account management. A persistent left-hand sidebar provides clear, constant access to various profile sections (Orders, Wishlist, Settings).\n\nBy compartmentalizing user data into specific views, we avoid overwhelming the user with a massive, scrolling settings page. The active state in the sidebar clearly indicates the user's current location within the dashboard architecture.\n\nThe clean, grid-based presentation of account details allows users to quickly scan and verify their personal information at a glance."
    },
    {
        "file": "orders.html",
        "title": "Order History",
        "tags": ["Data Presentation", "Status Tracking", "List UI"],
        "desc": "Order history is presented using a structured, list-based UI. Crucial information (Order Date, Status, Total) is highly visible, allowing users to quickly check on recent purchases without digging through complex menus.\n\nVisual cues, such as colored status badges (e.g., 'Delivered' in green), provide instant, at-a-glance comprehension of system status. This reduces anxiety regarding shipping and fulfillment.\n\nEach order block acts as a distinct visual unit, separated by ample whitespace and subtle borders, ensuring high legibility even for users with extensive purchase histories."
    },
    {
        "file": "wishlist.html",
        "title": "User Wishlist",
        "tags": ["Saved Items", "Re-engagement", "Grid View"],
        "desc": "The wishlist utilizes the same familiar 3-column product grid found on the main shop page. This consistency means the user requires zero additional cognitive effort to understand how to interact with their saved items.\n\nClear 'Add to Cart' and 'Remove' actions are provided on every card. By making the path from 'Wishlist' to 'Cart' a single click, we significantly shorten the conversion funnel for returning users.\n\nThe page serves as a powerful re-engagement tool, allowing users to curate their desired products in a highly visual, personalized gallery."
    },
    {
        "file": "personas.html",
        "title": "UX Research: Personas",
        "tags": ["Documentation", "User-Centric", "Research"],
        "desc": "This page documents the foundational UX research behind the project. Presenting user personas directly within the interface demonstrates a commitment to user-centric design principles.\n\nThe layout uses a simple, highly readable column structure to contrast the goals, needs, and pain points of different target demographics. This acts as a 'source of truth' for all subsequent design decisions.\n\nBy making this research transparent, stakeholders can easily trace specific UI choices (like the minimalist checkout) back to documented user requirements (like reducing cognitive overload)."
    },
    {
        "file": "design-system.html",
        "title": "Design System / Styleguide",
        "tags": ["Scalability", "Consistency", "Tokens"],
        "desc": "A comprehensive design system is the backbone of the Aura Audio project. This page acts as a living styleguide, detailing the exact typographic scales, color palettes, and component states used across the site.\n\nBy codifying these elements, we ensure absolute visual consistency across all 27 pages. It also allows developers to rapidly build new features using pre-established CSS classes without reinventing the wheel.\n\nThe presentation of the design tokens (colors, fonts, buttons) is strictly utilitarian, focusing on clarity and utility over decorative flair."
    },
    {
        "file": "terms.html",
        "title": "Terms of Service",
        "tags": ["Legal UX", "Readability", "Structure"],
        "desc": "Legal pages are notoriously difficult to read. We approached the Terms of Service with a focus on 'Legal UX'. The measure (line length) is restricted to ensure comfortable reading of dense textual information.\n\nClear, bold typography separates distinct clauses, creating a scannable document outline. We avoided tiny, low-contrast 'fine print', adhering strictly to WCAG accessibility guidelines for text contrast.\n\nWhile the content is dense, the generous whitespace and strict typographic rhythm prevent the page from feeling hostile or overwhelming to the user."
    },
    {
        "file": "privacy.html",
        "title": "Privacy Policy",
        "tags": ["Transparency", "Legal UX", "Trust"],
        "desc": "Similar to the Terms page, the Privacy Policy is designed for maximum transparency. In an era where data privacy is paramount, burying this information in illegible text damages brand trust.\n\nThe layout utilizes clear bullet points and hierarchical headings to break complex legal jargon into digestible concepts. This empowers users to easily find specific information regarding how their data is handled.\n\nThe clean, unbranded aesthetic of this page signals objectivity and professionalism, reinforcing the brand's commitment to user security and trust."
    },
    {
        "file": "faq.html",
        "title": "Frequently Asked Questions",
        "tags": ["Support Deflection", "Information Retrieval", "Accordion UI"],
        "desc": "The FAQ page is a critical tool for support deflection. By anticipating common user queries, we reduce the burden on customer service and provide users with immediate gratification.\n\nThe page likely utilizes an accordion UI (or distinct, separated blocks) to hide answers until requested. This prevents the user from being confronted by a massive wall of text, allowing them to scan questions rapidly.\n\nThe categorization of questions (e.g., Shipping, Returns, Tech Specs) further streamlines information retrieval, mapping directly to the user's mental model."
    },
    {
        "file": "contact.html",
        "title": "Contact Interface",
        "tags": ["Accessibility", "Direct Communication", "Form UI"],
        "desc": "A straightforward contact form placed alongside physical/email addresses provides multiple avenues of support, catering to different user preferences.\n\nThe expansive message text area provides a clear affordance that the user is encouraged to explain their issue fully. Large, highly visible input fields reduce the physical dexterity required to interact with the form.\n\nThe layout balances the form input on one side with reassuring, concrete contact details on the other, proving to the user that there is a real, accessible team behind the digital storefront."
    },
    {
        "file": "404.html",
        "title": "404 Error State",
        "tags": ["Error Recovery", "Brand Voice", "Wayfinding"],
        "desc": "A 404 page should never be a dead end. When users encounter a broken link, they experience frustration. This page is designed to de-escalate that frustration rapidly.\n\nBy using on-brand messaging ('Lost in the Soundscape') and a clear, dominant primary CTA to return home, we transform user frustration into an opportunity for continued engagement.\n\nThe minimalist aesthetic prevents sensory overload during an error state, providing a calm, clear exit route back to the safety of the main application."
    },
    {
        "file": "thank-you.html",
        "title": "Developer Credits",
        "tags": ["Submission", "Project End"],
        "desc": "Thank you for reviewing the Aura Audio UI/UX Project. Designed and developed by Shivam Tanwar.\n\nThis project demonstrates a rigorous application of modern UI/UX principles, from cognitive load management to scalable design systems, resulting in a cohesive, premium e-commerce experience."
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
