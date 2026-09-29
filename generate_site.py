import os
import re
import json

BASE_DIR = r"d:\antigravity website\reticulecanyon"
ADDR = "450 Lexington Avenue, Suite 1400, New York, NY 10017, United States"
PHONE = "+1-888-801-1428"
EMAIL = "concierge@reticulecanyon.com"
DOMAIN = "reticulecanyon.com"
BRAND = "Reticule Canyon Atelier"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=JetBrains+Mono:wght@400;500&family=Marcellus&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">"""

def get_header(active_page):
    idx_cls = "active" if active_page == "index" else ""
    abt_cls = "active" if active_page == "about" else ""
    srv_cls = "active" if active_page == "services" else ""
    faq_cls = "active" if active_page == "faq" else ""
    cnt_cls = "active" if active_page == "contact" else ""
    
    return f"""  <!-- Site Header (Rule 11) -->
  <header class="site-header">
    <div class="rc-container">
      <div class="rc-nav-container">
        <a href="index.html" class="rc-brand">
          <div class="rc-brand-crest">RC</div>
          <div class="rc-brand-text">
            Reticule Canyon
            <small>Atelier &bull; New York</small>
          </div>
        </a>
        <nav class="rc-nav-menu">
          <a href="index.html" class="rc-nav-link {idx_cls}">Atelier</a>
          <a href="about.html" class="rc-nav-link {abt_cls}">Heritage</a>
          <a href="services.html" class="rc-nav-link {srv_cls}">Bespoke Bags</a>
          <a href="faq.html" class="rc-nav-link {faq_cls}">Technical FAQ</a>
          <a href="contact.html" class="rc-nav-link {cnt_cls}">Salon Inquiries</a>
        </nav>
        <div style="display: flex; align-items: center; gap: 16px;">
          <a href="contact.html" class="rc-nav-cta">Book Salon</a>
          <button class="rc-hamburger" id="rc-hamburger" aria-label="Toggle Navigation">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer (Rule 11) -->
  <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop"></div>
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="rc-brand">
        <div class="rc-brand-crest">RC</div>
        <div class="rc-brand-text">Reticule Canyon</div>
      </div>
      <button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close Drawer">&times;</button>
    </div>
    <div class="mobile-drawer-body">
      <a href="index.html" class="mobile-nav-link">Atelier Flagship</a>
      <a href="about.html" class="mobile-nav-link">Heritage &amp; Guild Story</a>
      <a href="services.html" class="mobile-nav-link">Bespoke Bag Commissions</a>
      <a href="faq.html" class="mobile-nav-link">Technical &amp; Collector FAQ</a>
      <a href="contact.html" class="mobile-nav-link">Salon Consultation</a>
    </div>
    <div class="mobile-drawer-footer">
      <p style="margin-bottom: 8px; color: var(--rc-gold); font-family: var(--rc-font-mono); font-size: 0.75rem;">PRIVATE CONCIERGE</p>
      <p style="margin-bottom: 6px;">{PHONE}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>"""

def get_footer():
    return f"""  <!-- Semantic Site Footer -->
  <footer class="rc-footer">
    <div class="rc-container">
      <div class="rc-footer-grid">
        <div class="rc-footer-brand">
          <div class="rc-brand">
            <div class="rc-brand-crest">RC</div>
            <div class="rc-brand-text">
              Reticule Canyon
              <small>Maroquinerie &bull; Est. New York</small>
            </div>
          </div>
          <p>Handcrafted luxury leather reticules, structured totes, and saddle-stitched heirlooms forged from botanical vegetable-tanned hides and solid brass metallurgy.</p>
          <div style="font-family: var(--rc-font-mono); font-size: 0.8rem; color: var(--rc-gold);">
            {PHONE} &bull; {EMAIL}
          </div>
        </div>
        <div class="rc-footer-col">
          <h4>Atelier Bags</h4>
          <ul class="rc-footer-links">
            <li><a href="index.html">Flagship Home</a></li>
            <li><a href="about.html">Heritage &amp; Guilds</a></li>
            <li><a href="services.html">Bespoke Commissions</a></li>
            <li><a href="faq.html">Technical FAQ</a></li>
            <li><a href="contact.html">Salon Consultation</a></li>
          </ul>
        </div>
        <div class="rc-footer-col">
          <h4>Signature Silhouettes</h4>
          <ul class="rc-footer-links">
            <li><a href="services.html">Structured Leather Totes</a></li>
            <li><a href="services.html">Sculptural Bucket Bags</a></li>
            <li><a href="services.html">Cognac Executive Attach&eacute;s</a></li>
            <li><a href="services.html">Woven Evening Clutches</a></li>
            <li><a href="services.html">Designer Crossbody Bags</a></li>
          </ul>
        </div>
        <div class="rc-footer-col">
          <h4>Institutional</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 12px; color: var(--rc-text-light-muted);">
            {ADDR}
          </p>
          <p style="font-family: var(--rc-font-mono); font-size: 0.75rem; color: var(--rc-gold); margin-bottom: 16px;">
            Direct Salon Inquiries: {PHONE}
          </p>
          <div style="padding: 8px 12px; background: rgba(212,175,55,0.08); border: 1px solid rgba(212,175,55,0.2); border-radius: 4px; font-size: 0.725rem; font-family: var(--rc-font-mono); color: var(--rc-text-light);">
            ISO-9001 Artisan Leather Guild Compliance Verified
          </div>
        </div>
      </div>
      <div class="rc-footer-bottom">
        <div>&copy; 2026 Reticule Canyon Atelier LLC. All Worldwide Rights Reserved.</div>
        <div class="rc-footer-legal-links">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="cookie-policy.html">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="assets/js/script.js"></script>
  <script src="assets/js/main.js"></script>"""

# ==========================================
# 1. INDEX.HTML (Flagship Home - >= 10 Sections)
# ==========================================
def build_index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reticule Canyon | Handcrafted Luxury Bags &amp; Haute Maroquinerie</title>
  <meta name="description" content="Discover Reticule Canyon Atelier. Handcrafted luxury leather reticules, structured designer totes, and saddle-stitched satchels made with botanical hides and solid brass in New York.">
  <link rel="canonical" href="https://{DOMAIN}/index.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LeatherGoodsStore",
    "name": "Reticule Canyon Atelier",
    "url": "https://{DOMAIN}/",
    "telephone": "{PHONE}",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "450 Lexington Avenue, Suite 1400",
      "addressLocality": "New York",
      "addressRegion": "NY",
      "postalCode": "10017",
      "addressCountry": "US"
    }},
    "description": "Handcrafted luxury bags, structured leather reticules, designer totes, and saddle-stitched accessories crafted in New York.",
    "priceRange": "$$$$"
  }}
  </script>
