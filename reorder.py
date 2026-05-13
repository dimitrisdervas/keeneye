import re

with open('/home/dervas/Apps/keeneye/index.html', 'r') as f:
    content = f.read()

# 1. Extract h-right from hero
h_right_pattern = r'(\s*<div class="h-right">.*?</div>\n  </div>\n</section>)'
h_right_match = re.search(r'(\s*<div class="h-right">.*?</div>\n  </div>\n</section>)', content, flags=re.DOTALL)
if h_right_match:
    # We will replace this block with just '</div>\n</section>'
    h_right_content = re.search(r'<div class="h-right">.*?(?=</div>\n  </div>\n</section>)</div>', h_right_match.group(1), flags=re.DOTALL).group(0)
    content = content.replace(h_right_match.group(1), '\n  </div>\n</section>')
else:
    print("Could not find h-right")
    exit(1)

# 2. Extract sections
hero_pattern = r'<!-- HERO -->.*?</section>'
portfolio_pattern = r'<!-- PORTFOLIO -->.*?</section>'
services_pattern = r'<!-- SERVICES \(desktop only\) -->.*?</section>'
about_pattern = r'<!-- ABOUT -->.*?</section>'
contact_pattern = r'<!-- CONTACT -->.*?</section>'

hero = re.search(hero_pattern, content, flags=re.DOTALL).group(0)
portfolio = re.search(portfolio_pattern, content, flags=re.DOTALL).group(0)
services = re.search(services_pattern, content, flags=re.DOTALL).group(0)
about = re.search(about_pattern, content, flags=re.DOTALL).group(0)
contact = re.search(contact_pattern, content, flags=re.DOTALL).group(0)

# Modify About section
about_top_match = re.search(r'<div class="about-top">(.*?)</div>', about, flags=re.DOTALL)
about_text = about_top_match.group(1)

new_about_top = f"""<div class="about-grid">
    <div class="about-text">
{about_text}
    </div>
    <div class="about-stats">
{h_right_content}
    </div>
  </div>"""

about = about.replace(about_top_match.group(0), new_about_top)

# We need to change the CSS for h-right since it's now inside about-stats, or just use custom CSS for about-grid.
css_to_add = """
    .about-grid{display:grid;grid-template-columns:1fr;gap:48px;margin-bottom:60px}
    @media(min-width:768px){.about-grid{grid-template-columns:1fr 1fr;gap:80px;align-items:center}}
    .about-text{text-align:left}
    .about-stats .h-right{padding-left:0;border-left:1px solid rgba(0,0,0,0.1);padding-left:40px}
"""

content = content.replace('/* CONTACT */', css_to_add + '\n    /* CONTACT */')

# Change about-top CSS to about-text
content = content.replace('.about-top{', '.about-top-old{') # Disable old
content = content.replace('.about-top h2', '.about-text h2')
content = content.replace('.about-top p', '.about-text p')

# Reorder the HTML
# Current layout in file is Hero, Portfolio, Services, About, Contact
# Remove them from content
content = re.sub(hero_pattern + r'\s*', '', content, flags=re.DOTALL)
content = re.sub(portfolio_pattern + r'\s*', '', content, flags=re.DOTALL)
content = re.sub(services_pattern + r'\s*', '', content, flags=re.DOTALL)
content = re.sub(about_pattern + r'\s*', '', content, flags=re.DOTALL)
content = re.sub(contact_pattern + r'\s*', '', content, flags=re.DOTALL)

# Insert in new order
new_order = f"""{hero}

<div class="divider"></div>

{about}

<div class="divider"></div>

{portfolio}

<div class="divider"></div>

{services}

{contact}
"""

# Insert before FOOTER
content = content.replace('<!-- FOOTER -->', new_order + '\n<!-- FOOTER -->')

with open('/home/dervas/Apps/keeneye/index.html', 'w') as f:
    f.write(content)
