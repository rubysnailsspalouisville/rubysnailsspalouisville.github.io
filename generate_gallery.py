import os
import subprocess
from pathlib import Path

gallery_dir = Path("/Users/thaophuong/Downloads/ruby nail spa /gallery")

valid_extensions = {'.png', '.heic', '.jpeg', '.jpg'}
image_files = []

# Process files
for file in gallery_dir.iterdir():
    if file.is_file() and file.suffix.lower() in valid_extensions:
        # If it's a huge PNG or HEIC, we convert it to JPEG using sips
        # Or if it's already a JPEG but large, we compress it
        
        # Determine output file name
        out_name = file.stem + ".jpg"
        out_path = gallery_dir / out_name
        
        # If the file is not already a .jpg, or it's a huge .jpg, process it
        if file.suffix.lower() != '.jpg' or file.stat().st_size > 1000000:
            print(f"Optimizing {file.name} -> {out_name}")
            subprocess.run([
                "sips", "-s", "format", "jpeg", 
                "-s", "formatOptions", "40", 
                "-Z", "800", 
                str(file), "--out", str(out_path)
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # If we created a new file and the old one was different extension, remove old one
            if file.name != out_name:
                file.unlink()
        
        if out_name not in image_files:
            image_files.append(out_name)

# Make sure we don't duplicate names in the list
image_files = list(set(image_files))
image_files.sort()

# Generate HTML
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Gallery | Ruby Nail Spa</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="site-header">
        <!-- Top Contact Bar -->
        <div class="top-bar">
            <div class="container top-bar-inner">
                <div class="top-contact">
                    <a href="tel:5023330868" class="phone-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-phone"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        <span>(502) 333-0868</span>
                    </a>
                </div>
                <div class="top-cta">
                    <a href="#" class="btn btn-outline-gold">Best Nail Salon</a>
                </div>
            </div>
        </div>

        <!-- Main Navigation Header -->
        <div class="main-header">
            <div class="container header-inner">
                <div class="logo-area">
                    <a href="index.html" class="logo">
                        <img src="att.3M3OUhW3eHOqAw83b57mKpZw6g7XbE0eXKBNpCAUNx0.JPG" alt="Ruby Nail Spa Logo" class="logo-image">
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="main-nav">
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="#">About us</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="gallery.html" class="active">Gallery</a></li>
                    </ul>
                </nav>

                <!-- Book Now Button & Mobile Menu Toggle -->
                <div class="header-actions">
                    <a href="#" class="btn btn-gold">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-calendar"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        Book Now
                    </a>
                    
                    <button class="mobile-menu-toggle" aria-label="Toggle menu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <main>
        <section class="services-page-header" style="padding: 160px 40px 100px; text-align: center; background-color: var(--primary-black);">
            <div class="services-badge" style="display: inline-block; border: 1px solid rgba(197, 160, 89, 0.5); padding: 8px 20px; font-size: 11px; font-family: var(--font-body); color: var(--primary-gold); letter-spacing: 4px; text-transform: uppercase; margin-bottom: 24px;">PORTFOLIO</div>
            <h1 style="font-size: 56px; font-family: var(--font-heading); color: var(--primary-gold); font-weight: 400; font-style: italic; margin-bottom: 20px;">Our Work</h1>
            <p style="font-family: var(--font-heading); font-style: italic; font-size: 16px; color: var(--text-muted); max-width: 600px; margin: 0 auto;">Take a look at the beautiful nails and relaxing experiences we create every day at Ruby's Nails & Spa.</p>
        </section>
        
        <div class="full-gallery-wrapper">
            <div class="masonry-grid" id="masonryGrid">
"""

for img in image_files:
    html_content += f"""                <div class="masonry-item">
                    <img src="gallery/{img}" alt="Ruby Nail Spa Gallery Image" loading="lazy">
                    <div class="masonry-overlay"><span>View</span></div>
                </div>\n"""

html_content += """            </div>
        </div>
    </main>

    <!-- Lightbox Modal -->
    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightboxClose">&times;</button>
        <div class="lightbox-backdrop" id="lightboxBackdrop"></div>
        <img src="" alt="Enlarged gallery image" class="lightbox-img" id="lightboxImg">
    </div>

    <!-- Footer Section -->
    <footer class="site-footer">
        <div class="footer-container">
            <!-- Left Side: Google Map -->
            <div class="footer-map-container">
                <iframe 
                    src="https://www.google.com/maps?q=Ruby+Nail+Spa,+8268+Dixie+Hwy,+Louisville,+KY+40258&output=embed" 
                    width="100%" 
                    height="100%" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
            </div>

            <!-- Right Side: Contact Info -->
            <div class="footer-info-container">
                <div class="footer-header">
                    <span class="footer-label">FIND US</span>
                    <h2 class="footer-title">Visit <span class="gold-text">Ruby Nails</span></h2>
                    <p class="footer-desc">A professional beauty salon in Louisville, KY that aims to bring service of the highest quality to our clients, where they can prettify themselves and relax.</p>
                </div>

                <div class="footer-contact-cards">
                    <!-- Address Card -->
                    <div class="contact-card">
                        <div class="contact-icon">📍</div>
                        <div class="contact-details">
                            <span class="contact-label">ADDRESS</span>
                            <p class="contact-value">8268 Dixie Hwy<br>Louisville, KY 40258</p>
                        </div>
                    </div>

                    <!-- Phone Card -->
                    <div class="contact-card">
                        <div class="contact-icon">📞</div>
                        <div class="contact-details">
                            <span class="contact-label">PHONE</span>
                            <p class="contact-value"><a href="tel:5023330868" class="contact-link">(502) 333-0868</a></p>
                        </div>
                    </div>

                    <!-- Hours Card -->
                    <div class="contact-card">
                        <div class="contact-icon">🕒</div>
                        <div class="contact-details">
                            <span class="contact-label">BUSINESS HOURS</span>
                            <div class="hours-row">
                                <span>Monday - Saturday</span>
                                <span>10:00 am - 7:30 pm</span>
                            </div>
                            <div class="hours-row">
                                <span>Sunday</span>
                                <span>11:30 am - 5:30 pm</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Ruby's Nails & Spa. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Sticky Header Effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('.main-header');
            if (window.scrollY > 40) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        // Mobile Menu Toggle
        const menuToggle = document.querySelector('.mobile-menu-toggle');
        const mainNav = document.querySelector('.main-nav');
        
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            mainNav.classList.toggle('active');
        });

        // ---- Lightbox ----
        const lightbox     = document.getElementById('lightbox');
        const lightboxImg  = document.getElementById('lightboxImg');
        const lightboxClose   = document.getElementById('lightboxClose');
        const lightboxBackdrop = document.getElementById('lightboxBackdrop');

        // Open lightbox when any gallery item is clicked
        document.querySelectorAll('.masonry-item').forEach(item => {
            item.addEventListener('click', () => {
                const src = item.querySelector('img').src;
                lightboxImg.src = src;
                lightbox.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        // Close on X button or backdrop click
        function closeLightbox() {
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
            setTimeout(() => { lightboxImg.src = ''; }, 350);
        }

        lightboxClose.addEventListener('click', closeLightbox);
        lightboxBackdrop.addEventListener('click', closeLightbox);

        // Close on Escape key
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') closeLightbox();
        });
    </script>
</body>
</html>
"""

with open("/Users/thaophuong/Downloads/ruby nail spa /gallery.html", "w") as f:
    f.write(html_content)

print("Optimization complete and gallery.html generated.")