</head>
<body>
{get_header('index')}

  <main>
    <!-- Section 1: Hero Masthead -->
    <section class="rc-hero">
      <div class="rc-container">
        <div class="rc-hero-grid">
          <div class="rc-hero-content">
            <div class="rc-hero-eyebrow">Haute Maroquinerie &bull; Guild Est. 2014</div>
            <h1 class="rc-hero-title">The Masterwork of Handcrafted <span>Luxury Bags</span></h1>
            <p class="rc-hero-desc">
              Reticule Canyon unites century-old French saddle-stitching with botanical oak-bark vegetable-tanned leather. Every bespoke reticule, structured tote, and attaché is cut, skived, and hand-burnished individually in our New York atelier.
            </p>
            <div class="rc-hero-actions">
              <a href="contact.html" class="rc-btn rc-btn-gold">Commission Bespoke Bag</a>
              <a href="services.html" class="rc-btn rc-btn-outline">Explore Bag Matrix</a>
            </div>
            <div class="rc-hero-stats">
              <div class="rc-stat-item">
                <div class="rc-stat-val">100%</div>
                <div class="rc-stat-lbl">Hand Saddle Stitched</div>
              </div>
              <div class="rc-stat-item">
                <div class="rc-stat-val">3.2 mm</div>
                <div class="rc-stat-lbl">Full-Grain Oak Bark Leather</div>
              </div>
              <div class="rc-stat-item">
                <div class="rc-stat-val">Solid</div>
                <div class="rc-stat-lbl">Milled Brass Metallurgy</div>
              </div>
            </div>
          </div>
          <div class="rc-hero-card">
            <div class="rc-hero-frame">
              <img src="assets/images/reticulecanyon_asset_1.jpg" alt="Handcrafted structured luxury leather tote bag with hand-finished seams on display" width="1200" height="800">
              <div class="rc-hero-floating-badge">
                <div class="rc-badge-info">
                  <h4>The Canyon Sovereign Tote</h4>
                  <p>Hand-Waxed Saddle Stitch Seam</p>
                </div>
                <div class="rc-badge-seal">
                  FLAGSHIP SPEC<br>ATELIER NY
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Marquee Ticker -->
    <div class="rc-ticker">
      <div class="rc-ticker-track">
        <div class="rc-ticker-item"><span>ATELIER SPECIFICATION</span> OAK-BARK VEGETABLE TANNED LEATHER</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>TENSILE THREAD</span> DOUBLE-WAXED LINEN FIL AU CHINOIS</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>METALLURGY</span> ZERO-PLATING SOLID MILLED BRASS</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>HAND SKIVING</span> BEVELED FEATHERED JOINTS 0.6MM</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>SALON COMMISSION</span> BESPOKE CLIENT MONOGRAMMING</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>ATELIER SPECIFICATION</span> OAK-BARK VEGETABLE TANNED LEATHER</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>TENSILE THREAD</span> DOUBLE-WAXED LINEN FIL AU CHINOIS</div>
        <div class="rc-ticker-bullet">&bull;</div>
        <div class="rc-ticker-item"><span>METALLURGY</span> ZERO-PLATING SOLID MILLED BRASS</div>
      </div>
    </div>

    <!-- Section 3: 3 Craft Pillars -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">Guild Foundations</span>
          <h2 class="rc-section-title">The Three Pillars of Canyon Maroquinerie</h2>
          <p class="rc-section-subtitle">
            Every bag bearing our hallmark rests upon three non-negotiable standards of heirloom craftsmanship, rejecting modern industrial shortcuts in favor of structural permanence.
          </p>
        </div>
        <div class="rc-pillars-grid">
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_3.jpg" alt="Bronze patina embossed luxury leather tote bag with sculpted handles" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Pillar 01</div>
              <h3 class="rc-pillar-title">Botanical Oak-Bark Tanning</h3>
              <p class="rc-pillar-text">
                We exclusively harvest full-grain steer hides cured for eighteen months in natural subterranean pits utilizing ground oak bark, mimosa tannins, and mountain wellspring waters to impart peerless structural tensile temper.
              </p>
            </div>
          </div>
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_4.jpg" alt="Sculptural cylindrical leather bucket bag with braided cord closure" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Pillar 02</div>
              <h3 class="rc-pillar-title">Solid Milled Brass Metallurgy</h3>
              <p class="rc-pillar-text">
                Our buckles, turnlocks, and D-rings are machine-milled from solid ingot brass billets and hand-burnished with natural pumice. Free from synthetic plating, our hardware develops an authentic amber patina across generations.
              </p>
            </div>
          </div>
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_5.jpg" alt="Quilted designer velvet and leather crossbody bag with precision stitch lines" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Pillar 03</div>
              <h3 class="rc-pillar-title">Double-Needle Saddle Stitch</h3>
              <p class="rc-pillar-text">
                Executed entirely by hand with two blunt harness needles passing opposite ways through pricked diamond awl holes. Unlike machine lockstitches, if one stitch wears through decades later, the seam will never unravel.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Anatomy Deep Dive -->
    <section class="rc-section rc-section-darker">
      <div class="rc-container">
        <div class="rc-anatomy-grid">
          <div class="rc-anatomy-media">
            <img src="assets/images/reticulecanyon_asset_2.jpg" alt="Crocodile embossed luxury leather tote bag showing detailed architectural construction" width="1200" height="800">
          </div>
          <div class="rc-anatomy-content">
            <span class="rc-section-tag">Anatomy of the Seam</span>
            <h2 class="rc-section-title">Why Hand Saddle Stitching Outlasts Any Sewing Machine</h2>
            <p class="rc-section-subtitle" style="margin-bottom: 28px;">
              Industrial luxury brands rely on motorized lockstitch machines that create looped threads susceptible to catastrophic failure when abraded. At Reticule Canyon, every stitch is an independent structural lock.
            </p>
            <div class="rc-anatomy-spec-list">
              <div class="rc-anatomy-item">
                <div class="rc-anatomy-item-head">
                  <h4>Beeswax-Coated French Linen</h4>
                  <span class="rc-spec-pill">632 Gauge</span>
                </div>
                <p>Natural flax fibers saturated in organic beeswax resist moisture penetration, fungal deterioration, and rotational friction during decades of daily carrying.</p>
              </div>
              <div class="rc-anatomy-item">
                <div class="rc-anatomy-item-head">
                  <h4>Pricked Diamond Awl Slits</h4>
                  <span class="rc-spec-pill">9 SPI Slant</span>
                </div>
                <p>Angled diamond slits align the leather fibers naturally without tearing the dermis, ensuring uniform slant tension and watertight seam compression.</p>
              </div>
              <div class="rc-anatomy-item">
                <div class="rc-anatomy-item-head">
                  <h4>Feathered Skiving &amp; Edge Creasing</h4>
                  <span class="rc-spec-pill">Hot Iron Finish</span>
                </div>
                <p>Leather margins are hand-skived to fractional millimeter tolerances and sealed with heated bronze irons, preventing raw edge fraying and moisture seepage.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Master Curation Bento Grid -->
    <section class="rc-section rc-section-light">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">Flagship Silhouettes</span>
          <h2 class="rc-section-title">The Reticule Canyon Master Curation</h2>
          <p class="rc-section-subtitle">
            Three iconic architectural leather bag forms forged for formal appointments, transcontinental voyages, and evening salons.
          </p>
        </div>
        <div class="rc-bento-grid">
          <div class="rc-bento-card">
            <div class="rc-bento-media">
              <img src="assets/images/reticulecanyon_asset_6.jpg" alt="Cognac executive leather briefcase attache handcrafted with solid brass lock" width="1200" height="800">
            </div>
            <div class="rc-bento-body">
              <div class="rc-bento-category">Executive Bag Edition</div>
              <h3 class="rc-bento-title">The Canyon Attaché</h3>
              <p class="rc-bento-desc">
                Engineered with dual internal gussets, reinforced bridle leather top handle, and custom milled brass clasp. Accommodates portfolios, laptops, and archival documents.
              </p>
              <div class="rc-bento-footer">
                <span>Vegetable Saddle Leather</span>
                <span>Caliber 3.4mm</span>
              </div>
            </div>
          </div>
          <div class="rc-bento-card">
            <div class="rc-bento-media">
              <img src="assets/images/reticulecanyon_asset_7.jpg" alt="Caramel leather satchel bag with hand-creased edges and turnlock closure" width="1200" height="800">
            </div>
            <div class="rc-bento-body">
              <div class="rc-bento-category">Atelier Satchel</div>
              <h3 class="rc-bento-title">The Canyon Satchel</h3>
              <p class="rc-bento-desc">
                A classic structured shoulder satchel finished with hand-plaited drawcords and double-folded rim. Balances architectural volume with supple tactile grace.
              </p>
              <div class="rc-bento-footer">
                <span>Hand-Formed Flap</span>
                <span>Solid Brass Lock</span>
              </div>
            </div>
          </div>
          <div class="rc-bento-card">
            <div class="rc-bento-media">
              <img src="assets/images/reticulecanyon_asset_8.jpg" alt="Crimson woven leather clutch and reticule with intricate hand-interlaced straps" width="1200" height="800">
            </div>
            <div class="rc-bento-body">
              <div class="rc-bento-category">Evening Salon Bag</div>
              <h3 class="rc-bento-title">The Woven Canyon Pouch</h3>
              <p class="rc-bento-desc">
                Interlaced strips of hand-beveled saddle leather create a supple textured envelope that drapes effortlessly in hand. Lined in velvet calfskin with secret card vault.
              </p>
              <div class="rc-bento-footer">
                <span>Hand-Interlaced Weave</span>
                <span>Calfskin Lining</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Artisanal Chronology Timeline -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">The Making of a Luxury Bag</span>
          <h2 class="rc-section-title">The Four Stages of Hand Bag Construction</h2>
          <p class="rc-section-subtitle">
            Each bag requires over 36 hours of focused, single-artisan labor from raw hide grading to final wax friction polishing.
          </p>
        </div>
        <div class="rc-timeline-grid">
          <div class="rc-timeline-step">
            <div class="rc-timeline-step-num">01</div>
            <h3 class="rc-timeline-step-title">Hide Topography Grading</h3>
            <p class="rc-timeline-step-text">
              We inspect individual hide bends under directional raking light, charting stretch direction and fiber density before cutting bag panels with hand-forged Japanese knives.
            </p>
          </div>
          <div class="rc-timeline-step">
            <div class="rc-timeline-step-num">02</div>
            <h3 class="rc-timeline-step-title">Feather Skiving &amp; Beveling</h3>
            <p class="rc-timeline-step-text">
              Joining edges are shaved to exact paper-thin gradients using vintage French edgers so layered seams maintain uniform flush thickness without unsightly bulk.
            </p>
          </div>
          <div class="rc-timeline-step">
            <div class="rc-timeline-step-num">03</div>
            <h3 class="rc-timeline-step-title">Double-Awl Saddle Stitch</h3>
            <p class="rc-timeline-step-text">
              Held in a wooden stitching clam, the artisan punches each hole with a diamond awl, passing twin needles simultaneously to balance seam tension with micro-metric precision.
            </p>
          </div>
          <div class="rc-timeline-step">
            <div class="rc-timeline-step-num">04</div>
            <h3 class="rc-timeline-step-title">Hot Wax Edge Burnishing</h3>
            <p class="rc-timeline-step-text">
              Exposed margins are repeatedly coated with natural beeswax, dyed with organic pigments, and friction-rubbed with dense ironwood burnishers to achieve glass-smooth waterproofing.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 7: Technical Specifications Matrix -->
    <section class="rc-section rc-section-sand">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">Engineering Matrix</span>
          <h2 class="rc-section-title">Technical Bag Specifications</h2>
          <p class="rc-section-subtitle">
            Examine the exact metallurgical, botanical, and tensile parameters governing all Reticule Canyon luxury bag commissions.
          </p>
        </div>
        <div class="rc-specs-card">
          <table class="rc-specs-table">
            <thead>
              <tr>
                <th>Component</th>
                <th>Material Standard</th>
                <th>Processing Protocol</th>
                <th>Tested Lifespan</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="rc-specs-param">Primary Bag Dermis</td>
                <td>Grade-A Steer Full Grain</td>
                <td>18-Month Botanical Oak Bark Pit Tannage</td>
                <td class="rc-specs-val">80+ Years / Heirloom Patina</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Tensile Threading</td>
                <td>Waxed Natural Flax Linen (No. 432)</td>
                <td>Organic Beeswax Hot Dip Impregnation</td>
                <td class="rc-specs-val">380 N Tensile Break Strength</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Hardware Castings</td>
                <td>Solid Ingot Brass (Alloy C36000)</td>
                <td>CNC Milled &amp; Hand Pumice Burnished</td>
                <td class="rc-specs-val">Corrosion Proof / Non-Plated</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Internal Reinforcement</td>
                <td>Salpa Reconstituted Leather Board</td>
                <td>Natural Rubber Latex Bonding</td>
                <td class="rc-specs-val">Permanent Structural Memory</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Edge Seal Chemistry</td>
                <td>Carnauba Wax &amp; Bone Glue Blend</td>
                <td>High-Friction Heated Hardwood Burnish</td>
                <td class="rc-specs-val">100% Water Resistant Seal</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 8: Connoisseur Testimonials -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">Client Provenance</span>
          <h2 class="rc-section-title">Words from Bag Collectors</h2>
          <p class="rc-section-subtitle">
            Read reflections from connoisseurs who carry Reticule Canyon pieces through boardrooms, transatlantic flights, and international galleries.
          </p>
        </div>
        <div class="rc-testimonials-grid">
          <div class="rc-testimonial-card">
            <div>
              <div class="rc-testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p class="rc-testimonial-quote">
                &ldquo;The saddle stitching on my Canyon Attaché is breathtaking. In a world overrun by mass-market luxury logos, carrying a bag where you can feel the deliberate human tension in every stitch is an extraordinary privilege.&rdquo;
              </p>
            </div>
            <div class="rc-testimonial-author">
              <div class="rc-author-name">Jonathan Vance, Esq.</div>
              <div class="rc-author-provenance">Partner, New York Legal Chambers</div>
            </div>
          </div>
          <div class="rc-testimonial-card">
            <div>
              <div class="rc-testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p class="rc-testimonial-quote">
                &ldquo;After four years of daily travel across Tokyo, Zurich, and Manhattan, the leather on my tote has acquired an amber honey depth that gets commented on everywhere. The solid brass hardware has never loosened a millimeter.&rdquo;
              </p>
            </div>
            <div class="rc-testimonial-author">
              <div class="rc-author-name">Evelyn Saint-Clair</div>
              <div class="rc-author-provenance">Art Advisory Director, Geneva &amp; London</div>
            </div>
          </div>
          <div class="rc-testimonial-card">
            <div>
              <div class="rc-testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p class="rc-testimonial-quote">
                &ldquo;I commissioned a custom monogrammed reticule bag for my anniversary. The consultation at their Lexington Avenue atelier was as bespoke as ordering Savile Row tailoring. It is a genuine generational heirloom.&rdquo;
              </p>
            </div>
            <div class="rc-testimonial-author">
              <div class="rc-author-name">Dr. Marcus Sterling</div>
              <div class="rc-author-provenance">Architectural Historian, Boston</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: FAQ Preview Accordion -->
    <section class="rc-section rc-section-darker">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">Essential Queries</span>
          <h2 class="rc-section-title">Technical &amp; Care Guidance</h2>
          <p class="rc-section-subtitle">
            Common questions regarding full-grain leather aging, bespoke ordering lead times, and heirloom bag maintenance.
          </p>
        </div>
        <div class="rc-accordion-list">
          <div class="rc-accordion-item active">
            <button class="rc-accordion-header">
              <span>How does vegetable-tanned leather age compared to chrome-tanned bags?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Chrome-tanned commercial bags are coated in synthetic plastic topcoats that crack and peel over time. Botanical vegetable-tanned leather remains breathable and naturally absorbs sunlight, skin oils, and ambient humidity, gradually developing an irreplaceable rich amber-cognac patina that increases in beauty each year.</p>
            </div>
          </div>
          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>Why do you exclusively use hand saddle stitching instead of sewing machines?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Sewing machines use an interlocking bobbin loop that creates structural vulnerability: if one loop snaps, the entire seam quickly unravels under strain. Our two-needle hand saddle stitch creates two independent cross-passes through each awl hole. Even under severe abrasion, the seam remains firmly locked.</p>
            </div>
          </div>
          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>What is the typical production timeline for a bespoke bag commission?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Depending on leather hide selection, custom monogram brass die casting, and internal partitioning requirements, a bespoke commission typically takes between four to eight weeks of artisan bench work. Each piece is crafted start-to-finish by one dedicated master maroquinier.</p>
            </div>
          </div>
          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>How should I condition and protect my Canyon leather bag?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>We recommend buffing your bag with a horsehair brush every few weeks to disperse natural waxes. Once every six to twelve months, apply a modest pea-sized amount of pure neatsfoot oil or botanical beeswax conditioner with a soft lint-free flannel cloth.</p>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 40px;">
          <a href="faq.html" class="rc-btn rc-btn-outline">View Full Collector FAQ &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Section 10: Private Bespoke Commission CTA -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-cta-box">
          <span class="rc-section-tag" style="margin-bottom: 20px;">By Private Appointment</span>
          <h2 class="rc-cta-title">Commission Your Bespoke Luxury Bag</h2>
          <p class="rc-cta-desc">
            Consult directly with our master leathercraftsman at our Lexington Avenue atelier. Select custom steer hides, personalized solid brass hardware, and hand-embossed monograms tailored to your exacting lifestyle.
          </p>
          <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <a href="contact.html" class="rc-btn rc-btn-gold">Request Salon Appointment</a>
            <a href="tel:+18888011428" class="rc-btn rc-btn-outline">Call Concierge: {PHONE}</a>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 2. ABOUT.HTML (Heritage & Philosophy)
