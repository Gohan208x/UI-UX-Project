/**
 * AURA AUDIO - Main JavaScript
 * Fully operational cart using localStorage.
 */

// 1. PRODUCT DATABASE (Simulating a backend)
const products = [
    {
        id: 'p1',
        title: 'Aethereus Pro Max',
        price: 549.00,
        image: 'images/product_pro_max.jpg',
        description: 'Industry-leading noise cancellation with unmatched fidelity.'
    },
    {
        id: 'p2',
        title: 'Aethereus Studio',
        price: 349.00,
        image: 'images/product_studio.jpg',
        description: 'Studio-quality reference audio for creators.'
    },
    {
        id: 'p3',
        title: 'Aethereus Lite',
        price: 199.00,
        image: 'images/product_pro_max.jpg', // Using pro max as it's a sleek headphone
        description: 'Everyday comfort and premium sound.'
    },
    {
        id: 'p4',
        title: 'Aura Soundbar X',
        price: 899.00,
        image: 'images/product_soundbar.jpg',
        description: 'Cinematic spatial audio for your living room.'
    }
];

// 2. STATE MANAGEMENT
let cart = JSON.parse(localStorage.getItem('aura_cart')) || [];

function saveCart() {
    localStorage.setItem('aura_cart', JSON.stringify(cart));
    updateCartIcon();
}

function updateCartIcon() {
    const navCartBtn = document.getElementById('nav-cart-btn');
    if (navCartBtn) {
        navCartBtn.textContent = `Cart (${cart.length})`;
    }
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push(product);
        saveCart();
    }
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
    renderCartPage(); // Re-render if on cart page
}

// 3. UI RENDERING

// Render Shop Page
function renderShopPage() {
    const shopContainer = document.getElementById('shop-grid');
    if (!shopContainer) return;
    
    shopContainer.innerHTML = '';
    
    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <a href="product-${product.id}.html">
                <img src="${product.image}" alt="${product.title}" class="product-img">
            </a>
            <div class="product-info">
                <a href="product-${product.id}.html">
                    <h3 class="product-title">${product.title}</h3>
                </a>
                <p class="product-price">$${product.price.toFixed(2)}</p>
                <button class="btn btn-outline" onclick="handleAddToCartClick(event, '${product.id}')" style="width:100%">Add to Cart</button>
            </div>
        `;
        shopContainer.appendChild(card);
    });
}

// Handle Cart Button Click (with visual feedback)
window.handleAddToCartClick = function(e, productId) {
    e.preventDefault();
    const btn = e.target;
    
    addToCart(productId);
    
    const originalText = btn.textContent;
    btn.textContent = 'Added';
    btn.classList.add('btn-primary');
    btn.classList.remove('btn-outline');
    
    setTimeout(() => {
        btn.textContent = originalText;
        btn.classList.remove('btn-primary');
        btn.classList.add('btn-outline');
    }, 1500);
}

// Render Cart Page
function renderCartPage() {
    const cartItemsContainer = document.getElementById('cart-items-container');
    const subtotalEl = document.getElementById('cart-subtotal');
    const taxEl = document.getElementById('cart-tax');
    const totalEl = document.getElementById('cart-total');
    
    if (!cartItemsContainer) return;

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p style="color: var(--text-muted); padding: 40px; text-align:center;">Your cart is empty.</p>';
        subtotalEl.textContent = '$0.00';
        taxEl.textContent = '$0.00';
        totalEl.textContent = '$0.00';
        return;
    }

    cartItemsContainer.innerHTML = '';
    let subtotal = 0;

    cart.forEach((item, index) => {
        subtotal += item.price;
        const itemEl = document.createElement('div');
        itemEl.className = 'cart-item';
        itemEl.innerHTML = `
            <img src="${item.image}" alt="${item.title}">
            <div class="cart-item-info">
                <h3 class="cart-item-title">${item.title}</h3>
                <p class="cart-item-price">$${item.price.toFixed(2)}</p>
            </div>
            <button class="btn btn-outline" style="padding: 8px 16px; font-size: 0.8rem;" onclick="removeFromCart(${index})">Remove</button>
        `;
        cartItemsContainer.appendChild(itemEl);
    });

    const tax = subtotal * 0.08; // 8% dummy tax
    const total = subtotal + tax;

    subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
    taxEl.textContent = `$${tax.toFixed(2)}`;
    totalEl.textContent = `$${total.toFixed(2)}`;
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateCartIcon();
    renderShopPage();
    renderCartPage();
    
    // Mobile menu logic
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '100%';
            navLinks.style.left = '0';
            navLinks.style.width = '100%';
            navLinks.style.background = 'var(--bg-glass)';
            navLinks.style.padding = '20px';
        });
    }
});

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
