import os

# Define the common wrapper layout
layout_top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aura Audio | {title}</title>
    <meta name="description" content="Premium audio equipment and high-end headphones.">
    <link rel="stylesheet" href="css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">AURA</a>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="shop.html">Shop</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="reviews.html">Reviews</a></li>
                <li><a href="blog.html">Blog</a></li>
            </ul>
            <div class="nav-actions">
                <a href="cart.html" class="cart-icon" id="nav-cart-btn">Cart (0)</a>
                <a href="login.html" class="btn btn-outline">Sign In</a>
                <button class="mobile-menu-toggle" aria-label="Toggle Menu">&#9776;</button>
            </div>
        </div>
    </nav>

    <main class="page-content" id="page-content">
"""

layout_bottom = """
    </main>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-col">
                <h3>AURA</h3>
                <p>Uncompromised clarity. Minimalist design. The future of audio.</p>
            </div>
            <div class="footer-col">
                <h4>Shop</h4>
                <a href="shop.html">All Products</a>
                <a href="cart.html">Shopping Cart</a>
                <a href="checkout-shipping.html">Checkout</a>
            </div>
            <div class="footer-col">
                <h4>Company</h4>
                <a href="about.html">About Us</a>
                <a href="contact.html">Contact Support</a>
                <a href="faq.html">FAQ</a>
                <a href="blog.html">Blog</a>
            </div>
            <div class="footer-col">
                <h4>Legal & Info</h4>
                <a href="terms.html">Terms of Service</a>
                <a href="privacy.html">Privacy Policy</a>
                <a href="personas.html">UX Personas</a>
                <a href="design-system.html">Design System</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Aura Audio Technologies. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/app.js"></script>