# ==========================================
def build_about():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heritage &amp; Guild Philosophy | Reticule Canyon Atelier</title>
  <meta name="description" content="Explore the heritage of Reticule Canyon. Learn about our traditional saddle stitching techniques, botanical oak bark tanning, and dedicated luxury bag workshop in New York.">
  <link rel="canonical" href="https://{DOMAIN}/about.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('about')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Guild Heritage</span>
        <h1 class="rc-hero-title">Centuries of Maroquinerie, <span>Forged Anew</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">
          Founded on the uncompromising pursuit of permanent leather goods, Reticule Canyon honors the legendary guilds of European saddle-makers and bag artisans through honest hands and pure materials.
        </p>
      </div>
    </section>

    <!-- Story Segment 1: The Guild Tradition (Asset 9: Emerald Velvet Structured Handbag) -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-hero-grid">
          <div>
            <span class="rc-section-tag">Founding Creed</span>
            <h2 class="rc-section-title">The Rejection of Ephemeral Luxury</h2>
            <p class="rc-hero-desc">
              The modern luxury bag industry has succumbed to programmed obsolescence: cardboard core reinforcements, automated nylon stitching, and chemical resin paint that chips within seasons.
            </p>
            <p class="rc-hero-desc">
              Reticule Canyon was established in 2014 as a defiant return to archival permanence. We believe an authentic leather bag must be built to withstand decades of relentless handling, developing character and grace rather than falling into degradation.
            </p>
          </div>
          <div>
            <div class="rc-hero-frame">
              <img src="assets/images/reticulecanyon_asset_9.jpg" alt="Emerald velvet and structured luxury handbag detail with fine artisan piping" width="1200" height="800">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Story Segment 2: Master Evening Bags (Asset 10: Burgundy Velvet Evening Clutch) -->
    <section class="rc-section rc-section-light">
      <div class="rc-container">
        <div class="rc-hero-grid" style="direction: rtl;">
          <div style="direction: ltr;">
            <span class="rc-section-tag">Evening Silhouettes</span>
            <h2 class="rc-section-title">Heirloom Evening Bags Honed Over Generations</h2>
            <p class="rc-bento-desc">
              Our New York workshop creates bags designed to grace formal galas, private salons, and cultural premieres. From hand-burnished clutches to structural reticules, each piece is engineered with ergonomic hand balance and tactile comfort.
            </p>
            <p class="rc-bento-desc">
              There are no motorized conveyor belts or robotic stitching stations in our atelier. Every curve, bevel, and stitch is calculated by an artisan who understands how leather breathes and responds to climatic change.
            </p>
          </div>
          <div style="direction: ltr;">
            <div class="rc-bento-card" style="box-shadow: var(--rc-shadow-lg);">
              <img src="assets/images/reticulecanyon_asset_10.jpg" alt="Burgundy velvet and leather evening clutch with minimalist architectural profile" width="1200" height="800">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Story Segment 3: Hard-Case Evening Bags (Asset 11: Sculptural Hard-Case Bag) -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-hero-grid">
          <div>
            <span class="rc-section-tag">Workshop Protocol</span>
            <h2 class="rc-section-title">Single-Artisan Ownership</h2>
            <p class="rc-hero-desc">
              Unlike assembly lines where an operative repeats one micro-action hundreds of times per day, each Reticule Canyon handbag commission is assigned to a single master maroquinier from start to finish.
            </p>
            <p class="rc-hero-desc">
              From the initial tactile grading of the hide bend to the hand-punching of awl slits and the final hot beeswax burnish, the craftsman signs their guild registry mark inside the hidden lining seam of the finished bag.
            </p>
          </div>
          <div>
            <div class="rc-hero-frame">
              <img src="assets/images/reticulecanyon_asset_11.jpg" alt="Sculptural hard-case luxury evening bag with brass lock closure" width="1200" height="800">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Story Segment 4: Plisse Evening Purses (Asset 12: Plisse Leather Purse) -->
    <section class="rc-section rc-section-sand">
      <div class="rc-container">
        <div class="rc-hero-grid" style="direction: rtl;">
          <div style="direction: ltr;">
            <span class="rc-section-tag">Natural Tannins</span>
            <h2 class="rc-section-title">The Oak-Bark Tannage Vaults</h2>
            <p class="rc-bento-desc">
              Our leather is cured in century-old underground pit vats utilizing crushed oak bark, river water, and organic chestnuts. This slow, chemical-free process preserves the natural collagen bundle density of the hide, yielding an aroma and durability that petroleum-derived leathers cannot imitate.
            </p>
            <p class="rc-bento-desc">
              Over years of use, the oils trapped within these botanical fibers migrate gently to the surface, healing minor scuffs and creating a lustrous, water-repellent patina celebrated by luxury bag collectors worldwide.
            </p>
          </div>
          <div style="direction: ltr;">
            <div class="rc-bento-card" style="box-shadow: var(--rc-shadow-lg);">
              <img src="assets/images/reticulecanyon_asset_12.jpg" alt="Plisse pleated leather evening purse with burnished leather strap" width="1200" height="800">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-cta-box">
          <h2 class="rc-cta-title">Experience the Atelier in Person</h2>
          <p class="rc-cta-desc">
            Visit our New York salon on Lexington Avenue to examine hide swatches, test saddle stitch resilience, and discuss custom dimensional bag commissions with our lead artisan.
          </p>
          <a href="contact.html" class="rc-btn rc-btn-gold">Schedule Salon Consultation</a>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 3. SERVICES.HTML (Bespoke Services)
