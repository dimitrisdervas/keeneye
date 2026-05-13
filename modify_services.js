const fs = require('fs');
let html = fs.readFileSync('services.html', 'utf8');

// Update Nav Links
html = html.replace(/href="#hero"/g, 'href="index.html#hero"');
html = html.replace(/href="#products"/g, 'href="index.html#products"');
html = html.replace(/href="#about"/g, 'href="index.html#about"');
html = html.replace(/href="#contact"/g, 'href="index.html#contact"');
html = html.replace(/href="services\.html"/g, 'href="#"'); // Mobile link
html = html.replace(/href="#services"/g, 'href="#"');     // Desktop link

// Remove Hero section
html = html.replace(/<!-- HERO -->[\s\S]*?<\/section>/, '');

// Remove Products section
html = html.replace(/<!-- PRODUCTS -->[\s\S]*?<\/section>/, '');

// Show Services on mobile
html = html.replace(/id="services" class="hidden md:block /, 'id="services" class="');

// Remove About section
html = html.replace(/<!-- ABOUT -->[\s\S]*?<\/section>/, '');

// Remove Contact section
html = html.replace(/<!-- CONTACT -->[\s\S]*?<\/section>/, '');

fs.writeFileSync('services.html', html);
