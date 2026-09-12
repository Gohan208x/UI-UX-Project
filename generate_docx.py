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

def generate_docx():
    # 1. Take screenshots
    cwd = os.getcwd()
    screenshots_dir = os.path.join(cwd, "screenshots_tmp")
    os.makedirs(screenshots_dir, exist_ok=True)
    
    print("Launching headless browser to take screenshots...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a desktop viewport size
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        
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
    
    # Configure document for Landscape A3
    # A3 size: 16.54 inches wide x 11.69 inches high
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Inches(16.54)
    section.page_height = Inches(11.69)
    # Reduce margins, add large top margin to center Y-axis
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(2.5)
    section.bottom_margin = Inches(0.5)
    
    # Customize styles
    styles = doc.styles
    title_style = styles['Heading 1']
    title_font = title_style.font
    title_font.name = 'Arial'
    title_font.size = Pt(24)
    title_font.color.rgb = RGBColor(0, 0, 0)
    
    for i, p_data in enumerate(pages):
        if p_data["file"] in ["title.html", "thank-you.html"]:
            # Full width image for plain slides
            paragraph = doc.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.add_picture(p_data["screenshot"], width=Inches(15.5))
        else:
            # We will use a table to create a side-by-side layout.
            table = doc.add_table(rows=1, cols=2)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.allow_autofit = False
            
            # Adjust column widths for A3 Landscape
            width_left = Inches(10)
            width_right = Inches(5)
            table.columns[0].width = width_left
            table.columns[1].width = width_right
            
            row = table.rows[0]
            cell_left = row.cells[0]
            cell_right = row.cells[1]
            
            cell_left.width = width_left
            cell_right.width = width_right
            
            cell_left.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_right.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            # Add image to left cell
            paragraph = cell_left.paragraphs[0]
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.add_picture(p_data["screenshot"], width=Inches(9.5))
            
            # Add text to right cell
            title_para = cell_right.paragraphs[0]
            title_para.style = 'Heading 1'
            title_para.add_run(p_data["title"])
            
            # Add tags
            tags_para = cell_right.add_paragraph()
            tags_run = tags_para.add_run(f"Tags: {', '.join(p_data['tags'])}")
            tags_run.italic = True
            tags_run.font.color.rgb = RGBColor(100, 100, 100)
            
            # Add spacing
            cell_right.add_paragraph()
            
            # Add description with increased font size
            desc_para = cell_right.add_paragraph()
            desc_run = desc_para.add_run(p_data["desc"])
            desc_run.font.size = Pt(18)
            desc_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # Page break for all but the last page
        if i < len(pages) - 1:
            doc.add_page_break()

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