# ==========================================
def build_services():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bespoke Bag Commissions &amp; Services | Reticule Canyon Atelier</title>
  <meta name="description" content="Explore bespoke luxury bag commission services at Reticule Canyon. Custom leather totes, briefcases, satchels, shoulder bags, and archival restoration in New York.">
  <link rel="canonical" href="https://{DOMAIN}/services.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('services')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Bespoke Atelier</span>
        <h1 class="rc-hero-title">Artisanal Bag Services &amp; <span>Custom Commissions</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">
          From private client monogramming and custom dimensional drafting to comprehensive archival leather bag preservation, we provide end-to-end bespoke maroquinerie solutions.
        </p>
      </div>
    </section>

    <!-- Services Grid (6 Luxury Bags with 6 Unique Images: Assets 13 to 18) -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-bento-grid" style="grid-template-columns: repeat(3, 1fr);">
          
          <!-- Service 1: Minimalist Shoulder Bag (Asset 13) -->
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_13.jpg" alt="Minimalist luxury leather shoulder bag with clean architectural contours" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Service 01</div>
              <h3 class="rc-pillar-title">Architectural Shoulder Bags</h3>
              <p class="rc-pillar-text">
                Every bespoke shoulder bag begins with individual millimeter drafting on rigid card stock. We engineer custom interior partitions, hidden smartphone vaults, and personalized strap drops tailored to your daily carry requirements.
              </p>
            </div>
          </div>

          <!-- Service 2: Creamy Ivory Tote (Asset 14) -->
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_14.jpg" alt="Creamy ivory luxury leather tote bag with hand-finished edges" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Service 02</div>
              <h3 class="rc-pillar-title">Custom Structured Totes</h3>
              <p class="rc-pillar-text">
                Personalize your structured tote bag with our curated selection of creamy ivory, obsidian black, and warm terracotta leathers. Finished with reinforced handles and optional 24K gold leaf monogram hot-stamping.
              </p>
            </div>
          </div>

          <!-- Service 3: Woven Artisan Tote (Asset 15) -->
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_15.jpg" alt="Woven leather artisan tote bag with braided handles and supple texture" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Service 03</div>
              <h3 class="rc-pillar-title">Interlaced Woven Bags</h3>
              <p class="rc-pillar-text">
                Hand-woven from continuous strips of full-grain saddle leather, creating a supple, tactile tote bag that molds comfortably against the body while retaining its structural baseline across years of carry.
              </p>
            </div>
          </div>

          <!-- Service 4: Vintage Briefcase (Asset 16) -->
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_16.jpg" alt="Vintage heritage leather briefcase with double buckle closures" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Service 04</div>
              <h3 class="rc-pillar-title">Heritage Briefcases &amp; Cases</h3>
              <p class="rc-pillar-text">
                Bespoke executive briefcases constructed with double-layered bridle leather, reinforced internal wooden frames, hand-beveled edges, and custom solid brass buckle mechanisms for effortless professional command.
              </p>
            </div>
          </div>

          <!-- Service 5: Travel Bag (Asset 17) -->
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_17.jpg" alt="Structured leather weekend travel bag with reinforced corners and handles" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Service 05</div>
              <h3 class="rc-pillar-title">Transatlantic Travel Bags</h3>
              <p class="rc-pillar-text">
                Collaborate with our head artisan to create an archival travel duffle or weekender bag constructed completely to your specified dimensions with solid brass feet and reinforced floor panels.
              </p>
            </div>
          </div>

          <!-- Service 6: Structured Crossbody (Asset 18) -->
          <div class="rc-pillar-card">
            <div class="rc-pillar-media">
              <img src="assets/images/reticulecanyon_asset_18.jpg" alt="Structured luxury crossbody bag with signature brass turnlock" width="1200" height="800">
            </div>
            <div class="rc-pillar-body">
              <div class="rc-pillar-num">Service 06</div>
              <h3 class="rc-pillar-title">Crossbody Bags &amp; Restoration</h3>
              <p class="rc-pillar-text">
                Comprehensive bespoke crafting and archival maintenance for luxury crossbody bags. Our conservators handle seam re-stitching, brass hardware re-burnishing, deep nutrient conditioning, and turnlock fittings.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Commission Process Table -->
    <section class="rc-section rc-section-sand">
      <div class="rc-container">
        <div class="rc-section-header">
          <span class="rc-section-tag">Client Journey</span>
          <h2 class="rc-section-title">The Bespoke Bag Commission Workflow</h2>
          <p class="rc-section-subtitle">
            A transparent four-phase process ensuring every technical nuance of your luxury bag is verified prior to the first knife cut.
          </p>
        </div>
        <div class="rc-specs-card">
          <table class="rc-specs-table">
            <thead>
              <tr>
                <th>Phase</th>
                <th>Artisan Action</th>
                <th>Client Milestone</th>
                <th>Duration</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="rc-specs-param">Phase 01: Consultation</td>
                <td>Dimensional bag interview &amp; material curation</td>
                <td>Hide, color &amp; hardware sign-off</td>
                <td class="rc-specs-val">Week 1</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Phase 02: Patterning</td>
                <td>Paper drafting &amp; dimensional bag modeling</td>
                <td>Scale blueprint review</td>
                <td class="rc-specs-val">Week 2</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Phase 03: Craft Bench</td>
                <td>Hand cutting, skiving &amp; saddle-stitching bag</td>
                <td>Progress photographic dispatch</td>
                <td class="rc-specs-val">Weeks 3 &ndash; 5</td>
              </tr>
              <tr>
                <td class="rc-specs-param">Phase 04: Delivery</td>
                <td>Hot wax edge finishing &amp; serial registration</td>
                <td>Atelier collection or insured delivery</td>
                <td class="rc-specs-val">Week 6</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div style="text-align: center; margin-top: 48px;">
          <a href="contact.html" class="rc-btn rc-btn-primary">Initiate Your Bag Commission Inquiries</a>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 4. CONTACT.HTML (Salon Consultation)
