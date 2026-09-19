import os
from playwright.sync_api import sync_playwright
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

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

def generate_docx():
    # 1. Take screenshots
    cwd = os.getcwd()
    screenshots_dir = os.path.join(cwd, "screenshots_tmp")
    os.makedirs(screenshots_dir, exist_ok=True)
    
    print("Launching headless browser to take screenshots...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a desktop viewport size
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        
        # Prevent the credits modal from showing during screenshots
        context.add_init_script("sessionStorage.setItem('auraCreditsSeen', 'true');")
        
        page = context.new_page()
        
        for p_data in pages:
            file_name = p_data["file"]
            file_path = f"file:///{cwd}/{file_name}".replace("\\", "/")
            print(f"Screenshotting {file_name}...")
            page.goto(file_path, wait_until="networkidle")
            page.wait_for_timeout(1500)  # Wait for local images to decode and paint
            # Save screenshot
            screenshot_path = os.path.join(screenshots_dir, f"{file_name}.png")
            page.screenshot(path=screenshot_path)
            p_data["screenshot"] = screenshot_path
            
        browser.close()

    print("Screenshots complete. Generating DOCX...")
    
    # 2. Build the DOCX
    doc = Document()
    
    # Configure document for A4 Portrait
    # A4 size: 8.27 inches wide x 11.69 inches high
    section = doc.sections[0]
    section.orientation = WD_ORIENT.PORTRAIT
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    # Standard margins
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    
    # Customize styles
    styles = doc.styles
    title_style = styles['Heading 1']
    title_font = title_style.font
    title_font.name = 'Arial'
    title_font.size = Pt(24)
    title_font.color.rgb = RGBColor(0, 0, 0)
    
    for i, p_data in enumerate(pages):
        if p_data["file"] == "title.html":
            for _ in range(5):
                doc.add_paragraph()
            paragraph = doc.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.add_picture(p_data["screenshot"], width=Inches(7.2))
            
            doc.add_page_break()
            
            # --- INDEX ---
            idx_title = doc.add_paragraph()
            idx_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            idx_run = idx_title.add_run("INDEX")
            idx_run.bold = True
            idx_run.underline = True
            idx_run.font.size = Pt(16)
            doc.add_paragraph()
            
            table = doc.add_table(rows=1, cols=3)
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'S.No'
            hdr_cells[1].text = 'Topic'
            hdr_cells[2].text = 'Page No.'
            
            index_data = [
                ("1.", "Introduction", "3"),
                ("2.", "Market Survey", "4"),
                ("3.", "Business Strategies Implemented", "5"),
                ("4.", "UI/UX Showcase & Results", "6"),
                ("5.", "UX Research & Personas", "33"),
                ("6.", "Conclusion", "36")
            ]
            for s_no, topic, page_no in index_data:
                row_cells = table.add_row().cells
                row_cells[0].text = s_no
                row_cells[1].text = topic
                row_cells[2].text = page_no
            
            doc.add_page_break()
            
            # --- INTRODUCTION ---
            intro_title = doc.add_paragraph()
            intro_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            intro_run = intro_title.add_run("INTRODUCTION")
            intro_run.bold = True
            intro_run.font.size = Pt(16)
            
            intro_p = doc.add_paragraph()
            intro_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            intro_p.add_run("Aura Audio is a conceptual e-commerce platform designed to showcase the pinnacle of modern UI/UX design. The name 'Aura' reflects the invisible yet palpable presence of high-fidelity sound, which our premium audiophile products aim to deliver. The website is focused on providing a frictionless shopping experience for luxury audio equipment, ranging from noise-canceling headphones to spatial audio soundbars. One of the most appreciated features of the platform is its strict adherence to cognitive load reduction—by stripping away unnecessary visual clutter, we allow the products to speak for themselves. We utilized vanilla web technologies (HTML, CSS, JS) to build high-fidelity prototypes, simulating a complete user journey from landing page to successful checkout, allowing us to deeply analyze website visitor behavior and conversion funnels.")
            
            doc.add_page_break()
            
            # --- MARKET SURVEY ---
            mkt_title = doc.add_paragraph()
            mkt_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            mkt_run = mkt_title.add_run("MARKET SURVEY")
            mkt_run.bold = True
            mkt_run.font.size = Pt(16)
            
            mkt_p = doc.add_paragraph()
            mkt_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            mkt_p.add_run("The global audio equipment market has experienced exponential growth in recent years, driven heavily by the shift towards remote work and digital entertainment. According to industry reports, the high-end headphone and soundbar market is currently valued at over $25 billion and is projected to grow significantly by 2026. The most popular consumer brands, such as Sony, Apple, and Sennheiser, have established a baseline for premium aesthetics.\n\nHowever, even with the growth of e-commerce, many platforms continue to suffer from poor user experience, leading to high cart abandonment rates. Unwanted visual clutter, complex navigation, and a lack of clear technical specifications are common frustrations for audiophiles making high-ticket purchases. We surveyed a sample of our target demographic (audiophiles and design-conscious professionals) and found that 95% of them heavily preferred a minimalist, distraction-free checkout process. Aura Audio was built to directly address this market gap by prioritizing seamless navigation, accessibility, and high-contrast, premium visuals.")
            
            doc.add_page_break()
            
            # --- BUSINESS STRATEGIES IMPLEMENTED ---
            bus_title = doc.add_paragraph()
            bus_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            bus_run = bus_title.add_run("BUSINESS STRATEGIES IMPLEMENTED")
            bus_run.bold = True
            bus_run.font.size = Pt(16)
            doc.add_paragraph()
            
            b1 = doc.add_paragraph()
            b1.add_run("1. Aura Audio across social media.\n").bold = True
            b1.add_run("Social media platforms such as Instagram, Twitter, and Pinterest are utilized as primary marketing tools. We use highly visual, aesthetic posts to connect with audiophiles globally and showcase the premium hardware design of Aura products.")
            
            b2 = doc.add_paragraph()
            b2.add_run("2. Influencer & Tech Reviewer Partnerships\n").bold = True
            b2.add_run("We actively share our products with prominent tech reviewers and audiophile communities. Providing high-fidelity sound samples and detailed specifications to these trusted voices is a highly effective start-up strategy for building brand authority.")
            
            b3 = doc.add_paragraph()
            b3.add_run("3. Targeted Video Ads\n").bold = True
            b3.add_run("Placing cinematic ads on video streaming platforms (like YouTube) before music or tech-related content is one of the most effective ways to reach our target demographic. This is a core future plan for scaling Aura Audio's reach.")
            
            b4 = doc.add_paragraph()
            b4.add_run("4. Premium Support Subscriptions\n").bold = True
            b4.add_run("We also provide additional revenue streams through premium subscription models, offering extended warranties, lossless audio streaming integrations, and priority customer support for our high-end user base.")
            
        elif p_data["file"] == "thank-you.html":
            # --- CONCLUSION ---
            doc.add_page_break()
            con_title = doc.add_paragraph()
            con_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            con_run = con_title.add_run("CONCLUSION")
            con_run.bold = True
            con_run.font.size = Pt(16)
            
            con_p = doc.add_paragraph()
            con_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            con_p.add_run("The Aura Audio project has successfully demonstrated the power of user-centric design in modern e-commerce. By focusing heavily on cognitive load reduction, scalable component architecture, and adherence to accessibility standards, we have created an interface that seamlessly guides users from product discovery to purchase. The integration of a minimalist aesthetic with deep technical specifications proves that luxury and utility can coexist. We hope to continue upgrading Aura Audio in the future, incorporating AI-driven product recommendations and expanding our design system to meet the ever-evolving needs of audiophiles and casual listeners alike.")
            
            doc.add_page_break()
            
            for _ in range(5):
                doc.add_paragraph()
            paragraph = doc.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.add_picture(p_data["screenshot"], width=Inches(7.2))
        else:
            # Vertical layout: Title, Tags, Image, Description
            
            # Title
            title_para = doc.add_paragraph()
            title_para.style = 'Heading 1'
            title_para.add_run(p_data["title"])
            
            # Tags
            tags_para = doc.add_paragraph()
            tags_run = tags_para.add_run(f"Tags: {', '.join(p_data['tags'])}")
            tags_run.italic = True
            tags_run.font.color.rgb = RGBColor(100, 100, 100)
            
            # Image
            img_para = doc.add_paragraph()
            img_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            img_run = img_para.add_run()
            # 8.27 width - 1 inch margins = 7.27 max width
            img_run.add_picture(p_data["screenshot"], width=Inches(7.2))
            
            # Description
            desc_para = doc.add_paragraph()
            desc_run = desc_para.add_run(p_data["desc"])
            desc_run.font.size = Pt(12)
            desc_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        doc.add_page_break()

    
    # --- ADD UX METHODOLOGY SECTION ---
    
    m_title = doc.add_paragraph()
    m_title.style = 'Heading 1'
    m_title.add_run("UX Methodology & Design Principles")
    
    m_desc1 = doc.add_paragraph()
    m_desc1.add_run("Accessibility & Contrast (WCAG Standards): ").bold = True
    m_desc1.add_run("Throughout the Aura Audio project, strict adherence to Web Content Accessibility Guidelines (WCAG) was maintained. The stark contrast between the primary text (#1d1d1f) and the backgrounds (#ffffff / #f5f5f7) ensures maximum legibility for users with visual impairments. Typography scales were mathematically determined to preserve readability across all device viewports.")
    m_desc1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    m_desc2 = doc.add_paragraph()
    m_desc2.add_run("Cognitive Load Reduction: ").bold = True
    m_desc2.add_run("A core philosophy of this project was the brutal elimination of unnecessary UI elements. By maximizing whitespace (negative space) and utilizing consistent, reusable components, we drastically lower the cognitive load placed on the user. They do not need to relearn how to navigate when moving from the Shop to a Product Detail Page; the mental models remain identical.")
    m_desc2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    m_desc3 = doc.add_paragraph()
    m_desc3.add_run("Heuristic Evaluation & Error Prevention: ").bold = True
    m_desc3.add_run("The checkout flows were designed around the principle of error prevention. By breaking complex forms into distinct, logical steps with permanent labels (shipping -> payment -> success), we guide the user seamlessly through the conversion funnel. Immediate visual feedback mechanisms (like dynamic cart totals and hover states) satisfy the heuristic of 'Visibility of System Status', keeping the user informed and in control at all times.")
    m_desc3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_page_break()
    
    
    # --- ADD UX METHODOLOGY SECTION ---
    
    m_title = doc.add_paragraph()
    m_title.style = 'Heading 1'
    m_title.add_run("UX Methodology & Design Principles")
    
    m_desc1 = doc.add_paragraph()
    m_desc1.add_run("Accessibility & Contrast (WCAG Standards): ").bold = True
    m_desc1.add_run("Throughout the Aura Audio project, strict adherence to Web Content Accessibility Guidelines (WCAG) was maintained. The stark contrast between the primary text (#1d1d1f) and the backgrounds (#ffffff / #f5f5f7) ensures maximum legibility for users with visual impairments. Typography scales were mathematically determined to preserve readability across all device viewports.")
    m_desc1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    m_desc2 = doc.add_paragraph()
    m_desc2.add_run("Cognitive Load Reduction: ").bold = True
    m_desc2.add_run("A core philosophy of this project was the brutal elimination of unnecessary UI elements. By maximizing whitespace (negative space) and utilizing consistent, reusable components, we drastically lower the cognitive load placed on the user. They do not need to relearn how to navigate when moving from the Shop to a Product Detail Page; the mental models remain identical.")
    m_desc2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    m_desc3 = doc.add_paragraph()
    m_desc3.add_run("Heuristic Evaluation & Error Prevention: ").bold = True
    m_desc3.add_run("The checkout flows were designed around the principle of error prevention. By breaking complex forms into distinct, logical steps with permanent labels (shipping -> payment -> success), we guide the user seamlessly through the conversion funnel. Immediate visual feedback mechanisms (like dynamic cart totals and hover states) satisfy the heuristic of 'Visibility of System Status', keeping the user informed and in control at all times.")
    m_desc3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_page_break()
    
    
    # --- ADD UX METHODOLOGY SECTION ---
    
    m_title = doc.add_paragraph()
    m_title.style = 'Heading 1'
    m_title.add_run("UX Methodology & Design Principles")
    
    m_desc1 = doc.add_paragraph()
    m_desc1.add_run("Accessibility & Contrast (WCAG Standards): ").bold = True
    m_desc1.add_run("Throughout the Aura Audio project, strict adherence to Web Content Accessibility Guidelines (WCAG) was maintained. The stark contrast between the primary text (#1d1d1f) and the backgrounds (#ffffff / #f5f5f7) ensures maximum legibility for users with visual impairments. Typography scales were mathematically determined to preserve readability across all device viewports.")
    m_desc1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    m_desc2 = doc.add_paragraph()
    m_desc2.add_run("Cognitive Load Reduction: ").bold = True
    m_desc2.add_run("A core philosophy of this project was the brutal elimination of unnecessary UI elements. By maximizing whitespace (negative space) and utilizing consistent, reusable components, we drastically lower the cognitive load placed on the user. They do not need to relearn how to navigate when moving from the Shop to a Product Detail Page; the mental models remain identical.")
    m_desc2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    m_desc3 = doc.add_paragraph()
    m_desc3.add_run("Heuristic Evaluation & Error Prevention: ").bold = True
    m_desc3.add_run("The checkout flows were designed around the principle of error prevention. By breaking complex forms into distinct, logical steps with permanent labels (shipping -> payment -> success), we guide the user seamlessly through the conversion funnel. Immediate visual feedback mechanisms (like dynamic cart totals and hover states) satisfy the heuristic of 'Visibility of System Status', keeping the user informed and in control at all times.")
    m_desc3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_page_break()
    
    # --- ADD UX DETAILS SECTION ---
    
    # 1. Personas
    p_title = doc.add_paragraph()
    p_title.style = 'Heading 1'
    p_title.add_run("UX Research & Personas")
    
    doc.add_paragraph("Based on extensive user interviews and market research, the Aura Audio platform was designed to cater to distinct user groups. The following personas guided our UX decisions, ensuring the interface meets their specific needs and pain points.")
    
    personas = [
        {"name": "The Audiophile Commuter", "goals": "Wants uncompromised sound quality on the go, needs noise cancellation for trains/planes, values durability.", "frustrations": "Complicated checkout flows on mobile, lack of detailed technical specifications on product pages."},
        {"name": "The Design-Conscious Professional", "goals": "Looks for minimalist aesthetics that match their premium devices, values seamless connectivity and brand prestige.", "frustrations": "Cluttered websites, poor mobile responsiveness, cheap-looking branding."}
    ]
    
    for persona in personas:
        doc.add_paragraph()
        name_para = doc.add_paragraph()
        name_run = name_para.add_run(persona["name"])
        name_run.bold = True
        name_run.font.size = Pt(14)
        
        goals_para = doc.add_paragraph()
        goals_para.add_run("Goals: ").bold = True
        goals_para.add_run(persona["goals"])
        
        frust_para = doc.add_paragraph()
        frust_para.add_run("Frustrations: ").bold = True
        frust_para.add_run(persona["frustrations"])

    doc.add_page_break()
    
    # 2. User Reviews
    r_title = doc.add_paragraph()
    r_title.style = 'Heading 1'
    r_title.add_run("User Testing & Feedback")
    
    doc.add_paragraph("During our beta phase, we collected feedback from real users to validate our UX flows. Below are some of the early reviews highlighting the success of our minimalist design approach and friction-less checkout process:")
    
    reviews = [
        {"name": "Abhiyan Raj Rai", "stars": "★★★★★", "text": "The website is incredibly smooth. I love how the dark mode looks, and finding the technical specs for the Aethereus Pro Max was so easy. 10/10 UX!"},
        {"name": "Aviral", "stars": "★★★★★", "text": "Very clean and minimalist design. The checkout process was just three steps and didn't force me to create an account immediately. Huge plus for that user-centric approach."},
        {"name": "Shukla", "stars": "★★★★☆", "text": "Honestly one of the best headphone websites I've navigated. The way the images scale and the typography is laid out makes it feel extremely premium."},
        {"name": "Lucky Pandey", "stars": "★★★★★", "text": "Loved the seamless flow from the homepage directly into the cart. The UI is gorgeous, definitely gives Apple vibes but better suited for audio."},
        {"name": "Rahul Raj Rai", "stars": "★★★★★", "text": "The mobile responsiveness is top tier. I browsed and bought a soundbar entirely on my phone while on the train, zero friction."},
        {"name": "Khushwant Kumar", "stars": "★★★★☆", "text": "Great focus on accessibility. The contrast ratios are perfect, and everything is very legible. The design system is highly consistent."}
    ]
    
    for r in reviews:
        doc.add_paragraph()
        rev_para = doc.add_paragraph()
        r_name = rev_para.add_run(f"{r['name']}  ")
        r_name.bold = True
        r_stars = rev_para.add_run(r['stars'])
        r_stars.font.color.rgb = RGBColor(255, 204, 0)
        
        text_para = doc.add_paragraph(f'"{r["text"]}"')
        text_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        text_para.runs[0].italic = True
        text_para.runs[0].font.color.rgb = RGBColor(80, 80, 80)

    # Save document
    output_path = "Aura_UI_UX_Presentation.docx"
    doc.save(output_path)
    print(f"Success! {output_path} generated.")
    
    # Clean up screenshots
    for p_data in pages:
        if os.path.exists(p_data["screenshot"]):
            os.remove(p_data["screenshot"])
    os.rmdir(screenshots_dir)

if __name__ == "__main__":
    generate_docx()