</body>
</html>
"""

# Define unique content for all 23 pages
pages_data = {
    "index.html": {
        "title": "Home",
        "content": """
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
        
        <section class="hero-basic" style="padding: 0; min-height: 85vh; display: flex; align-items: center; background: url('images/hero_banner.jpg') center/cover no-repeat; position: relative;">
            <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.4);"></div>
            <div class="container" style="position: relative; z-index: 10; text-align: left; width: 100%;">
                <h1 style="font-size: 4.5rem; color: #fff; margin-bottom: 20px; text-shadow: 0 4px 20px rgba(0,0,0,0.8);">PURE<br>SOUND.</h1>
                <p style="font-size: 1.2rem; color: #f5f5f7; margin-bottom: 30px; max-width: 500px; text-shadow: 0 2px 10px rgba(0,0,0,0.8);">Experience uncompromised luxury with the new Aethereus series. Designed for perfection.</p>
                <a href="shop.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 15px 35px; background: #fff; color: #000;">Shop Collection</a>
            </div>
        </section>
        
        <section class="container" style="padding-top: 80px; padding-bottom: 80px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 40px;">
                <h2 style="font-size: 2.5rem;">Featured Products</h2>
                <a href="shop.html" style="color: var(--accent-primary); font-weight: 500;">View All &rarr;</a>
            </div>
            <div class="product-grid">
                <div class="product-card">
                    <a href="product-p1.html"><img src="images/product_pro_max.jpg" alt="Aethereus Pro Max" class="product-img"></a>
                    <div class="product-info">
                        <a href="product-p1.html"><h3 class="product-title">Aethereus Pro Max</h3></a>
                        <p class="product-price">$549.00</p>
                        <button class="btn btn-outline" onclick="handleAddToCartClick(event, 'p1')" style="width:100%">Add to Cart</button>
                    </div>
                </div>
                <div class="product-card">
                    <a href="product-p2.html"><img src="images/product_studio.jpg" alt="Aethereus Studio" class="product-img"></a>
                    <div class="product-info">
                        <a href="product-p2.html"><h3 class="product-title">Aethereus Studio</h3></a>
                        <p class="product-price">$349.00</p>
                        <button class="btn btn-outline" onclick="handleAddToCartClick(event, 'p2')" style="width:100%">Add to Cart</button>
                    </div>
                </div>
                <div class="product-card">
                    <a href="product-p3.html"><img src="images/product_pro_max.jpg" alt="Aethereus Lite" class="product-img"></a>
                    <div class="product-info">
                        <a href="product-p3.html"><h3 class="product-title">Aethereus Lite</h3></a>
                        <p class="product-price">$199.00</p>
                        <button class="btn btn-outline" onclick="handleAddToCartClick(event, 'p3')" style="width:100%">Add to Cart</button>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "shop.html": {
        "title": "Shop",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px;">
            <h1>Shop Collection</h1>
            <p>Explore our premium audio engineered for the modern audiophile.</p>
        </section>
        <section class="container" style="padding-bottom: 80px;">
            <div id="shop-grid" class="product-grid">
                <!-- JS WILL RENDER PRODUCTS HERE -->
            </div>
        </section>
        """
    },
    "product-details.html": {
        "title": "Aethereus Pro Max",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start;">
                <div style="background: var(--bg-secondary); padding: 40px; border-radius: var(--radius-md);">
                    <img src="images/product_headphone_1789213583711.jpg" alt="Aethereus Pro Max" style="width: 100%; height: auto; mix-blend-mode: multiply;">
                </div>
                <div>
                    <p style="color: var(--text-muted); text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem; margin-bottom: 10px;">Over-Ear Headphones</p>
                    <h1 style="font-size: 3rem; margin-bottom: 20px;">Aethereus Pro Max</h1>
                    <p style="font-size: 1.5rem; color: var(--text-main); margin-bottom: 30px;">$549.00</p>
                    <p style="color: var(--text-muted); font-size: 1.1rem; line-height: 1.6; margin-bottom: 40px;">Experience industry-leading noise cancellation combined with unmatched audio fidelity. The Aethereus Pro Max redefines the wireless listening experience with custom acoustic architecture and computational audio.</p>
                    
                    <div style="margin-bottom: 30px;">
                        <h4 style="margin-bottom: 10px;">Color</h4>
                        <div style="display: flex; gap: 10px;">
                            <div style="width: 30px; height: 30px; border-radius: 50%; background: #000; border: 2px solid var(--accent-primary); cursor: pointer;"></div>
                            <div style="width: 30px; height: 30px; border-radius: 50%; background: #e0e0e0; cursor: pointer;"></div>
                            <div style="width: 30px; height: 30px; border-radius: 50%; background: #2c3e50; cursor: pointer;"></div>
                        </div>
                    </div>
                    
                    <button class="btn btn-primary" onclick="handleAddToCartClick(event, 'p1')" style="width: 100%; padding: 15px; font-size: 1.1rem; margin-bottom: 20px;">Add to Cart</button>
                    
                    <ul style="color: var(--text-muted); list-style-position: inside; font-size: 0.9rem;">
                        <li style="margin-bottom: 8px;">Free shipping and returns</li>
                        <li style="margin-bottom: 8px;">2-year limited warranty</li>
                        <li>Up to 40 hours of listening time</li>
                    </ul>
                </div>
            </div>
        </section>
        """
    },
    "cart.html": {
        "title": "Shopping Cart",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 40px; background: none;">
            <h1 style="font-size: 2.5rem;">Shopping Cart</h1>
        </section>
        <section class="container" style="padding-bottom: 80px;">
            <div class="cart-layout">
                <div class="cart-items" id="cart-items-container">
                    <!-- JS WILL RENDER ITEMS HERE -->
                </div>
                <div class="cart-summary">
                    <h2 style="margin-bottom: 25px; font-size: 1.2rem;">Order Summary</h2>
                    <div class="summary-row"><span>Subtotal</span><span id="cart-subtotal">$0.00</span></div>
                    <div class="summary-row"><span>Estimated Shipping</span><span>Free</span></div>
                    <div class="summary-row"><span>Tax</span><span id="cart-tax">$0.00</span></div>
                    <div class="summary-total"><span>Total</span><span id="cart-total">$0.00</span></div>
                    <a href="checkout-shipping.html" class="btn btn-primary" style="width: 100%; margin-top: 30px;">Proceed to Checkout</a>
                    <a href="shop.html" class="btn btn-secondary" style="width: 100%; margin-top: 10px;">Continue Shopping</a>
                </div>
            </div>
        </section>
        """
    },
    "checkout-shipping.html": {
        "title": "Shipping Details",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 40px; background: none;">
            <h1 style="font-size: 2.5rem;">Secure Checkout</h1>
            <p>Step 1 of 2: Shipping Details</p>
        </section>
        <section class="container" style="padding-bottom: 80px; max-width: 800px;">
            <form action="checkout-payment.html" style="background: var(--bg-main); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 40px; box-shadow: var(--shadow-soft);">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                    <div>
                        <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">First Name</label>
                        <input type="text" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Last Name</label>
                        <input type="text" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                    </div>
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Street Address</label>
                    <input type="text" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 30px;">
                    <div>
                        <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">City</label>
                        <input type="text" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">State</label>
                        <select style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);"><option>California</option><option>New York</option><option>Texas</option></select>
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">ZIP Code</label>
                        <input type="text" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                    </div>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 15px;">Continue to Payment</button>
            </form>
        </section>
        """
    },
    "checkout-payment.html": {
        "title": "Payment",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 40px; background: none;">
            <h1 style="font-size: 2.5rem;">Secure Checkout</h1>
            <p>Step 2 of 2: Payment Details</p>
        </section>
        <section class="container" style="padding-bottom: 80px; max-width: 800px;">
            <div style="background: var(--bg-main); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 40px; text-align: center; box-shadow: var(--shadow-soft);">
                <h2 style="margin-bottom: 20px;">Scan to Pay</h2>
                <p style="color: var(--text-muted); margin-bottom: 30px;">Open your payment app and scan the QR code below to complete your secure transaction.</p>
                <div style="background: #fff; padding: 20px; display: inline-block; border-radius: var(--radius-sm); margin-bottom: 30px; border: 1px solid var(--border-color);">
                    <img src="images/dummy_qr_1789213596364.jpg" alt="Payment QR Code" style="width: 250px; height: 250px;">
                </div>
                <div>
                    <button id="confirm-payment" class="btn btn-primary" style="width: 100%; max-width: 300px; padding: 15px;" onclick="window.location.href='checkout-success.html'">Simulate Payment Complete</button>
                </div>
                <p style="margin-top: 15px; font-size: 0.9rem; color: var(--text-muted);"><a href="checkout-shipping.html" style="text-decoration: underline;">&larr; Back to Shipping</a></p>
            </div>
        </section>
        """
    },
    "checkout-success.html": {
        "title": "Order Success",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 80px; background: none; text-align: center;">
            <div style="width: 80px; height: 80px; background: #34c759; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 auto 30px;">&#10003;</div>
            <h1 style="font-size: 3rem; margin-bottom: 20px;">Order Confirmed</h1>
            <p style="font-size: 1.2rem; color: var(--text-muted); margin-bottom: 40px;">Thank you for your purchase. Your order number is <strong>#AURA-948271</strong>.</p>
            <p style="margin-bottom: 40px;">We've sent a confirmation email with your shipping details and tracking information.</p>
            <a href="shop.html" class="btn btn-primary" onclick="localStorage.removeItem('aura_cart')">Continue Shopping</a>
        </section>
        """
    },
    "login.html": {
        "title": "Login",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px; max-width: 500px;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h1 style="font-size: 2.5rem; margin-bottom: 10px;">Welcome Back</h1>
                <p style="color: var(--text-muted);">Sign in to your Aura account</p>
            </div>
            <form action="profile.html" style="background: var(--bg-main); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 40px; box-shadow: var(--shadow-soft);">
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Email Address</label>
                    <input type="email" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                </div>
                <div style="margin-bottom: 30px;">
                    <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Password</label>
                    <input type="password" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 15px;">Sign In</button>
                <div style="text-align: center; margin-top: 20px; font-size: 0.9rem;">
                    <a href="register.html" style="color: var(--accent-primary);">Don't have an account? Sign up</a>
                </div>
            </form>
        </section>
        """
    },
    "register.html": {
        "title": "Register",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px; max-width: 500px;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h1 style="font-size: 2.5rem; margin-bottom: 10px;">Create Account</h1>
                <p style="color: var(--text-muted);">Join the Aura Audio family</p>
            </div>
            <form action="profile.html" style="background: var(--bg-main); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 40px; box-shadow: var(--shadow-soft);">
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Full Name</label>
                    <input type="text" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Email Address</label>
                    <input type="email" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                </div>
                <div style="margin-bottom: 30px;">
                    <label style="display: block; margin-bottom: 8px; font-size: 0.9rem;">Password</label>
                    <input type="password" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 15px;">Create Account</button>
                <div style="text-align: center; margin-top: 20px; font-size: 0.9rem;">
                    <a href="login.html" style="color: var(--accent-primary);">Already have an account? Sign in</a>
                </div>
            </form>
        </section>
        """
    },
    "profile.html": {
        "title": "User Profile",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: 250px 1fr; gap: 40px;">
                <div style="background: var(--bg-secondary); padding: 30px; border-radius: var(--radius-md);">
                    <h3 style="margin-bottom: 20px;">My Account</h3>
                    <ul style="list-style: none; font-size: 1rem; line-height: 2;">
                        <li><a href="profile.html" style="font-weight: 600; color: var(--accent-primary);">Profile Details</a></li>
                        <li><a href="orders.html">Order History</a></li>
                        <li><a href="wishlist.html">Wishlist</a></li>
                        <li><a href="login.html" style="color: #ff3b30;">Log Out</a></li>
                    </ul>
                </div>
                <div>
                    <h1 style="margin-bottom: 30px;">Profile Details</h1>
                    <div style="background: var(--bg-main); padding: 40px; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-soft);">
                        <p style="margin-bottom: 20px;"><strong>Name:</strong> John Doe</p>
                        <p style="margin-bottom: 20px;"><strong>Email:</strong> john.doe@example.com</p>
                        <p style="margin-bottom: 20px;"><strong>Member Since:</strong> January 2026</p>
                        <button class="btn btn-outline" style="margin-top: 20px;">Edit Information</button>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "orders.html": {
        "title": "Order History",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: 250px 1fr; gap: 40px;">
                <div style="background: var(--bg-secondary); padding: 30px; border-radius: var(--radius-md);">
                    <h3 style="margin-bottom: 20px;">My Account</h3>
                    <ul style="list-style: none; font-size: 1rem; line-height: 2;">
                        <li><a href="profile.html">Profile Details</a></li>
                        <li><a href="orders.html" style="font-weight: 600; color: var(--accent-primary);">Order History</a></li>
                        <li><a href="wishlist.html">Wishlist</a></li>
                        <li><a href="login.html" style="color: #ff3b30;">Log Out</a></li>
                    </ul>
                </div>
                <div>
                    <h1 style="margin-bottom: 30px;">Order History</h1>
                    <table style="width: 100%; border-collapse: collapse; text-align: left;">
                        <tr style="border-bottom: 2px solid var(--border-color);">
                            <th style="padding: 15px 0;">Order #</th>
                            <th style="padding: 15px 0;">Date</th>
                            <th style="padding: 15px 0;">Status</th>
                            <th style="padding: 15px 0;">Total</th>
                        </tr>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 15px 0;">#AURA-8371</td>
                            <td style="padding: 15px 0; color: var(--text-muted);">Aug 15, 2026</td>
                            <td style="padding: 15px 0;"><span style="background: #e5f6eb; color: #1e7e34; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem;">Delivered</span></td>
                            <td style="padding: 15px 0;">$549.00</td>
                        </tr>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 15px 0;">#AURA-6523</td>
                            <td style="padding: 15px 0; color: var(--text-muted);">Feb 02, 2026</td>
                            <td style="padding: 15px 0;"><span style="background: #e5f6eb; color: #1e7e34; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem;">Delivered</span></td>
                            <td style="padding: 15px 0;">$199.00</td>
                        </tr>
                    </table>
                </div>
            </div>
        </section>
        """
    },
    "wishlist.html": {
        "title": "Wishlist",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: 250px 1fr; gap: 40px;">
                <div style="background: var(--bg-secondary); padding: 30px; border-radius: var(--radius-md);">
                    <h3 style="margin-bottom: 20px;">My Account</h3>
                    <ul style="list-style: none; font-size: 1rem; line-height: 2;">
                        <li><a href="profile.html">Profile Details</a></li>
                        <li><a href="orders.html">Order History</a></li>
                        <li><a href="wishlist.html" style="font-weight: 600; color: var(--accent-primary);">Wishlist</a></li>
                        <li><a href="login.html" style="color: #ff3b30;">Log Out</a></li>
                    </ul>
                </div>
                <div>
                    <h1 style="margin-bottom: 30px;">My Wishlist</h1>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div style="border: 1px solid var(--border-color); padding: 20px; border-radius: var(--radius-md); display: flex; align-items: center; gap: 20px;">
                            <img src="images/product_headphone_1789213583711.jpg" alt="Aethereus Studio" style="width: 80px; height: 80px; object-fit: contain; filter: hue-rotate(180deg);">
                            <div>
                                <h4 style="margin-bottom: 5px;">Aethereus Studio</h4>
                                <p style="color: var(--text-muted); margin-bottom: 10px;">$349.00</p>
                                <button class="btn btn-outline" style="padding: 5px 15px; font-size: 0.8rem;" onclick="handleAddToCartClick(event, 'p2')">Move to Cart</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "about.html": {
        "title": "About Us",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px;">
            <h1>Our Story</h1>
            <p>The pursuit of acoustic perfection.</p>
        </section>
        <section class="container" style="padding-bottom: 80px; max-width: 800px; text-align: center;">
            <p style="font-size: 1.2rem; line-height: 1.8; color: var(--text-main); margin-bottom: 30px;">Aura Audio was founded in 2026 with a single, uncompromising vision: to bridge the gap between audiophile-grade fidelity and stunning minimalist design.</p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 30px;">For too long, true high-fidelity audio equipment has been bulky, complicated, and confined to the studio. We believed that pristine sound should be accessible in an elegant form factor that you can wear anywhere.</p>
            <img src="images/product_pro_max.jpg" alt="Aura Headphones" style="width: 100%; max-width: 600px; border-radius: var(--radius-md); margin-top: 40px; margin-bottom: 40px; box-shadow: var(--shadow-soft);">
            <h2 style="font-size: 2rem; margin-bottom: 20px;">Engineering Excellence</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-muted);">Every component in an Aura product is custom-designed. From the neodymium magnets to the memory foam ear cushions, we obsess over every millimeter and micro-gram to deliver an experience that simply elevates your senses.</p>
        </section>
        """
    },
    "contact.html": {
        "title": "Contact",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px;">
            <h1>Get in Touch</h1>
            <p>We're here to assist you with any questions or support.</p>
        </section>
        <section class="container" style="padding-bottom: 80px; display: grid; grid-template-columns: 1fr 1fr; gap: 60px;">
            <div>
                <h3 style="font-size: 1.5rem; margin-bottom: 20px;">Send us a message</h3>
                <form action="index.html">
                    <div style="margin-bottom: 20px;">
                        <input type="text" placeholder="Your Name" required style="width: 100%; padding: 15px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                    </div>
                    <div style="margin-bottom: 20px;">
                        <input type="email" placeholder="Your Email" required style="width: 100%; padding: 15px; border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                    </div>
                    <div style="margin-bottom: 20px;">
                        <textarea placeholder="Your Message" rows="5" required style="width: 100%; padding: 15px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-family: inherit; resize: vertical;"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
            </div>
            <div style="background: var(--bg-secondary); padding: 40px; border-radius: var(--radius-md);">
                <h3 style="font-size: 1.5rem; margin-bottom: 20px;">Global Headquarters</h3>
                <p style="color: var(--text-muted); margin-bottom: 30px; line-height: 1.6;">100 Acoustic Way<br>Suite 400<br>San Francisco, CA 94107<br>United States</p>
                <h3 style="font-size: 1.2rem; margin-bottom: 10px;">Support Hours</h3>
                <p style="color: var(--text-muted); margin-bottom: 30px;">Mon - Fri: 9am - 6pm PST<br>Sat - Sun: Closed</p>
                <h3 style="font-size: 1.2rem; margin-bottom: 10px;">Direct Contact</h3>
                <p style="color: var(--text-muted);">support@auraaudio.com<br>1-800-555-0199</p>
            </div>
        </section>
        """
    },
    "faq.html": {
        "title": "FAQ",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px;">
            <h1>Frequently Asked Questions</h1>
            <p>Find answers to common questions about our products.</p>
        </section>
        <section class="container" style="padding-bottom: 80px; max-width: 800px;">
            <div style="border-bottom: 1px solid var(--border-color); padding: 20px 0;">
                <h3 style="font-size: 1.2rem; margin-bottom: 10px;">Do Aura headphones support spatial audio?</h3>
                <p style="color: var(--text-muted); line-height: 1.6;">Yes, both the Aethereus Pro Max and Studio models support fully immersive spatial audio with dynamic head tracking on compatible devices.</p>
            </div>
            <div style="border-bottom: 1px solid var(--border-color); padding: 20px 0;">
                <h3 style="font-size: 1.2rem; margin-bottom: 10px;">What is the warranty period?</h3>
                <p style="color: var(--text-muted); line-height: 1.6;">All Aura products come with a standard 2-year limited warranty covering manufacturing defects.</p>
            </div>
            <div style="border-bottom: 1px solid var(--border-color); padding: 20px 0;">
                <h3 style="font-size: 1.2rem; margin-bottom: 10px;">How long does the battery last?</h3>
                <p style="color: var(--text-muted); line-height: 1.6;">The Aethereus Pro Max provides up to 40 hours of listening time with Active Noise Cancellation enabled. A quick 10-minute charge gives you 5 hours of playback.</p>
            </div>
            <div style="padding: 20px 0;">
                <h3 style="font-size: 1.2rem; margin-bottom: 10px;">What is your return policy?</h3>
                <p style="color: var(--text-muted); line-height: 1.6;">We offer a 30-day, no-questions-asked return policy. If you aren't completely satisfied, simply return the product in its original packaging for a full refund.</p>
            </div>
        </section>
        """
    },
    "blog.html": {
        "title": "Blog",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px;">
            <h1>Aura News</h1>
            <p>Latest updates, audio tips, and industry news.</p>
        </section>
        <section class="container" style="padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px;">
                <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden;">
                    <div style="height: 200px; background: url('images/product_pro_max.jpg') center/cover;"></div>
                    <div style="padding: 30px;">
                        <p style="font-size: 0.8rem; color: var(--accent-primary); text-transform: uppercase; font-weight: 600; margin-bottom: 10px;">Product Update</p>
                        <h3 style="font-size: 1.3rem; margin-bottom: 15px;">Introducing the Aethereus Pro Max</h3>
                        <p style="color: var(--text-muted); margin-bottom: 20px; line-height: 1.6;">Our flagship headphone has arrived. Discover the engineering behind our most advanced acoustic architecture yet.</p>
                        <a href="blog-post-1.html" style="font-weight: 500; color: var(--text-main);">Read Article &rarr;</a>
                    </div>
                </div>
                <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden;">
                    <div style="height: 200px; background: url('images/product_studio.jpg') center/cover;"></div>
                    <div style="padding: 30px;">
                        <p style="font-size: 0.8rem; color: var(--accent-primary); text-transform: uppercase; font-weight: 600; margin-bottom: 10px;">Education</p>
                        <h3 style="font-size: 1.3rem; margin-bottom: 15px;">Understanding Active Noise Cancellation</h3>
                        <p style="color: var(--text-muted); margin-bottom: 20px; line-height: 1.6;">How exactly do headphones silence the world around you? A deep dive into the computational algorithms.</p>
                        <a href="blog-post-2.html" style="font-weight: 500; color: var(--text-main);">Read Article &rarr;</a>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "blog-post-1.html": {
        "title": "Introducing Pro Max",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px; max-width: 800px;">
            <p style="color: var(--accent-primary); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px;">Product Update</p>
            <h1 style="font-size: 3rem; margin-bottom: 20px; line-height: 1.2;">Introducing the Aethereus Pro Max</h1>
            <p style="color: var(--text-muted); margin-bottom: 40px;">Published on September 12, 2026 &bull; 5 min read</p>
            <div style="width: 100%; height: 400px; background: url('images/product_pro_max.jpg') center/cover; border-radius: var(--radius-md); margin-bottom: 40px;"></div>
            <div style="font-size: 1.1rem; line-height: 1.8; color: var(--text-main);">
                <p style="margin-bottom: 25px;">Today marks a significant milestone for Aura Audio. After three years of rigorous research and development, we are thrilled to unveil our flagship wireless headphones: the Aethereus Pro Max.</p>
                <h3 style="font-size: 1.8rem; margin: 40px 0 20px;">Redefining the Acoustic Standard</h3>
                <p style="margin-bottom: 25px;">The Pro Max features an entirely new 40mm dynamic driver, engineered in-house to deliver a frequency response that rivals wired studio monitors. But we didn't stop at the hardware. Driven by our custom H2 compute chip, the active noise cancellation adapts to your environment 200 times per second.</p>
                <blockquote style="border-left: 4px solid var(--accent-primary); padding-left: 20px; font-style: italic; font-size: 1.3rem; margin: 40px 0;">"Our goal wasn't just to make a great headphone. It was to completely erase the barrier between the listener and the music."</blockquote>
                <p style="margin-bottom: 25px;">The Aethereus Pro Max is available today globally. Experience sound like never before.</p>
            </div>
            <a href="blog.html" class="btn btn-outline" style="margin-top: 40px;">&larr; Back to all articles</a>
        </section>
        """
    },
    "blog-post-2.html": {
        "title": "Understanding ANC",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px; max-width: 800px;">
            <p style="color: var(--accent-primary); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px;">Education</p>
            <h1 style="font-size: 3rem; margin-bottom: 20px; line-height: 1.2;">Understanding Active Noise Cancellation</h1>
            <p style="color: var(--text-muted); margin-bottom: 40px;">Published on September 05, 2026 &bull; 7 min read</p>
            <div style="width: 100%; height: 400px; background: url('images/product_studio.jpg') center/cover; border-radius: var(--radius-md); margin-bottom: 40px;"></div>
            <div style="font-size: 1.1rem; line-height: 1.8; color: var(--text-main);">
                <p style="margin-bottom: 25px;">Active Noise Cancellation (ANC) has become a staple in modern premium headphones, but the technology behind it is nothing short of computational magic.</p>
                <h3 style="font-size: 1.8rem; margin: 40px 0 20px;">The Physics of Silence</h3>
                <p style="margin-bottom: 25px;">At its core, sound is a wave of air pressure. ANC works on the principle of destructive interference. Microphones on the outside (and inside) of the headphone earcups constantly monitor ambient noise.</p>
                <p style="margin-bottom: 25px;">Once this noise is detected, a digital signal processor (DSP) generates an inverted sound wave—an exact mirror image of the noise—and plays it through the speakers alongside your music. When the external noise wave and the internal anti-noise wave meet, they cancel each other out, leaving you with pure silence.</p>
            </div>
            <a href="blog.html" class="btn btn-outline" style="margin-top: 40px;">&larr; Back to all articles</a>
        </section>
        """
    },
    "reviews.html": {
        "title": "Reviews",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 40px; background: none;">
            <h1 style="font-size: 2.5rem;">Customer Reviews</h1>
            <p>See what our listeners have to say about Aura Audio.</p>
        </section>
        <section class="container" style="padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div style="background: var(--bg-main); padding: 30px; border-radius: var(--radius-md); box-shadow: var(--shadow-soft);">
                    <div style="display: flex; align-items: center; margin-bottom: 20px;">
                        <img src="images/avatar_indian_1.jpg" alt="Rohan J." style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; margin-right: 15px;">
                        <div>
                            <h3 style="font-size: 1.1rem; margin-bottom: 5px;">Rohan Joshi</h3>
                            <div style="color: #FFD700; font-size: 0.9rem;">★★★★★</div>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-style: italic; line-height: 1.6;">"Honestly blown away by the Aethereus Pro. The noise cancellation is unreal, especially during my daily commute. They're a bit pricey, but the build quality and sound clarity make it completely worth the investment."</p>
                </div>
                <div style="background: var(--bg-main); padding: 30px; border-radius: var(--radius-md); box-shadow: var(--shadow-soft);">
                    <div style="display: flex; align-items: center; margin-bottom: 20px;">
                        <img src="images/avatar_indian_2.jpg" alt="Neha T." style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; margin-right: 15px;">
                        <div>
                            <h3 style="font-size: 1.1rem; margin-bottom: 5px;">Neha Thakur</h3>
                            <div style="color: #FFD700; font-size: 0.9rem;">★★★★★</div>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-style: italic; line-height: 1.6;">"I'm an audio engineer and I usually avoid 'lifestyle' brands, but Aura Audio really nailed the frequency response on the Studio ANC models. The bass is punchy without muddying the mids. Plus, they look incredibly sleek."</p>
                </div>
                <div style="background: var(--bg-main); padding: 30px; border-radius: var(--radius-md); box-shadow: var(--shadow-soft);">
                    <div style="display: flex; align-items: center; margin-bottom: 20px;">
                        <div style="width: 60px; height: 60px; border-radius: 50%; background: var(--accent-primary); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.2rem; margin-right: 15px;">AK</div>
                        <div>
                            <h3 style="font-size: 1.1rem; margin-bottom: 5px;">Amit K.</h3>
                            <div style="color: #FFD700; font-size: 0.9rem;">★★★★☆</div>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-style: italic; line-height: 1.6;">"Great battery life and very comfortable for long listening sessions. I took off one star because the carrying case is a little bulky for my everyday bag, but otherwise, absolutely stellar performance."</p>
                </div>
            </div>
        </section>
        """
    },
    "terms.html": {
        "title": "Terms of Service",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px; background: none;">
            <h1>Terms of Service</h1>
            <p>Last updated: September 2026</p>
        </section>
        <section class="container" style="padding-bottom: 80px; max-width: 800px; color: var(--text-muted); line-height: 1.8;">
            <h2 style="color: var(--text-main); margin: 30px 0 15px;">1. Agreement to Terms</h2>
            <p style="margin-bottom: 20px;">By accessing our website and purchasing our products, you agree to be bound by these Terms of Service. If you disagree with any part of the terms, you do not have permission to access the Service.</p>
            <h2 style="color: var(--text-main); margin: 30px 0 15px;">2. Purchases and Payment</h2>
            <p style="margin-bottom: 20px;">We accept various forms of payment. By submitting payment information, you grant us the right to provide the information to third parties for purposes of facilitating the completion of Purchases.</p>
            <h2 style="color: var(--text-main); margin: 30px 0 15px;">3. Returns and Refunds</h2>
            <p style="margin-bottom: 20px;">Our Return & Refund Policy provides you with 30 days to return a product. See our full Return Policy page for detailed instructions.</p>
        </section>
        """
    },
    "privacy.html": {
        "title": "Privacy Policy",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px; background: none;">
            <h1>Privacy Policy</h1>
            <p>Your privacy is critically important to us.</p>
        </section>
        <section class="container" style="padding-bottom: 80px; max-width: 800px; color: var(--text-muted); line-height: 1.8;">
            <p style="margin-bottom: 20px;">It is Aura Audio's policy to respect your privacy regarding any information we may collect while operating our website. This Privacy Policy applies to auraaudio.com.</p>
            <h2 style="color: var(--text-main); margin: 30px 0 15px;">Website Visitors</h2>
            <p style="margin-bottom: 20px;">Like most website operators, Aura collects non-personally-identifying information of the sort that web browsers and servers typically make available, such as the browser type, language preference, and the date and time of each visitor request.</p>
            <h2 style="color: var(--text-main); margin: 30px 0 15px;">Gathering of Personally-Identifying Information</h2>
            <p style="margin-bottom: 20px;">Certain visitors to our websites choose to interact with us in ways that require us to gather personally-identifying information (such as entering shipping addresses for orders).</p>
        </section>
        """
    },
    "404.html": {
        "title": "Page Not Found",
        "content": """
        <section class="container" style="padding-top: 160px; padding-bottom: 100px; text-align: center;">
            <h1 style="font-size: 6rem; color: var(--accent-primary); margin-bottom: 10px;">404</h1>
            <h2 style="font-size: 2rem; margin-bottom: 20px;">Oops! Page Not Found</h2>
            <p style="color: var(--text-muted); margin-bottom: 40px; font-size: 1.1rem;">The page you are looking for doesn't exist or has been moved.</p>
            <a href="index.html" class="btn btn-primary">Return Home</a>
        </section>
        """
    },
    "personas.html": {
        "title": "UX Personas",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px; background: none;">
            <h1>UX Personas</h1>
            <p>Target audience research for the Aura Audio UI/UX Project.</p>
        </section>
        <section class="container" style="padding-bottom: 80px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
                <!-- Persona 1 -->
                <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 40px; background: var(--bg-main);">
                    <div style="display: flex; align-items: center; margin-bottom: 30px;">
                        <div style="width: 80px; height: 80px; border-radius: 50%; background: #e0e0e0; margin-right: 20px;"></div>
                        <div>
                            <h2 style="margin-bottom: 5px;">"The Audiophile Professional"</h2>
                            <p style="color: var(--text-muted);">Alex, 32 &bull; Sound Engineer</p>
                        </div>
                    </div>
                    <h4 style="margin-bottom: 10px;">Goals</h4>
                    <ul style="color: var(--text-muted); margin-bottom: 20px; list-style-position: inside;">
                        <li>Requires flat frequency response for accurate mixing.</li>
                        <li>Wants all-day comfort for 8+ hour studio sessions.</li>
                    </ul>
                    <h4 style="margin-bottom: 10px;">Pain Points</h4>
                    <ul style="color: var(--text-muted); list-style-position: inside;">
                        <li>Frustrated by "bassy" lifestyle brands.</li>
                        <li>Hates clumsy UI when trying to compare technical specs.</li>
                    </ul>
                </div>
                <!-- Persona 2 -->
                <div style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 40px; background: var(--bg-main);">
                    <div style="display: flex; align-items: center; margin-bottom: 30px;">
                        <div style="width: 80px; height: 80px; border-radius: 50%; background: #e0e0e0; margin-right: 20px;"></div>
                        <div>
                            <h2 style="margin-bottom: 5px;">"The Remote Worker"</h2>
                            <p style="color: var(--text-muted);">Sam, 28 &bull; Tech Consultant</p>
                        </div>
                    </div>
                    <h4 style="margin-bottom: 10px;">Goals</h4>
                    <ul style="color: var(--text-muted); margin-bottom: 20px; list-style-position: inside;">
                        <li>Needs top-tier ANC to block out coffee shop noise.</li>
                        <li>Wants a premium, sleek look for video calls.</li>
                    </ul>
                    <h4 style="margin-bottom: 10px;">Pain Points</h4>
                    <ul style="color: var(--text-muted); list-style-position: inside;">
                        <li>Battery anxiety during long travel days.</li>
                        <li>Needs a seamless, fast checkout experience on mobile.</li>
                    </ul>
                </div>
            </div>
        </section>
        """
    },
    "design-system.html": {
        "title": "Design System",
        "content": """
        <section class="hero-basic" style="padding-top: 140px; padding-bottom: 60px; background: none;">
            <h1>UI Design System</h1>
            <p>Styleguide components for the Aura Audio project.</p>
        </section>
        <section class="container" style="padding-bottom: 80px;">
            <div style="margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px;">Typography</h2>
                <h1 style="font-size: 3rem; margin-bottom: 10px;">Heading 1 - Inter 600</h1>
                <h2 style="font-size: 2rem; margin-bottom: 10px;">Heading 2 - Inter 600</h2>
                <h3 style="font-size: 1.5rem; margin-bottom: 10px;">Heading 3 - Inter 600</h3>
                <p style="font-size: 1rem; color: var(--text-muted);">Body Text - Inter 400. Used for paragraphs and descriptions. The quick brown fox jumps over the lazy dog.</p>
            </div>
            <div style="margin-bottom: 60px;">
                <h2 style="margin-bottom: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px;">Colors</h2>
                <div style="display: flex; gap: 20px;">
                    <div><div style="width: 100px; height: 100px; background: #ffffff; border: 1px solid #ddd; border-radius: 8px;"></div><p style="text-align: center; margin-top: 10px;">Bg Main</p></div>
                    <div><div style="width: 100px; height: 100px; background: #f5f5f7; border: 1px solid #ddd; border-radius: 8px;"></div><p style="text-align: center; margin-top: 10px;">Bg Secondary</p></div>
                    <div><div style="width: 100px; height: 100px; background: #0071e3; border-radius: 8px;"></div><p style="text-align: center; margin-top: 10px;">Accent</p></div>
                    <div><div style="width: 100px; height: 100px; background: #1d1d1f; border-radius: 8px;"></div><p style="text-align: center; margin-top: 10px;">Text Main</p></div>
                </div>
            </div>
            <div>
                <h2 style="margin-bottom: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px;">Buttons</h2>
                <button class="btn btn-primary" style="margin-right: 10px;">Primary Button</button>
                <button class="btn btn-secondary" style="margin-right: 10px;">Secondary Button</button>
                <button class="btn btn-outline">Outline Button</button>
            </div>
        </section>
        """
    },
    "404.html": {
        "title": "Page Not Found",
        "content": """
        <section class="container" style="padding-top: 140px; padding-bottom: 80px; text-align: center;">
            <h1 style="font-size: 6rem; font-weight: 700; color: var(--text-main); margin-bottom: 20px;">404</h1>
            <h2 style="font-size: 2rem; margin-bottom: 20px;">Lost in the Soundscape</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 40px; max-width: 500px; margin-left: auto; margin-right: auto;">The page you are looking for has been moved or no longer exists. Let's get you back to the music.</p>
            <a href="index.html" class="btn btn-primary" style="padding: 15px 30px; font-size: 1.1rem;">Return Home</a>
        </section>
        """
    },
    "title.html": {
        "title": "Project Title",
        "content": """
        <section class="container" style="padding-top: 15vh; text-align: center; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h3 style="color: var(--accent-primary); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 20px;">Aura Audio</h3>
            <h1 style="font-size: 4rem; margin-bottom: 20px;">UI/UX Minor/Major Project</h1>
            <h2 style="font-size: 2rem; color: var(--text-muted);">Amity University</h2>
        </section>
        """
    },
    "thank-you.html": {
        "title": "Thank You",
        "content": """
        <section class="container" style="padding-top: 10vh; text-align: center; height: 100vh;">
            <h1 style="font-size: 4rem; margin-bottom: 40px;">Thank You</h1>
            <div style="background: var(--bg-secondary); padding: 50px; border-radius: var(--radius-md); max-width: 600px; margin: 0 auto; text-align: left; box-shadow: var(--shadow-soft);">
                <h2 style="font-size: 2rem; margin-bottom: 30px; text-align: center;">Developer Details</h2>
                <p style="font-size: 1.2rem; margin-bottom: 15px;"><strong>Name:</strong> Shivam Tanwar</p>
                <p style="font-size: 1.2rem; margin-bottom: 15px;"><strong>Enrollment Number:</strong> A2305324022</p>
                <p style="font-size: 1.2rem; margin-bottom: 15px;"><strong>Course:</strong> B.Tech - Information Technology</p>
                <p style="font-size: 1.2rem;"><strong>Year:</strong> 2024-2025</p>
            </div>
        </section>
        """
    }
}
# Write out the HTML files
for filename, data in pages_data.items():
    title = data["title"]
    content = data["content"]
    
    if filename in ["title.html", "thank-you.html"]:
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-main: #ffffff;
            --bg-secondary: #f5f5f7;
            --text-main: #1d1d1f;
            --text-muted: #86868b;
            --accent-primary: #0071e3;
            --border-color: #d2d2d7;
            --radius-md: 18px;
            --shadow-soft: 0 10px 30px rgba(0,0,0,0.05);
        }}
        body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; font-family: 'Inter', sans-serif; background: #fff; color: #111; }}
        h1, h2, h3, p {{ margin: 0; padding: 0; }}
        .container {{ width: 100%; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; }}
    </style>
</head>
<body>
    {content}
</body>
</html>"""
    else:
        html = layout_top.replace("{title}", title) + content + layout_bottom
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Successfully generated 23 completely unique and fully formatted pages.")
