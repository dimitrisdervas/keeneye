import re

with open('/home/dervas/Apps/keeneye/index.html', 'r') as f:
    content = f.read()

# Change title
content = content.replace(
    '<title>Keen Eye Advertising | Επιγραφές, Ψηφιακές Εκτυπώσεις & Branding</title>',
    '<title>Πορτφόλιο | Keen Eye Advertising</title>'
)

# Remove sections: hero, divider, products, divider, services, about, contact
to_remove = [
    r'<!-- HERO -->.*?</section>',
    r'<!-- PRODUCTS -->.*?</section>',
    r'<!-- SERVICES \(desktop only\) -->.*?</section>',
    r'<!-- ABOUT -->.*?</section>',
    r'<!-- CONTACT -->.*?</section>',
    r'<div class="divider"></div>'
]

for pattern in to_remove:
    content = re.sub(pattern, '', content, flags=re.DOTALL)

# Adjust portfolio section padding and text for the dedicated page
content = content.replace(
    '<div class="sec-label">Δουλειές Μας</div>\n  <div class="sec-title">Πρόσφατα Έργα</div>',
    '<h1 class="sec-title" style="margin-top:60px;">Πορτφόλιο</h1>'
)

# Update the JS so all items load or maybe load more at 16
content = content.replace('let itemsToShow = 8;', 'let itemsToShow = 16;')
content = content.replace('itemsToShow = 8; // reset', 'itemsToShow = 16; // reset')
content = content.replace('itemsToShow += 8;', 'itemsToShow += 16;')

with open('/home/dervas/Apps/keeneye/portfolio.html', 'w') as f:
    f.write(content)

