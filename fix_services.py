with open('/home/dervas/Apps/keeneye/services.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<li><a href="index.html#hero" class="hover:text-brand-dark transition">Αρχική</a></li>\n      <li><a href="#" class="hover:text-brand-dark transition">Υπηρεσίες</a></li>\n    </ul>',
    '<li><a href="index.html#hero" class="hover:text-brand-dark transition">Αρχική</a></li>\n      <li><a href="#" class="hover:text-brand-dark transition">Υπηρεσίες</a></li>\n      <li><a href="portfolio.html" class="hover:text-brand-dark transition">Πορτφόλιο</a></li>\n    </ul>'
)

content = content.replace(
    '<li><a href="index.html#hero" class="hover:text-brand-dark transition">Αρχική</a></li>\n      <li><a href="#" class="hover:text-brand-dark transition">Υπηρεσίες</a></li>\n    </ul>',
    '<li><a href="index.html#hero" class="hover:text-brand-dark transition">Αρχική</a></li>\n      <li><a href="#" class="hover:text-brand-dark transition">Υπηρεσίες</a></li>\n      <li><a href="portfolio.html" class="hover:text-brand-dark transition">Πορτφόλιο</a></li>\n    </ul>'
)

content = content.replace(
    '<ul class="flex flex-col gap-5 text-sm tracking-widest uppercase text-brand-mid">\n      <li><a href="index.html#hero" class="hover:text-brand-dark">Αρχική</a></li>\n      <li><a href="#" class="hover:text-brand-dark">Υπηρεσίες</a></li>\n    </ul>',
    '<ul class="flex flex-col gap-5 text-sm tracking-widest uppercase text-brand-mid">\n      <li><a href="index.html#hero" class="hover:text-brand-dark">Αρχική</a></li>\n      <li><a href="#" class="hover:text-brand-dark">Υπηρεσίες</a></li>\n      <li><a href="portfolio.html" class="hover:text-brand-dark">Πορτφόλιο</a></li>\n    </ul>'
)

with open('/home/dervas/Apps/keeneye/services.html', 'w') as f:
    f.write(content)
