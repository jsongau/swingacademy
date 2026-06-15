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

  /* ---- Coach matching quiz ---- */
  (function () {
    var quiz = document.getElementById("coach-quiz");
    if (!quiz) return;

    var COACHES = [
      { name: "Hitting Specialist",     tags: ["hitting","tryout","confidence"], city: "Chino Hills",        status: "featured", note: "Bat control, contact & confidence, ages 9–14." },
      { name: "Pitching Coach",         tags: ["pitching"],                       city: "Chino / Diamond Bar", status: "verified", note: "Mechanics, arm care & command. Travel-ball experience." },
      { name: "Catching & Fielding",    tags: ["catching"],                       city: "Walnut",             status: "public",   note: "Youth catching and fielding instruction." },
      { name: "Strength & Speed",       tags: ["strength","hitting","confidence"],city: "Rancho Cucamonga",   status: "verified", note: "Plyometrics, rotational power & sprint mechanics." },
      { name: "Travel Ball Coach",      tags: ["tryout","confidence"],            city: "Yorba Linda",        status: "public",   note: "Youth development & tryout preparation." },
      { name: "Hitting & Tryout Prep",  tags: ["hitting","tryout"],               city: "Corona",             status: "featured", note: "10-session plan with final evaluation." }
    ];
    var BADGE = {
      featured: ['badge--featured','Featured Coach'],
      verified: ['badge--verified','Verified Coach'],
      public:   ['badge--public','Public Listing']
    };
    var LABELS = { 1:"Player goal", 2:"Player info", 3:"Training preference", 4:"Budget", 5:"Your matches" };

    var state = { step: 1, goal: "", tag: "hitting", info: {}, pref: "", budget: "", course: false };
    var panes = quiz.querySelectorAll(".q-pane");
    var bar = quiz.querySelector("#q-bar"),
        stepLbl = quiz.querySelector("#q-step"),
        nameLbl = quiz.querySelector("#q-label");

    function show(step) {
      state.step = step;
      panes.forEach(function (p) { p.hidden = (+p.getAttribute("data-pane") !== step); });
      bar.style.width = (step * 20) + "%";
      stepLbl.textContent = "Step " + step + " of 5";
      nameLbl.textContent = LABELS[step];
      if (step === 5) render();
      quiz.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    quiz.addEventListener("click", function (e) {
      var nextBtn = e.target.closest("[data-next]");
      var backBtn = e.target.closest("[data-back]");
      var restart = e.target.closest("[data-restart]");

      if (restart) { state = { step:1, goal:"", tag:"hitting", info:{}, pref:"", budget:"", course:false }; show(1); return; }
      if (backBtn) { show(Math.max(1, state.step - 1)); return; }
      if (!nextBtn) return;

      var key = nextBtn.getAttribute("data-key");
      if (key === "goal")   { state.goal = nextBtn.getAttribute("data-val"); state.tag = nextBtn.getAttribute("data-tag"); show(2); }
      else if (key === "info") {
        state.info = {
          age: (quiz.querySelector("#q-age").value || "any age"),
          pos: (quiz.querySelector("#q-pos").value || "any position"),
          city: (quiz.querySelector("#q-city").value || "your area")
        };
        show(3);
      }
      else if (key === "pref")   { state.pref = nextBtn.getAttribute("data-val"); state.course = nextBtn.getAttribute("data-course") === "1"; show(4); }
      else if (key === "budget") { state.budget = nextBtn.getAttribute("data-val"); show(5); }
    });

    function render() {
      var matches = COACHES.filter(function (c) { return c.tags.indexOf(state.tag) > -1; });
      if (!matches.length) matches = COACHES.filter(function (c) { return c.status === "featured"; });
      matches = matches.slice(0, 3);

      quiz.querySelector("#q-summary").innerHTML =
        "Goal: <strong>" + state.goal + "</strong> · " + state.info.age +
        " · " + state.info.pos + " · near <strong>" + state.info.city + "</strong>" +
        (state.pref ? " · " + state.pref : "") + (state.budget ? " · " + state.budget : "");

      quiz.querySelector("#q-results").innerHTML = matches.map(function (c) {
        var b = BADGE[c.status];
        var cta = c.status === "public"
          ? '<a class="btn btn--ghost btn--sm" href="coach-claim.html">Claim this listing</a>'
          : '<a class="btn btn--primary btn--sm" href="#">Request booking</a>';
        return '<div class="card"><div class="card__body" style="padding:18px">' +
          '<div class="flex items-center" style="justify-content:space-between;gap:8px">' +
          '<h3 style="margin:0;font-size:1.15rem">' + c.name + '</h3>' +
          '<span class="badge ' + b[0] + ' badge--dot">' + b[1] + '</span></div>' +
          '<p class="text-muted" style="margin:.35rem 0">' + c.city + ' — ' + c.note + '</p>' +
          '<div class="pill-row">' + cta + ' <a class="btn btn--ghost btn--sm" href="#">View profile</a></div>' +
          '</div></div>';
      }).join("");

      var showCourse = state.course || state.pref === "10-session course" || state.goal === "Full development plan";
      quiz.querySelector("#q-course").hidden = !showCourse;
    }

    show(1);
  })();

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