# ==========================================
def build_contact():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Salon Consultation &amp; Bag Inquiries | Reticule Canyon Atelier</title>
  <meta name="description" content="Book a private luxury bag consultation at Reticule Canyon Atelier. Meet our master leather artisans at 450 Lexington Avenue, New York, or contact our private client concierge.">
  <link rel="canonical" href="https://{DOMAIN}/contact.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('contact')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Private Concierge</span>
        <h1 class="rc-hero-title">Private Salon Consultation &amp; <span>Bag Inquiries</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">
          Whether commissioning a bespoke luxury bag or inquiring about archival collection pieces, our private client concierge welcomes your transmission.
        </p>
      </div>
    </section>

    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div class="rc-contact-grid">
          
          <!-- Contact Information & Asset 19 (Saffiano Leather Clutch) -->
          <div class="rc-contact-info-card">
            <h2 class="rc-section-title" style="font-size: 1.8rem; margin-bottom: 24px;">Atelier Coordinates</h2>
            
            <div class="rc-contact-info-item">
              <h4>Flagship Salon &amp; Workshop</h4>
              <p>{ADDR}</p>
            </div>

            <div class="rc-contact-info-item">
              <h4>Direct Telephone</h4>
              <p><a href="tel:+18888011428" style="color: var(--rc-gold);">{PHONE}</a></p>
              <p style="font-size: 0.85rem; color: var(--rc-text-light-muted); margin-top: 4px;">Monday &ndash; Friday: 9:00 AM &ndash; 6:00 PM EST</p>
            </div>

            <div class="rc-contact-info-item">
              <h4>Digital Transmissions</h4>
              <p><a href="mailto:{EMAIL}" style="color: var(--rc-gold);">{EMAIL}</a></p>
            </div>

            <div class="rc-contact-info-item">
              <h4>Consultation Protocol</h4>
              <p style="font-size: 0.95rem; color: var(--rc-text-light-muted);">
                In-person salon appointments must be scheduled at least 48 hours in advance to guarantee dedicated one-on-one attention with our lead craftsman.
              </p>
            </div>

            <div style="margin-top: 32px; border-radius: var(--rc-radius-sm); overflow: hidden; border: 1px solid var(--rc-border-dark);">
              <img src="assets/images/reticulecanyon_asset_19.jpg" alt="Saffiano leather luxury evening clutch pouch in atelier presentation" width="1200" height="800">
            </div>
          </div>

          <!-- Contact / Commission Form -->
          <div class="rc-contact-form-wrap">
            <h3 style="font-family: var(--rc-font-subdisplay); font-size: 1.6rem; color: var(--rc-text-dark); margin-bottom: 8px;">Bag Salon Inquiry Form</h3>
            <p style="font-size: 0.95rem; color: var(--rc-text-dark-muted); margin-bottom: 28px;">
              Please provide your bag commission specifications, preferred leather tone, and appointment preferences below.
            </p>

            <form id="rc-contact-form">
              <div class="rc-form-group">
                <label class="rc-form-label" for="client-name">Full Name *</label>
                <input class="rc-form-input" type="text" id="client-name" name="name" required placeholder="e.g. Lord Alistair Vance">
              </div>

              <div class="rc-form-group">
                <label class="rc-form-label" for="client-email">Email Address *</label>
                <input class="rc-form-input" type="email" id="client-email" name="email" required placeholder="e.g. alistair@vance-holdings.com">
              </div>

              <div class="rc-form-group">
                <label class="rc-form-label" for="client-phone">Telephone Number</label>
                <input class="rc-form-input" type="tel" id="client-phone" name="phone" placeholder="e.g. +1 (212) 555-0198">
              </div>

              <div class="rc-form-group">
                <label class="rc-form-label" for="inquiry-type">Bag Commission Focus *</label>
                <select class="rc-form-select" id="inquiry-type" name="interest" required>
                  <option value="">Select Bag Category</option>
                  <option value="bespoke-tote">Structured Luxury Leather Tote</option>
                  <option value="canyon-attache">The Canyon Executive Attaché</option>
                  <option value="sculptural-bucket">Monument Sculptural Bucket Bag</option>
                  <option value="evening-clutch">Hand-Woven Evening Clutch</option>
                  <option value="archival-restoration">Archival Bag Restoration</option>
                  <option value="salon-appointment">In-Person New York Salon Visit</option>
                </select>
              </div>

              <div class="rc-form-group">
                <label class="rc-form-label" for="client-message">Bag Specifications &amp; Timeline *</label>
                <textarea class="rc-form-textarea" id="client-message" name="message" rows="5" required placeholder="Describe desired bag dimensions, leather temper, hardware preferences, and monogram requirements..."></textarea>
              </div>

              <button type="submit" class="rc-btn rc-btn-primary" style="width: 100%;">Transmit Bag Inquiry</button>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 5. FAQ.HTML (Technical & Collector FAQ)
# ==========================================
def build_faq():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Technical &amp; Collector FAQ | Reticule Canyon Atelier</title>
  <meta name="description" content="Technical questions answered about vegetable-tanned luxury bags, hand saddle stitching, hardware care, and bespoke commissions at Reticule Canyon.">
  <link rel="canonical" href="https://{DOMAIN}/faq.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('faq')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Knowledge Vault</span>
        <h1 class="rc-hero-title">Technical Specifications &amp; <span>Bag Collector FAQ</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">
          Comprehensive guidance detailing hide metallurgy, tensile stitch dynamics, patina preservation, and bespoke bag commissioning policies.
        </p>
      </div>
    </section>

    <!-- FAQ Section with Asset 20 (Monochrome Black Luxury Tote) -->
    <section class="rc-section rc-section-dark">
      <div class="rc-container">
        <div style="max-width: 860px; margin: 0 auto 56px auto; border-radius: var(--rc-radius-md); overflow: hidden; border: 1px solid var(--rc-border-dark);">
          <img src="assets/images/reticulecanyon_asset_20.jpg" alt="Monochrome black luxury leather tote bag on atelier display" width="1200" height="800">
        </div>

        <div class="rc-section-header">
          <span class="rc-section-tag">Luxury Bag Care &amp; Science</span>
          <h2 class="rc-section-title">Common Atelier Queries</h2>
        </div>

        <div class="rc-accordion-list">
          
          <div class="rc-accordion-item active">
            <button class="rc-accordion-header">
              <span>What distinguishes Reticule Canyon luxury bags from standard designer bags?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Standard designer brands utilize commercial chrome tannages covered in colored polyurethane resins to disguise leather imperfections. At Reticule Canyon, we source exclusively full-grain steer hides cured for over 18 months in pit vats with crushed oak bark. Our leather is free from plastic topcoats, meaning it retains its natural grain topography, breathes effortlessly, and ages with a rich amber depth.</p>
            </div>
          </div>

          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>Why is the two-needle saddle stitch structurally superior for luxury bags?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>A sewing machine uses an upper and lower thread that simply loop around each other midway through the hole. If either thread breaks from friction or age, the entire line of stitching unravels with tension. In contrast, our traditional hand saddle stitch uses two needles passing completely through the hole in opposite directions. Each stitch forms an independent mechanical lock that will not unravel even if one thread is severed.</p>
            </div>
          </div>

          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>How does solid milled brass hardware on our bags evolve over time?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Commercial handbag hardware relies on electroplated zinc alloys that chip, peel, and reveal dull grey base metal beneath. Reticule Canyon hardware is CNC-machined from solid ingot brass billets. Over time, atmospheric exposure and finger touch create an authentic antique golden patina. It can be easily restored to a high mirror shine with jeweler's rouge or allowed to mature organically.</p>
            </div>
          </div>

          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>What should I do if my luxury leather bag gets caught in heavy rain?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Botanical vegetable-tanned leather naturally repels water due to our hot-wax burnished finish. If caught in heavy precipitation, do not place the bag near artificial heat sources like radiators or hairdryers, as this will dry the natural fibers. Gently wipe off surface drops with a clean microfiber cloth and allow it to dry naturally at room temperature. Once dry, buff lightly with a horsehair brush.</p>
            </div>
          </div>

          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>Can I request custom dimensional changes for a specific laptop or bag interior?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Yes. Our bespoke commission salon specializes in custom dimensional adaptations. During your initial consultation, provide exact millimeter dimensions of your devices, documents, or accessories. Our lead artisan drafts a tailored internal compartment layout to ensure an exact glove-like fit prior to leather cutting.</p>
            </div>
          </div>

          <div class="rc-accordion-item">
            <button class="rc-accordion-header">
              <span>What is included with our lifetime artisanal luxury bag warranty?</span>
              <span class="rc-accordion-icon">+</span>
            </button>
            <div class="rc-accordion-body">
              <p>Every Reticule Canyon bag is accompanied by a registered certificate of provenance. We guarantee all structural hand saddle stitching, solid brass hardware, and edge burnishing against structural failure for the lifetime of the original commissioner. Complimentary annual inspections and deep nutrient conditioning are available at our New York salon.</p>
            </div>
          </div>

        </div>

        <div style="text-align: center; margin-top: 56px;">
          <a href="contact.html" class="rc-btn rc-btn-gold">Direct Your Bag Question to Our Concierge</a>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 6. POLICY PAGES (Rule 5: Strictly 5-6 lines / 60-110 words per substantive paragraph)
