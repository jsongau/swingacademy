/* ==========================================================================
   KEMUEL SWING ACADEMY — Global JS
   Nav: desktop mega-menu (hover + keyboard), mobile drawer + accordions.
   No dependencies. Progressive enhancement — links work without JS.
   ========================================================================== */
(function () {
  "use strict";

  /* ---- Mobile drawer toggle ---- */
  var toggle = document.querySelector(".nav__toggle");
  var drawer = document.getElementById("mobile-drawer");
  if (toggle && drawer) {
    toggle.addEventListener("click", function () {
      var open = drawer.getAttribute("data-open") === "true";
      drawer.setAttribute("data-open", String(!open));
      toggle.setAttribute("aria-expanded", String(!open));
      document.body.style.overflow = !open ? "hidden" : "";
    });
  }

  /* ---- Mobile accordions ---- */
  document.querySelectorAll(".acc__head").forEach(function (head) {
    head.addEventListener("click", function () {
      var panel = head.nextElementSibling;
      var open = head.getAttribute("aria-expanded") === "true";
      head.setAttribute("aria-expanded", String(!open));
      if (panel) panel.setAttribute("data-open", String(!open));
    });
  });

  /* ---- Desktop mega-menu: keyboard support (hover handled by CSS) ---- */
  document.querySelectorAll(".nav__item").forEach(function (item) {
    var link = item.querySelector(".nav__link");
    var mega = item.querySelector(".mega");
    if (!link || !mega) return;

    link.addEventListener("click", function (e) {
      // If it's a real navigational link with no submenu intent, let it pass.
      if (link.getAttribute("href") && link.getAttribute("href") !== "#") return;
      e.preventDefault();
      var open = mega.getAttribute("data-open") === "true";
      closeAllMega();
      if (!open) {
        mega.setAttribute("data-open", "true");
        link.setAttribute("aria-expanded", "true");
      }
    });

    item.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closeAllMega(); link.focus(); }
    });
  });

  function closeAllMega() {
    document.querySelectorAll(".mega[data-open='true']").forEach(function (m) {
      m.setAttribute("data-open", "false");
    });
    document.querySelectorAll(".nav__link[aria-expanded='true']").forEach(function (l) {
      l.setAttribute("aria-expanded", "false");
    });
  }

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav__item")) closeAllMega();
  });

  /* ---- Audience toggle (homepage hero & similar) ---- */
  document.querySelectorAll("[data-toggle-group]").forEach(function (group) {
    var btns = group.querySelectorAll("[data-toggle-target]");
    btns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var target = btn.getAttribute("data-toggle-target");
        btns.forEach(function (b) { b.setAttribute("aria-selected", "false"); });
        btn.setAttribute("aria-selected", "true");
        document.querySelectorAll("[data-toggle-panel]").forEach(function (p) {
          p.hidden = p.getAttribute("data-toggle-panel") !== target;
        });
      });
    });
  });

  /* ---- FAQ accordions ---- */
  document.querySelectorAll(".faq__q").forEach(function (q) {
    q.addEventListener("click", function () {
      var a = q.nextElementSibling;
      var open = q.getAttribute("aria-expanded") === "true";
      q.setAttribute("aria-expanded", String(!open));
      if (a) a.setAttribute("data-open", String(!open));
    });
  });

  /* ---- Filter chips (directory pages) ---- */
  document.querySelectorAll("[data-chip-toggle]").forEach(function (c) {
    c.addEventListener("click", function () {
      var pressed = c.getAttribute("aria-pressed") === "true";
      c.setAttribute("aria-pressed", String(!pressed));
    });
  });

  /* ---- Reveal-on-scroll (subtle) ---- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll("[data-reveal]").forEach(function (el) { io.observe(el); });
  }

})();
