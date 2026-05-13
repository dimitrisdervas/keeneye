import re
import os

images_dir = "/home/dervas/Apps/keeneye/photos/keeneye photos"

images = []
for root, _, files in os.walk(images_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            rel_dir = os.path.relpath(root, images_dir)
            if rel_dir == '.':
                cat = 'Αυτοκόλλητα' if 'banner' in file.lower() else 'Άλλα'
            else:
                cat = rel_dir
            
            src = f"./photos/keeneye photos/{rel_dir}/{file}".replace('././', './')
            images.append({
                'src': src.replace('"', '&quot;'),
                'cat': cat,
                'file': file
            })

# Map categories to JS friendly strings
cat_map = {
    'Επιγραφές': 'Επιγραφές',
    'Αυτοκόλλητα': 'Αυτοκόλλητα',
    '"Ντύσιμο" Οχημάτων': 'Ντύσιμο'
}

html_items = []
for img in images:
    c = cat_map.get(img['cat'], 'Άλλα')
    html_items.append(f'    <div class="port-item" data-category="{c}"><img src="{img["src"]}" alt="{c}"></div>')

grid_html = '\n'.join(html_items)

portfolio_html = f"""<!-- PORTFOLIO -->
<section class="portfolio" id="portfolio">
  <div class="sec-label">Δουλειές Μας</div>
  <div class="sec-title">Πρόσφατα Έργα</div>
  <div class="port-filters">
    <button class="p-filt active" data-filter="all">Όλα</button>
    <button class="p-filt" data-filter="Επιγραφές">Επιγραφές</button>
    <button class="p-filt" data-filter="Αυτοκόλλητα">Αυτοκόλλητα & Banner</button>
    <button class="p-filt" data-filter="Ντύσιμο">Ντύσιμο Οχημάτων</button>
  </div>
  <div class="port-grid" id="port-grid">
{grid_html}
  </div>
  <div class="port-load" id="port-load-container">
    <button id="load-more-btn">Δείτε περισσότερα</button>
  </div>
</section>"""

with open("/home/dervas/Apps/keeneye/index.html", "r") as f:
    content = f.read()

# Replace Portfolio section
content = re.sub(r'<!-- PORTFOLIO -->.*?</section>', portfolio_html, content, flags=re.DOTALL)

# Nav links replacement
content = content.replace(
    '<a href="services.html">Υπηρεσίες</a>\n  </div>\n  <button',
    '<a href="services.html">Υπηρεσίες</a>\n    <a href="portfolio.html">Πορτφόλιο</a>\n  </div>\n  <button'
)

content = content.replace(
    '<a href="services.html">Υπηρεσίες</a>\n</div>\n\n<!-- HERO',
    '<a href="services.html">Υπηρεσίες</a>\n  <a href="portfolio.html">Πορτφόλιο</a>\n</div>\n\n<!-- HERO'
)

# Footer links
content = content.replace(
    '<a href="services.html">Υπηρεσίες</a>\n    <a href="https://www.instagram.com/keeneye_adv/"',
    '<a href="services.html">Υπηρεσίες</a>\n    <a href="portfolio.html">Πορτφόλιο</a>\n    <a href="https://www.instagram.com/keeneye_adv/"'
)

# Hero Slideshow
hero_new = """<!-- HERO -->
<section class="hero" id="hero">
  <div class="hero-bg">
    <img src="./photos/keeneye photos/Επιγραφές/IMG_4474.JPG" class="hero-slide active">
    <img src="./photos/keeneye photos/Αυτοκόλλητα/Αυτοκόλλητα 4.jpg" class="hero-slide">
    <img src="./photos/keeneye photos/&quot;Ντύσιμο&quot; Οχημάτων/&quot;Ντύσιμο&quot; Οχημάτων 5.JPG" class="hero-slide">
  </div>
  <div class="h-left">"""
content = content.replace('<!-- HERO -->\n<section class="hero" id="hero">\n  <div class="h-left">', hero_new)

# Product grid
prod_old = """  <div class="prod-grid">
    <div class="prod-tile">
      <img src="./photos/keeneye photos/Επιγραφές/IMG_4474.JPG" alt="Επιγραφές" class="prod-tile-img">
      <span>Επιγραφές</span>
    </div>
    <div class="prod-tile">
      <img src="./photos/keeneye photos/Αυτοκόλλητα/Αυτοκόλλητα 4.jpg" alt="Αυτοκόλλητα" class="prod-tile-img">
      <span>Αυτοκόλλητα</span>
    </div>
    <div class="prod-tile">
      <img src="./photos/keeneye photos/Αυτοκόλλητα/IMG_4506.JPG" alt="Banner" class="prod-tile-img">
      <span>Banner</span>
    </div>
    <div class="prod-tile">
      <img src="./photos/keeneye photos/&quot;Ντύσιμο&quot; Οχημάτων/&quot;Ντύσιμο&quot; Οχημάτων 5.JPG" alt="Ντύσιμο Οχημάτων" class="prod-tile-img">
      <span>"Ντύσιμο" Οχημάτων</span>
    </div>
    <div class="prod-tile">
      <img src="./photos/keeneye photos/Επιγραφές/IMG_4490.JPG" alt="Διαφημιστικά Δώρα" class="prod-tile-img">
      <span>Διαφημιστικά Δώρα</span>
    </div>
    <div class="prod-tile">
      <img src="./photos/keeneye photos/Αυτοκόλλητα/IMG_4416.jpg" alt="Ρούχα Εργασίας" class="prod-tile-img">
      <span>Ρούχα Εργασίας</span>
    </div>
  </div>"""

prod_new = """  <div class="prod-grid">
    <div class="prod-tile">
      <div class="prod-img-wrap">
        <img src="./photos/keeneye photos/Επιγραφές/IMG_4474.JPG" alt="Επιγραφές" class="prod-tile-img">
        <div class="prod-overlay"><span>Επιγραφές</span></div>
      </div>
    </div>
    <div class="prod-tile">
      <div class="prod-img-wrap">
        <img src="./photos/keeneye photos/Αυτοκόλλητα/Αυτοκόλλητα 4.jpg" alt="Αυτοκόλλητα" class="prod-tile-img">
        <div class="prod-overlay"><span>Αυτοκόλλητα</span></div>
      </div>
    </div>
    <div class="prod-tile">
      <div class="prod-img-wrap">
        <img src="./photos/keeneye photos/Αυτοκόλλητα/IMG_4506.JPG" alt="Banner" class="prod-tile-img">
        <div class="prod-overlay"><span>Banner</span></div>
      </div>
    </div>
    <div class="prod-tile">
      <div class="prod-img-wrap">
        <img src="./photos/keeneye photos/&quot;Ντύσιμο&quot; Οχημάτων/&quot;Ντύσιμο&quot; Οχημάτων 5.JPG" alt="Ντύσιμο Οχημάτων" class="prod-tile-img">
        <div class="prod-overlay"><span>"Ντύσιμο" Οχημάτων</span></div>
      </div>
    </div>
    <div class="prod-tile">
      <div class="prod-img-wrap">
        <img src="./photos/keeneye photos/Επιγραφές/IMG_4490.JPG" alt="Διαφημιστικά Δώρα" class="prod-tile-img">
        <div class="prod-overlay"><span>Διαφημιστικά Δώρα</span></div>
      </div>
    </div>
    <div class="prod-tile">
      <div class="prod-img-wrap">
        <img src="./photos/keeneye photos/Αυτοκόλλητα/IMG_4416.jpg" alt="Ρούχα Εργασίας" class="prod-tile-img">
        <div class="prod-overlay"><span>Ρούχα Εργασίας</span></div>
      </div>
    </div>
  </div>"""
content = content.replace(prod_old, prod_new)

# About Videos
about_old = """<!-- ABOUT -->
<section class="about" id="about">
  <div class="sec-label">Ποιοι είμαστε</div>
  <h2>Τριάντα χρόνια παρουσίας στην αγορά.</h2>
  <p>Ξεκινήσαμε από την Αριδαία το 1995 με μια απλή πεποίθηση: η εικόνα μιας επιχείρησης αξίζει τον ίδιο σεβασμό με το προϊόν της. Σήμερα, από τη Θεσσαλονίκη, συνεχίζουμε να αναλαμβάνουμε κάθε έργο με την ίδια προσοχή — από μία απλή επιγραφή ως την πλήρη εικαστική ταυτότητα χώρου.</p>
</section>"""

about_new = """<!-- ABOUT -->
<section class="about" id="about">
  <div class="about-top">
    <div class="sec-label">Ποιοι είμαστε</div>
    <h2>Τριάντα χρόνια παρουσίας στην αγορά.</h2>
    <p>Ξεκινήσαμε από την Αριδαία το 1995 με μια απλή πεποίθηση: η εικόνα μιας επιχείρησης αξίζει τον ίδιο σεβασμό με το προϊόν της. Σήμερα, από τη Θεσσαλονίκη, συνεχίζουμε να αναλαμβάνουμε κάθε έργο με την ίδια προσοχή — από μία απλή επιγραφή ως την πλήρη εικαστική ταυτότητα χώρου.</p>
  </div>
  <div class="about-media">
    <video src="./photos/keeneye photos/banner.MOV" autoplay loop muted playsinline></video>
    <video src="./photos/keeneye photos/Αυτοκόλλητα.MOV" autoplay loop muted playsinline></video>
  </div>
</section>"""
content = content.replace(about_old, about_new)

# Append JS scripts and lightbox container
scripts = """
<!-- LIGHTBOX -->
<div class="lightbox" id="lightbox">
  <button class="lb-close" id="lb-close">&times;</button>
  <img src="" id="lb-img" alt="">
</div>

<script>
  // Mobile Nav
  document.getElementById('mob-menu').addEventListener('click', () => {
    document.getElementById('mob-nav').classList.toggle('open');
  });
  document.querySelectorAll('#mob-nav a').forEach(a => {
    a.addEventListener('click', () => document.getElementById('mob-nav').classList.remove('open'));
  });

  // Hero Slideshow
  const slides = document.querySelectorAll('.hero-slide');
  let currentSlide = 0;
  if(slides.length > 0){
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 4000);
  }

  // Portfolio Logic
  const portItems = Array.from(document.querySelectorAll('.port-item'));
  const filters = document.querySelectorAll('.p-filt');
  const loadBtn = document.getElementById('load-more-btn');
  let currentCategory = 'all';
  let itemsToShow = 8;

  function renderPortfolio() {
    let visibleCount = 0;
    portItems.forEach(item => {
      item.classList.remove('visible');
      const cat = item.getAttribute('data-category');
      if (currentCategory === 'all' || currentCategory === cat) {
        if (visibleCount < itemsToShow) {
          item.classList.add('visible');
        }
        visibleCount++;
      }
    });

    if (visibleCount <= itemsToShow) {
      document.getElementById('port-load-container').style.display = 'none';
    } else {
      document.getElementById('port-load-container').style.display = 'flex';
    }
  }

  filters.forEach(btn => {
    btn.addEventListener('click', () => {
      filters.forEach(f => f.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.getAttribute('data-filter');
      itemsToShow = 8; // reset
      renderPortfolio();
    });
  });

  if(loadBtn) {
    loadBtn.addEventListener('click', () => {
      itemsToShow += 8;
      renderPortfolio();
    });
  }

  renderPortfolio();

  // Lightbox Logic
  const lightbox = document.getElementById('lightbox');
  const lbImg = document.getElementById('lb-img');
  const lbClose = document.getElementById('lb-close');

  portItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      lbImg.src = img.src;
      lightbox.classList.add('active');
    });
  });

  lbClose.addEventListener('click', () => lightbox.classList.remove('active'));
  lightbox.addEventListener('click', (e) => {
    if(e.target === lightbox) lightbox.classList.remove('active');
  });
  document.addEventListener('keydown', (e) => {
    if(e.key === 'Escape') lightbox.classList.remove('active');
  });
</script>
</body>"""

content = re.sub(r'<script>.*?</script>\n</body>', scripts, content, flags=re.DOTALL)

with open("/home/dervas/Apps/keeneye/index.html", "w") as f:
    f.write(content)