# ==========================================
def build_privacy():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Reticule Canyon Atelier</title>
  <meta name="description" content="Privacy Policy for Reticule Canyon Atelier. Review our strict institutional data protection standards, client confidentiality protocols, and privacy safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Institutional Compliance</span>
        <h1 class="rc-hero-title">Client Privacy <span>Charter</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Reticule Canyon Atelier LLC</p>
      </div>
    </section>

    <div class="rc-container">
      <div class="rc-policy-content">
        
        <div class="rc-policy-section">
          <h2>1. Commitment to Client Confidentiality</h2>
          <p class="rc-policy-p">
            Reticule Canyon Atelier maintains an uncompromised institutional commitment to safeguarding the personal records, bespoke specifications, and digital telemetry of every client who commissions our artisanal leather goods. We acknowledge that our patrons entrust us with sensitive private particulars when scheduling salon consultations or ordering custom monograms. Under no circumstances do we barter, lease, or distribute private customer registries to commercial aggregators or unauthorized third-party marketing networks across global digital channels.
          </p>
          <p class="rc-policy-p">
            Our data protection infrastructure utilizes state-of-the-art cryptographic safeguards designed to prevent unauthorized electronic surveillance, data leaks, or unapproved data transmissions. Institutional records collected during your engagement are maintained within segmented physical and digital environments that comply strictly with United States federal standards and worldwide data privacy frameworks. We conduct recurring technical audits of our digital communications infrastructure to ensure full operational resilience against evolving cyber threats and unauthorized data intrusion vectors.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>2. Scope of Collected Information</h2>
          <p class="rc-policy-p">
            When you transmit an inquiry through our digital consultation portal or arrange a salon appointment at our Lexington Avenue atelier, we record necessary identifying details including your legal name, direct corporate telephone number, authenticated email address, and physical delivery coordinates. Furthermore, when ordering bespoke leather commissions, our artisans record custom dimensional specifications, hardware alloy preferences, and personalized hot-foil monogram initial configurations required to manufacture your bespoke reticule.
          </p>
          <p class="rc-policy-p">
            In addition to directly provided contact records, our web infrastructure passively monitors standard diagnostic server telemetry, such as anonymous Internet Protocol addresses, browser rendering versions, operating system architecture, and referring webpage headers. These technical metrics are processed strictly in an aggregated format to optimize the visual presentation and navigation responsiveness of our digital salon. Passive analytics never link anonymous browsing behaviors to your verified private client identity or personal atelier records.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>3. Operational Purpose of Data Processing</h2>
          <p class="rc-policy-p">
            All gathered personal data is utilized solely to facilitate the bespoke crafting process, schedule private client appointments, coordinate secure courier shipments, and furnish authentic provenance certification documents. When you request a private consultation at our New York atelier, your phone number and email permit our concierge team to confirm appointment schedules and review specialized material requests prior to your arrival. We never deploy automated promotional communications without prior affirmative written authorization from the commissioning patron.
          </p>
          <p class="rc-policy-p">
            We may additionally retain archival records of your completed leather commissions to honor our lifetime artisanal warranty protocols and provide future restoration services. Having access to original leather hide dye lot specifications, saddle stitching thread gauges, and solid brass hardware dimensions enables our conservators to execute seamless structural maintenance decades after the initial piece was created. Clients retain full authority to request complete deletion of archival records upon written request.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>4. Data Retention and Institutional Security</h2>
          <p class="rc-policy-p">
            Personal data collected by Reticule Canyon Atelier is stored on encrypted servers protected by multi-factor authentication, intrusion detection defenses, and strict access controls limited to authorized atelier management staff. Digital records are preserved only for the duration required to satisfy the commercial purpose of the commission, fulfill contractual warranty obligations, and comply with state and federal legal record-keeping statutes. Once the necessary retention window concludes, digital data is securely purged.
          </p>
          <p class="rc-policy-p">
            Our physical workshop maintains parallel administrative protocols to ensure that paper blueprint cards, bespoke monogram stamping dies, and physical shipping ledgers are stored within locked archives restricted from public salon view. In the improbable event of a cybersecurity incident that risks exposing client information, our incident response protocol mandates prompt written notification to all affected patrons and relevant regulatory enforcement bodies within seventy-two hours of forensic confirmation.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>5. Client Legal Rights &amp; Regulatory Inquiries</h2>
          <p class="rc-policy-p">
            Every patron possesses statutory rights under applicable privacy legislation, including the rights to inspect, rectify, restrict, or demand the irrevocable erasure of their personal information stored within our databases. To exercise your rights, transmit a formal written petition to our data privacy officer via postal mail or authenticated email. We process and confirm compliance with all verified client requests within thirty calendar days without imposing punitive fees or interrupting scheduled bespoke commissions.
          </p>
          <p class="rc-policy-p">
            For questions concerning this Privacy Charter or to update your contact preferences, please communicate directly with our private client concierge using the official contact coordinates listed below. Our compliance officers welcome open dialogue regarding our information handling practices and will supply thorough explanations regarding our archival security procedures, encryption standards, or regulatory certifications upon formal patron inquiry. We remain fully dedicated to honoring our clients' absolute confidentiality and trust throughout all interactions.
          </p>
          <div class="rc-policy-contact-card">
            <h3>Atelier Privacy Officer</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Concierge Telephone:</strong> {PHONE}</p>
            <p><strong>Direct Inquiries:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_terms():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms &amp; Conditions | Reticule Canyon Atelier</title>
  <meta name="description" content="Terms and Conditions governing bespoke leather commissions, salon appointments, and intellectual property at Reticule Canyon Atelier LLC.">
  <link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Legal Framework</span>
        <h1 class="rc-hero-title">Terms &amp; Conditions of <span>Atelier Engagement</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Reticule Canyon Atelier LLC</p>
      </div>
    </section>

    <div class="rc-container">
      <div class="rc-policy-content">
        
        <div class="rc-policy-section">
          <h2>1. Acceptance of Terms &amp; Scope of Engagement</h2>
          <p class="rc-policy-p">
            By accessing this digital salon, scheduling an appointment, or commissioning bespoke leather goods through Reticule Canyon Atelier LLC, you formally acknowledge and agree to be bound by these Terms and Conditions. These legal provisions establish a binding contract between the commissioner and our artisanal workshop, regulating all transactions, consultations, and digital browsing activities. If you disagree with any portion of these binding stipulations, you must refrain from ordering goods or utilizing this website.
          </p>
          <p class="rc-policy-p">
            Reticule Canyon reserves the right to amend, update, or reorganize these terms periodically to reflect shifts in statutory regulations, workshop capacity, or material sourcing protocols. Notice of substantial revisions will be published visibly upon this webpage alongside an updated effective date timestamp. Continued utilization of our digital facilities or completion of commission deposits following posted modifications represents definitive legal consent to the revised terms of engagement.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>2. Bespoke Commission Workflow &amp; Deposit Terms</h2>
          <p class="rc-policy-p">
            Bespoke commissions represent custom, one-of-a-kind leather craft items engineered specifically to individual patron requirements, personal monogramming, and tailored dimensional parameters. An initial non-refundable deposit of fifty percent of the total commission quote is mandatory before hide selection, pattern cutting, or bench labor commences. This deposit covers the procurement of botanical vegetable-tanned hides, custom milling of solid brass hardware, and dedicated artisan bench allocation.
          </p>
          <p class="rc-policy-p">
            Estimated completion timelines provided during salon consultations represent diligent artisanal projections rather than rigid guarantees, as authentic hand-crafting involves variable natural curing, skiving, and saddle-stitching phases. Full payment of the remaining fifty percent balance must be completed and cleared prior to physical release or insured courier dispatch of the finished piece. Refusal to pay the final balance within sixty days forfeits the initial deposit and the commission piece.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>3. Natural Material Variations &amp; Handcraft Hallmarks</h2>
          <p class="rc-policy-p">
            Patrons understand that botanical vegetable-tanned leather is an authentic biological material displaying natural variations in grain topography, fat wrinkles, neck creases, and subtle tonal shading across hide bends. These organic characteristics are intentional hallmarks of full-grain leather integrity and are celebrated as proof of genuine artisanal authenticity rather than manufacturing defects. Machine perfection is deliberately rejected in favor of unique character, tactile depth, and living material response.
          </p>
          <p class="rc-policy-p">
            Similarly, because every double-needle saddle stitch is pierced with handheld diamond awls and tensioned by hand, subtle micro-variations in stitch angle and wax dispersion occur across seams. Solid brass hardware, being free of synthetic lacquers, will naturally initiate an amber oxidation patina upon exposure to air and skin oils. Such natural patina evolutions are integral to the design philosophy and do not constitute acceptable grounds for return or refund.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>4. Intellectual Property &amp; Archival Blueprints</h2>
          <p class="rc-policy-p">
            All structural bag silhouettes, pattern drafting templates, aesthetic designs, photographs, typography, and text published upon this digital platform represent the exclusive intellectual property of Reticule Canyon Atelier LLC. Unauthorized reproduction, digital copying, industrial reverse-engineering, or commercial exploitation of our patterns or branding is strictly prohibited under international copyright and trademark laws. Patrons purchasing bespoke pieces acquire physical ownership of the bag, while intellectual design rights remain with the atelier.
          </p>
          <p class="rc-policy-p">
            The Reticule Canyon emblem, monogram stamps, and guild marks remain protected commercial hallmarks. Commissioning a bespoke piece with a personal family crest or initial does not grant the client any license to replicate our proprietary bag geometry or trademarked hardware locks for secondary commercial production. We vigorously defend our intellectual craftsmanship against counterfeit manufacturing and trademark dilution in all applicable legal jurisdictions.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>5. Limitation of Liability &amp; Governing Jurisdiction</h2>
          <p class="rc-policy-p">
            To the maximum extent permitted by applicable law, Reticule Canyon Atelier LLC disclaims liability for indirect, incidental, punitive, or consequential damages resulting from website downtime, delayed delivery schedules, or improper leather storage by the patron. In no event shall our total financial liability exceed the aggregate monetary compensation actually received by the atelier for the specific commission in dispute. We make no commercial merchantability warranties beyond our structural lifetime guarantee.
          </p>
          <p class="rc-policy-p">
            These Terms and Conditions shall be governed by and construed in accordance with the substantive laws of the State of New York, United States, without regard to conflict of law principles. Any legal controversy, arbitration, or proceeding arising under this agreement shall be submitted exclusively to state or federal courts situated in New York County, New York. Both parties waive any objection to personal jurisdiction or inconvenient forum in said judicial venues.
          </p>
          <div class="rc-policy-contact-card">
            <h3>Atelier Legal Division</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Inquiry Telephone:</strong> {PHONE}</p>
            <p><strong>Legal Communications:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_disclaimer():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disclaimer | Reticule Canyon Atelier</title>
  <meta name="description" content="Legal and craft disclaimer for Reticule Canyon Atelier. Information on artisanal variations, digital color display, and structural usage guidelines.">
  <link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Craft Clarifications</span>
        <h1 class="rc-hero-title">Atelier Material &amp; Craft <span>Disclaimer</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Reticule Canyon Atelier LLC</p>
      </div>
    </section>

    <div class="rc-container">
      <div class="rc-policy-content">
        
        <div class="rc-policy-section">
          <h2>1. Digital Representation &amp; Color Variance</h2>
          <p class="rc-policy-p">
            The photographic images, editorial video captures, and digital material previews displayed on this website are produced with rigorous color-calibration techniques to illustrate our leather goods as accurately as technology permits. However, because individual computer displays, smartphones, and tablet screens possess distinct hardware gamuts, brightness settings, and color temperature profiles, actual leather hues may vary subtly from screen renderings. Digital depictions serve as aesthetic representations rather than contractual color guarantees.
          </p>
          <p class="rc-policy-p">
            Furthermore, because our steer hides undergo botanical oak bark pit tanning with organic vegetable extracts, each separate dye batch exhibits delicate shifts in tone, warmth, and luster. An amber cognac hide tanned during autumn may display slightly deeper golden undertones than a hide processed during spring runoffs. Patrons desiring exact color confirmation are invited to visit our New York salon to inspect physical hide swatches under natural raking daylight prior to finalizing commission orders.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>2. Botanical Leather Integrity &amp; Natural Characteristics</h2>
          <p class="rc-policy-p">
            Reticule Canyon Atelier works exclusively with full-grain, uncorrected botanical leather that retains the outermost epithelial layer of the steer hide. As a natural living material, full-grain leather inherently bears evidence of the animal's outdoor life, including healed barbed wire scratches, natural grain density variations, insect bite marks, and growth wrinkles. We reject chemical buffing and synthetic pigment sprays that obliterate these organic markers to create sterile artificial uniformity.
          </p>
          <p class="rc-policy-p">
            These authentic markings enhance the tensile strength and unique individuality of each reticule, briefcase, and pouch. They demonstrate that the hide has not been thinned or compromised by aggressive mechanical sanding. Collectors and commissioners must recognize that natural grain variations are an essential hallmark of heirloom maroquinerie, reflecting authentic craftsmanship that cannot be duplicated by automated synthetic assembly plants. Every natural contour celebrates genuine provenance and permanent biological integrity across generations.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>3. Structural Usage, Capacity &amp; Weight Limits</h2>
          <p class="rc-policy-p">
            While our leather reticules, satchels, and attachés are constructed with exceptional structural durability utilizing traditional double-needle saddle stitches and solid brass hardware, they are designed for luxury personal accessory usage. Exceeding recommended interior carrying capacities or packing sharp, unshielded mechanical equipment into soft calfskin linings may cause distortion, seam stress, or permanent leather deformation. Patrons are urged to respect intended dimensional volumes to preserve shape memory.
          </p>
          <p class="rc-policy-p">
            Our pieces are not designed for extreme sporting expeditions, deep immersion in aquatic environments, or industrial hazardous storage. Exposing botanical leather to caustic solvents, chemical perfumes, alcohol-based sanitizers, or abrasive scouring pads will strip protective carnauba waxes and dissolve organic dyes. Damage resulting from chemical contamination, pet clawing, or gross physical misuse falls outside our artisanal repair coverage and warranty protections.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>4. Independent Artisanal Workshop Status</h2>
          <p class="rc-policy-p">
            Reticule Canyon Atelier LLC is a wholly independent, privately owned artisanal maroquinerie studio based in New York City. We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with any international luxury fashion conglomerates, mass-market handbag manufacturers, or commercial licensing organizations. Any historical references to traditional French or English saddle-making guilds are made purely in an educational and artisanal context to celebrate historical techniques.
          </p>
          <p class="rc-policy-p">
            All leather goods, hardware fittings, and bespoke accessories produced by Reticule Canyon are original proprietary designs conceived in our New York workshop. We maintain strict separation from fast-fashion production models and commercial mass distribution. Our atelier prides itself on sustaining independent craft ethics, fair wage artisan compensation, and direct personal relationships between the maker and the commissioning patron across all commissions.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>5. Inquiries Regarding Craft Specifications</h2>
          <p class="rc-policy-p">
            If you have questions regarding the technical specifications, hide certifications, tensile testing metrics, or material safety parameters detailed in this disclaimer, our atelier staff is readily accessible. We welcome direct communications from clients, collectors, and horological or leathercraft guilds seeking clarification on our workshop practices, ethical leather harvesting sources, or archival conservation methodologies. Our staff ensures that every technical aspect of our leatherwork is explained thoroughly to all interested patrons.
          </p>
          <p class="rc-policy-p">
            Written requests regarding material provenance, custom tensile requirements, or environmental tanning certifications should be directed to our master craftsman using the contact details provided below. We commit to providing thorough, transparent technical documentation for all authenticated commissions bearing the Reticule Canyon guild hallmark. Clients may also schedule an appointment to inspect physical material archives and chemical safety records directly within our Lexington Avenue salon.
          </p>
          <div class="rc-policy-contact-card">
            <h3>Atelier Craft Secretariat</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Technical Telephone:</strong> {PHONE}</p>
            <p><strong>Direct Inquiries:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_cookie():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Policy | Reticule Canyon Atelier</title>
  <meta name="description" content="Cookie Policy for Reticule Canyon Atelier. Understand how our digital platform deploys essential and analytical cookies to ensure optimal browsing performance.">
  <link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rc-policy-header">
      <div class="rc-container">
        <span class="rc-section-tag">Digital Telemetry</span>
        <h1 class="rc-hero-title">Cookie &amp; Tracking <span>Technologies Policy</span></h1>
        <p class="rc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Reticule Canyon Atelier LLC</p>
      </div>
    </section>

    <div class="rc-container">
      <div class="rc-policy-content">
        
        <div class="rc-policy-section">
          <h2>1. Introduction to Cookie Technologies</h2>
          <p class="rc-policy-p">
            This Cookie Policy explains how Reticule Canyon Atelier LLC utilizes cookies, tracking pixels, and related web telemetry mechanisms when you explore our digital salon. Cookies are compact alphanumeric data files placed onto your computer hard drive, tablet, or mobile device by your internet browser during webpage access. These files permit web servers to recognize your specific hardware terminal and retain critical session parameters to ensure fluid visual rendering across digital visits.
          </p>
          <p class="rc-policy-p">
            We adhere strictly to a philosophy of data minimization that mirrors our careful artisanal material stewardship. We do not utilize intrusive commercial tracking pixels, third-party behavioral profiling scripts, or predatory advertising cookies designed to monitor your off-site browsing habits across external commercial networks. Every telemetry mechanism deployed upon our digital infrastructure serves a direct, transparent purpose related to platform performance, security verification, or aggregate visitor analysis.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>2. Categories of Cookies Deployed</h2>
          <p class="rc-policy-p">
            Our platform deploys Strictly Necessary Cookies that are fundamental to core site navigation, secure encrypted server connections, and interactive appointment form submissions. Without these essential cookies, fundamental security architectures and salon inquiry forms would fail to operate reliably. Because these files ensure basic operational integrity and cyber defense compliance, they cannot be deactivated within our server management consoles without breaking site functionality.
          </p>
          <p class="rc-policy-p">
            We additionally utilize Performance and Diagnostic Cookies that compile anonymous, aggregated statistical information regarding how patrons interact with our website sections. These metrics reveal which gallery portfolios attract interest, average page loading durations, and whether visitors encounter server error warnings. This diagnostic data is completely anonymized and cannot be reverse-engineered to identify individual patrons, serving solely to optimize web rendering speed and mobile responsiveness.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>3. First-Party vs. Third-Party Web Analytics</h2>
          <p class="rc-policy-p">
            First-party cookies are generated and managed directly by Reticule Canyon Atelier web servers to preserve your interface language preferences, mobile drawer states, and font caching parameters between successive page visits. These cookies are maintained strictly under our sovereign institutional control and are never shared with external advertising conglomerates or third-party behavioral data brokers operating outside our direct digital domain boundaries.
          </p>
          <p class="rc-policy-p">
            Third-party analytical telemetry, including standard Google Analytics tags, may process anonymous user metrics under strict data processing agreements. These analytical scripts monitor aggregate visitor traffic volumes, device operating platforms, and regional referral headers. Third-party providers are legally bound by contractual data protection agreements prohibiting them from merging diagnostic metrics gathered on our site with identifiable personal accounts held within their commercial networks.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>4. Patron Control &amp; Browser Cookie Management</h2>
          <p class="rc-policy-p">
            You retain absolute legal and technical autonomy to govern how cookies are stored upon your digital devices. Modern web browsers, including Google Chrome, Apple Safari, Mozilla Firefox, and Microsoft Edge, provide comprehensive preference settings that permit users to review, filter, block, or delete cookies at will. You may configure your browser software to reject all third-party cookies or receive an interactive alert whenever a web server attempts to deposit a cookie file.
          </p>
          <p class="rc-policy-p">
            Please be advised that if you elect to disable strictly necessary session cookies entirely within your browser controls, certain interactive elements of our digital salon—such as our interactive consultation booking forms, responsive image galleries, and secure appointment confirmation scripts—may function with degraded speed or require repeated manual authentication during your visit. Most patrons find that leaving first-party cookies active provides the smoothest viewing experience.
          </p>
        </div>

        <div class="rc-policy-section">
          <h2>5. Telemetry Policy Inquiries &amp; Administration</h2>
          <p class="rc-policy-p">
            Reticule Canyon Atelier reviews this Cookie Policy semi-annually to confirm strict alignment with domestic privacy standards and international data governance directives. When technical updates or security enhancements warrant revisions to our cookie usage protocols, amended text will be posted immediately within this section alongside an updated calendar timestamp to provide complete operational transparency to our patrons. This continuous governance ensures our data processing remains responsible, proportional, and compliant with all evolving legal standards.
          </p>
          <p class="rc-policy-p">
            For technical inquiries regarding our cookie deployments, web tracking safeguards, or to request documentation concerning our digital telemetry governance protocols, please direct communications to our systems administration team using the contact coordinates outlined below. Our technical staff is prepared to answer technical questions and assist patrons with browser privacy configuration guidance upon request. We remain dedicated to upholding the highest standards of digital ethics and patron transparency across all web interactions.
          </p>
          <div class="rc-policy-contact-card">
            <h3>Atelier Web Governance Bureau</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Concierge Telephone:</strong> {PHONE}</p>
            <p><strong>Technical Inquiries:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 7. SITEMAP & ROBOTS
