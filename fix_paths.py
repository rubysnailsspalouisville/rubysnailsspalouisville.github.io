import re

# Fix paths for pages that are now one level deeper
# They need ../ prefixed to all local asset references

pages = {
    "about/index.html": "about.html",
    "services/index.html": "services.html",
    "gallery/index.html": "gallery.html",
}

for dest, src in pages.items():
    with open(f"/Users/thaophuong/Downloads/ruby nail spa /{src}", "r") as f:
        content = f.read()
    
    # Fix CSS link
    content = content.replace('href="styles.css"', 'href="../styles.css"')
    
    # Fix logo image
    content = content.replace('src="att.3M3OUhW3eHOqAw83b57mKpZw6g7XbE0eXKBNpCAUNx0.JPG"', 'src="../att.3M3OUhW3eHOqAw83b57mKpZw6g7XbE0eXKBNpCAUNx0.JPG"')
    
    # Fix award image (about page)
    content = content.replace('src="award.jpg"', 'src="../award.jpg"')
    
    # Fix service images
    content = content.replace('src="service/', 'src="../service/')
    
    # Fix gallery images  
    content = content.replace('src="gallery/', 'src="../gallery/')
    
    # Fix model/client images
    content = content.replace('src="model/', 'src="../model/')
    
    # Fix nav links - update to clean URLs
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="about.html"', 'href="/about"')
    content = content.replace('href="services.html"', 'href="/services"')
    content = content.replace('href="gallery.html"', 'href="/gallery"')
    
    # Fix view menu buttons and gallery button
    content = content.replace('href="services.html"', 'href="/services"')
    content = content.replace('href="gallery.html"', 'href="/gallery"')

    with open(f"/Users/thaophuong/Downloads/ruby nail spa /{dest}", "w") as f:
        f.write(content)
    print(f"Fixed: {dest}")

# Also fix index.html nav links
with open("/Users/thaophuong/Downloads/ruby nail spa /index.html", "r") as f:
    content = f.read()

content = content.replace('href="about.html"', 'href="/about"')
content = content.replace('href="services.html"', 'href="/services"')
content = content.replace('href="gallery.html"', 'href="/gallery"')
content = content.replace('href="services.html"', 'href="/services"')
content = content.replace('href="gallery.html"', 'href="/gallery"')

with open("/Users/thaophuong/Downloads/ruby nail spa /index.html", "w") as f:
    f.write(content)
print("Fixed: index.html")

print("All done!")
