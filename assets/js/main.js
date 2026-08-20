/*!
 * WaveNode — AI Video & Audio Streaming Platform Template
 * main.js — all interactivity, dependency-free vanilla JavaScript.
 *
 * Modules (each hooks onto data- attributes, so removing a block of
 * markup never throws an error):
 *   1. Theme toggle (dark / light, persisted to localStorage)
 *   2. Sticky header state
 *   3. Mobile navigation drawer
 *   4. Scroll-reveal animations (IntersectionObserver)
 *   5. Accordions (FAQ)
 *   6. Pricing billing toggle (monthly / annual)
 *   7. Copy-to-clipboard for code blocks
 *   8. Back-to-top button
 *   9. Current year stamp
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'wavenode-theme';

  /* ----------------------------------------------------------------
     1. Theme toggle
     The initial theme class is applied by the tiny inline script in
     <head> (prevents flash of wrong theme). This module only handles
     the click behaviour.
  ---------------------------------------------------------------- */
  function initThemeToggle() {
    var root = document.documentElement;
    var buttons = document.querySelectorAll('[data-theme-toggle]');

    buttons.forEach(function (button) {
      button.addEventListener('click', function () {
        var isDark = root.classList.toggle('dark');
        try {
          localStorage.setItem(STORAGE_KEY, isDark ? 'dark' : 'light');
        } catch (err) {
          /* localStorage unavailable (private mode) — theme still toggles */
        }
        buttons.forEach(function (b) {
          b.setAttribute('aria-pressed', String(isDark));
        });
      });
    });
  }

  /* ----------------------------------------------------------------
     2. Sticky header — adds a frosted background once the page scrolls
  ---------------------------------------------------------------- */
  function initStickyHeader() {
    var header = document.querySelector('[data-header]');
    if (!header) return;

    var update = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 24);
    };

    update();
    window.addEventListener('scroll', update, { passive: true });
  }

  /* ----------------------------------------------------------------
     3. Mobile navigation drawer
  ---------------------------------------------------------------- */
  function initMobileMenu() {
    var toggle = document.querySelector('[data-menu-toggle]');
    var menu = document.querySelector('[data-mobile-menu]');
    if (!toggle || !menu) return;

    var iconOpen = toggle.querySelector('[data-icon-open]');
    var iconClose = toggle.querySelector('[data-icon-close]');

    function setState(open) {
      menu.classList.toggle('hidden', !open);
      toggle.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('overflow-hidden', open);
      if (iconOpen && iconClose) {
        iconOpen.classList.toggle('hidden', open);
        iconClose.classList.toggle('hidden', !open);
      }
    }

    toggle.addEventListener('click', function () {
      setState(menu.classList.contains('hidden'));
    });

    // Close when a navigation link inside the drawer is used
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        setState(false);
      });
    });

    // Close on Escape
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !menu.classList.contains('hidden')) {
        setState(false);
        toggle.focus();
      }
    });

    // Reset drawer state when resizing up to the desktop layout
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1024) setState(false);
    });
  }

  /* ----------------------------------------------------------------
     4. Scroll-reveal animations
  ---------------------------------------------------------------- */
  function initReveal() {
    var items = document.querySelectorAll('[data-reveal]');
    if (!items.length) return;

    if (!('IntersectionObserver' in window)) {
      items.forEach(function (item) {
        item.classList.add('is-revealed');
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    items.forEach(function (item) {
      observer.observe(item);
    });
  }

  /* ----------------------------------------------------------------
     5. Accordions
     Markup contract:
       <div data-accordion>
         <h3><button data-accordion-trigger aria-expanded="false">…</button></h3>
         <div data-accordion-panel class="accordion-panel"><div>…</div></div>
       </div>
  ---------------------------------------------------------------- */
  function initAccordions() {
    document.querySelectorAll('[data-accordion]').forEach(function (item) {
      var trigger = item.querySelector('[data-accordion-trigger]');
      var panel = item.querySelector('[data-accordion-panel]');
      if (!trigger || !panel) return;

      trigger.addEventListener('click', function () {
        var isOpen = panel.classList.toggle('is-open');
        trigger.setAttribute('aria-expanded', String(isOpen));

        // Optional single-open behaviour within a [data-accordion-group]
        var group = item.closest('[data-accordion-group]');
        if (group && isOpen) {
          group.querySelectorAll('[data-accordion]').forEach(function (other) {
            if (other === item) return;
            var otherPanel = other.querySelector('[data-accordion-panel]');
            var otherTrigger = other.querySelector('[data-accordion-trigger]');
            if (otherPanel) otherPanel.classList.remove('is-open');
            if (otherTrigger) otherTrigger.setAttribute('aria-expanded', 'false');
          });
        }
      });
    });
  }

  /* ----------------------------------------------------------------
     6. Pricing billing toggle
     [data-billing-toggle]        — the switch button
     [data-price-monthly]         — element shown for monthly billing
     [data-price-annual]          — element shown for annual billing
  ---------------------------------------------------------------- */
  function initBillingToggle() {
    var toggles = document.querySelectorAll('[data-billing-toggle]');
    if (!toggles.length) return;

    function setBilling(annual) {
      document.querySelectorAll('[data-price-monthly]').forEach(function (el) {
        el.classList.toggle('hidden', annual);
      });
      document.querySelectorAll('[data-price-annual]').forEach(function (el) {
        el.classList.toggle('hidden', !annual);
      });
      toggles.forEach(function (t) {
        t.setAttribute('aria-checked', String(annual));
        var knob = t.querySelector('[data-toggle-knob]');
        if (knob) {
          knob.classList.toggle('translate-x-5', annual);
          knob.classList.toggle('translate-x-0', !annual);
        }
        t.classList.toggle('bg-primary-600', annual);
        t.classList.toggle('bg-slate-300', !annual);
        t.classList.toggle('dark:bg-slate-700', !annual);
      });
    }

    toggles.forEach(function (toggle) {
      toggle.addEventListener('click', function () {
        setBilling(toggle.getAttribute('aria-checked') !== 'true');
      });
    });

    // Annual is the default (best-value view)
    setBilling(true);
  }

  /* ----------------------------------------------------------------
     7. Copy-to-clipboard for code blocks
     <button data-copy data-copy-target="#snippet-id">
  ---------------------------------------------------------------- */
  function initCopyButtons() {
    document.querySelectorAll('[data-copy]').forEach(function (button) {
      button.addEventListener('click', function () {
        var selector = button.getAttribute('data-copy-target');
        var target = selector ? document.querySelector(selector) : null;
        if (!target || !navigator.clipboard) return;

        navigator.clipboard.writeText(target.innerText).then(function () {
          var original = button.innerHTML;
          button.innerHTML = 'Copied!';
          window.setTimeout(function () {
            button.innerHTML = original;
          }, 1600);
        });
      });
    });
  }

  /* ----------------------------------------------------------------
     8. Back-to-top button
  ---------------------------------------------------------------- */
  function initBackToTop() {
    var button = document.querySelector('[data-back-to-top]');
    if (!button) return;

    var update = function () {
      var visible = window.scrollY > 600;
      button.classList.toggle('opacity-0', !visible);
      button.classList.toggle('pointer-events-none', !visible);
    };

    update();
    window.addEventListener('scroll', update, { passive: true });

    button.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ----------------------------------------------------------------
     9. Current year stamp — <span data-year></span>
  ---------------------------------------------------------------- */
  function initYear() {
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  /* ----------------------------------------------------------------
     Boot
  ---------------------------------------------------------------- */
  function init() {
    initThemeToggle();
    initStickyHeader();
    initMobileMenu();
    initReveal();
    initAccordions();
    initBillingToggle();
    initCopyButtons();
    initBackToTop();
    initYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