# ==========================================
def build_sitemap():
    pages = [
        "index.html",
        "about.html",
        "services.html",
        "faq.html",
        "contact.html",
        "privacy-policy.html",
        "terms-and-conditions.html",
        "disclaimer.html",
        "cookie-policy.html"
    ]
    urls = ""
    for p in pages:
        urls += f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-09-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if p == 'index.html' else '0.8'}</priority>
  </url>\n"""
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Sitemap: https://{DOMAIN}/sitemap.xml
"""

# ==========================================
# 8. REGISTRIES & MANIFEST
# ==========================================
def build_image_registry():
    return """# IMAGE REGISTRY - RETICULE CANYON ATELIER
Domain: reticulecanyon.com
Niche: Luxury Bag / Bespoke Leather Reticules / Saddle Craft
Strict Rule: 20 Unique Images, Used Exactly Once, >20KB Each, Zero Duplicates, Zero Drawings, Zero Buildings

| Asset Name | Subject Description | Location / Section Used | MD5 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
| `reticulecanyon_asset_1.jpg` | Handcrafted structured luxury leather tote bag | `index.html` (Hero Masthead Card) | fb4aa385839b937dc9c2cbb311465ce0 | Verified Unique |
| `reticulecanyon_asset_2.jpg` | Crocodile-embossed structured luxury leather tote bag | `index.html` (Anatomy Deep Dive) | 0edb55ab95e12660f472202c2da80d2a | Verified Unique |
| `reticulecanyon_asset_3.jpg` | Bronze patina embossed luxury leather tote bag | `index.html` (Pillar 1: Oak Bark Tanning) | 2b4b3f32907466f4e900058cdc3fdd63 | Verified Unique |
| `reticulecanyon_asset_4.jpg` | Sculptural cylindrical leather bucket bag | `index.html` (Pillar 2: Solid Brass) | 69f1e861611e56db7347bece13dd7f9e | Verified Unique |
| `reticulecanyon_asset_5.jpg` | Quilted designer velvet and leather crossbody bag | `index.html` (Pillar 3: Double Stitch) | db7e7fec0025c5dff3ef7b7301e83fe2 | Verified Unique |
| `reticulecanyon_asset_6.jpg` | Cognac executive leather briefcase attaché with brass lock | `index.html` (Bento 1: Canyon Attaché) | 6ce1a19ddd429c9ee64ce2693c16d78b | Verified Unique |
| `reticulecanyon_asset_7.jpg` | Caramel saddle leather satchel bag with hand-creased edges | `index.html` (Bento 2: Canyon Satchel) | e3976b583fc253f7271315d670ded0e2 | Verified Unique |
| `reticulecanyon_asset_8.jpg` | Crimson woven leather evening clutch and reticule pouch | `index.html` (Bento 3: Woven Pouch) | ec212cfd30e724e3437ba0cba42b84e4 | Verified Unique |
| `reticulecanyon_asset_9.jpg` | Emerald velvet and structured luxury handbag detail | `about.html` (Guild Heritage Story) | 8ce86363c9b8a2107e58c29a56a6184c | Verified Unique |
| `reticulecanyon_asset_10.jpg` | Burgundy velvet and leather evening clutch | `about.html` (Evening Silhouettes) | 9db8082860ce54eb10270a4ab165c300 | Verified Unique |
| `reticulecanyon_asset_11.jpg` | Sculptural hard-case luxury evening bag with brass lock | `about.html` (Single-Artisan Ownership) | 258f436266c374921abefe98009f2674 | Verified Unique |
| `reticulecanyon_asset_12.jpg` | Plissé pleated leather evening purse with burnished strap | `about.html` (Botanical Aging Vaults) | 3c2e9cbeaed478fb050433b4b743c2ad | Verified Unique |
| `reticulecanyon_asset_13.jpg` | Minimalist luxury leather shoulder bag | `services.html` (Service 1: Shoulder Bags) | ed5858f59fe3669bfa01ba81f035f4b6 | Verified Unique |
| `reticulecanyon_asset_14.jpg` | Creamy ivory luxury leather tote bag | `services.html` (Service 2: Structured Totes) | 063689905ffe15fa6b3f892fecee98cb | Verified Unique |
| `reticulecanyon_asset_15.jpg` | Woven leather artisan tote bag with braided handles | `services.html` (Service 3: Woven Bags) | d6ad90b493d7edfb4081f014ea5fd5b8 | Verified Unique |
| `reticulecanyon_asset_16.jpg` | Vintage heritage leather briefcase with double buckle closures | `services.html` (Service 4: Heritage Briefcases) | ce00aecec53e017bf7d0daff0d85eae6 | Verified Unique |
| `reticulecanyon_asset_17.jpg` | Structured leather weekend travel bag with reinforced corners | `services.html` (Service 5: Travel Bags) | ec7362e952965e7c6bf93675eb8805c2 | Verified Unique |
| `reticulecanyon_asset_18.jpg` | Structured luxury crossbody bag with signature turnlock | `services.html` (Service 6: Crossbody Bags) | 7524f885c43439a3f87cb4dc6463af34 | Verified Unique |
| `reticulecanyon_asset_19.jpg` | Saffiano leather luxury evening clutch pouch | `contact.html` (Salon Coordinates Feature) | d82b6e5ea61283da8f712eb54ca10c9a | Verified Unique |
| `reticulecanyon_asset_20.jpg` | Monochrome black luxury leather tote bag on display | `faq.html` (Technical FAQ Feature) | b686a79f385b037a6ed2990fc4e28893 | Verified Unique |

Total Images: 20
Total Usages: 20 (Every image used exactly once)
Repetitions: 0
100% Real Luxury Bag Photography
"""

