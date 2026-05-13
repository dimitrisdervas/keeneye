import re

with open("index.html", "r") as f:
    content = f.read()

def repl(m):
    category = m.group(1)
    img_tag = m.group(2)
    return f'<div class="port-item" data-category="{category}">\n      {img_tag}\n      <div class="port-overlay"><span>{category}</span></div>\n    </div>'

new_content = re.sub(r'<div class="port-item" data-category="([^"]+)">\s*(<img[^>]+>)\s*</div>', repl, content)

with open("index.html", "w") as f:
    f.write(new_content)
