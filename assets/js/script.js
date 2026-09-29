/**
 * Reticule Canyon Atelier - Interactive Engine
 * Synchronized Mobile Drawer, Accordions, Smooth Scroll & Form Interactivity
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Mobile Drawer Toggle
  const hamburger = document.getElementById('rc-hamburger');
  const drawer = document.getElementById('mobile-drawer');
  const drawerClose = document.getElementById('mobile-drawer-close');
  const drawerBackdrop = document.getElementById('mobile-drawer-backdrop');

  function openDrawer() {
    if (drawer) drawer.classList.add('active');
    if (drawerBackdrop) drawerBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (drawer) drawer.classList.remove('active');
    if (drawerBackdrop) drawerBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (hamburger) {
    hamburger.addEventListener('click', function(e) {
      e.preventDefault();
      openDrawer();
    });
  }

  if (drawerClose) {
    drawerClose.addEventListener('click', function(e) {
      e.preventDefault();
      closeDrawer();
    });
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', closeDrawer);
  }

  // Close drawer on clicking any mobile nav link
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');
  mobileLinks.forEach(function (link) {
    link.addEventListener('click', closeDrawer);
  });

  // 2. Accordions (FAQ & Technical Care)
  const accordionHeaders = document.querySelectorAll('.rc-accordion-header');
  accordionHeaders.forEach(function (header) {
    header.addEventListener('click', function () {
      const item = this.parentElement;
      const isActive = item.classList.contains('active');

      // Optional: close other accordions in the same list
      const parentList = item.parentElement;
      if (parentList && parentList.classList.contains('rc-accordion-list')) {
        parentList.querySelectorAll('.rc-accordion-item').forEach(function (sibling) {
          sibling.classList.remove('active');
        });
      }

      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // 3. Contact Form Submission Feedback
  const contactForm = document.getElementById('rc-contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('.rc-btn-primary');
      const originalText = submitBtn.innerText;
      submitBtn.innerText = 'TRANSMITTING INQUIRY...';
      submitBtn.disabled = true;

      setTimeout(function () {
        submitBtn.innerText = 'INQUIRY LOGGED WITH ATELIER';
        submitBtn.style.background = '#2e7d32';
        submitBtn.style.borderColor = '#2e7d32';

        const successNotice = document.createElement('div');
        successNotice.style.marginTop = '18px';
        successNotice.style.padding = '14px 18px';
        successNotice.style.borderRadius = '4px';
        successNotice.style.background = 'rgba(46, 125, 50, 0.12)';
        successNotice.style.border = '1px solid #2e7d32';
        successNotice.style.color = '#1b5e20';
        successNotice.style.fontSize = '0.9rem';
        successNotice.style.fontFamily = 'var(--rc-font-body)';
        successNotice.innerText = 'Thank you for contacting Reticule Canyon. A private client concierge has received your commission specifications and will respond within 24 business hours.';
        
        contactForm.appendChild(successNotice);
        contactForm.reset();
      }, 1200);
    });
  }
});