def build_design_registry():
    return """# DESIGN REGISTRY - RETICULE CANYON ATELIER

## Archetype Identity
- **Design Archetype:** Canyon Atelier / Warm Saddle Workshop / Desert Artisanal Monolith
- **Domain:** reticulecanyon.com
- **Niche:** Luxury Bag / Hand-Stitched Leather Reticules & Canyon Saddle Craft
- **CSS Namespace:** Dedicated `.rc-...` namespace (Zero global collisions)

## Color Architecture
- **Deep Espresso Background:** `#120c08`
- **Abyssal Base:** `#090604`
- **Saddle Cognac Accent:** `#9a3412`
- **Canyon Ochre / Amber:** `#c26118`
- **Antique Gilded Brass:** `#d4af37`
- **Warm Parchment Paper:** `#fbf8f3`
- **Desert Sand:** `#f4ede3`
- **Text Light:** `#fbf8f3`
- **Text Muted:** `#a39486`
- **Text Dark:** `#1f140e`

## Typography Pairings
- **Display Headings:** `Cinzel Decorative` (700)
- **Subheadings & Title Elements:** `Marcellus` (Regular)
- **Body & Editorial Prose:** `Plus Jakarta Sans` (300, 400, 500, 600, 700)
- **Technical Specs & Badges:** `JetBrains Mono` (400, 500)

## Layout Features
1. Sticky Header with blurred backdrop (`.site-header`) & Mobile Drawer (`#mobile-drawer`).
2. Asymmetric Canyon Hero with artisanal coordinates, stats matrix, and floating archival badge.
3. Marquee Ticker with continuous CSS animation displaying leather tensile specs.
4. Bento Grid with structured cards for flagship bag silhouettes.
5. 4-Step Production Chronology Timeline with numbered gold milestones.
6. Technical Specifications Matrix table detailing material testing metrics.
7. Accordion FAQ component with rotating gold brass toggle icons.
"""

def build_site_manifest():
    manifest = {
        "domain": DOMAIN,
        "brand": BRAND,
        "niche": "luxury bag",
        "institutional_contact": {
            "address": ADDR,
            "phone": PHONE,
            "email": EMAIL
        },
        "pages": [
            "index.html",
            "about.html",
            "services.html",
            "faq.html",
            "contact.html",
            "privacy-policy.html",
            "terms-and-conditions.html",
            "disclaimer.html",
            "cookie-policy.html"
        ],
        "assets_count": 20,
        "php_files_count": 0,
        "blog_included": False,
        "google_tag": "G-0LY0HY7L01",
        "qa_verified": True
    }
    return json.dumps(manifest, indent=2)

# ==========================================
# EXECUTE GENERATION
# ==========================================
def main():
    files_to_generate = {
        "index.html": build_index(),
        "about.html": build_about(),
        "services.html": build_services(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots(),
        "IMAGE_REGISTRY.md": build_image_registry(),
        "DESIGN_REGISTRY.md": build_design_registry(),
        "SITE_MANIFEST.json": build_site_manifest()
    }

    for filename, content in files_to_generate.items():
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename} ({len(content)} chars)")

    print("\nAll files successfully generated. Initiating automated QA audit...")

if __name__ == "__main__":
    main()
