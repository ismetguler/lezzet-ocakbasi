/* ===== Lezzet Ocakbaşı — etkileşim ===== */
(function () {
  "use strict";

  // Yıl
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Navbar scroll efekti
  var nav = document.getElementById("nav");
  function onScroll() {
    if (window.scrollY > 40) nav.classList.add("scrolled");
    else nav.classList.remove("scrolled");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobil menü
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  toggle.addEventListener("click", function () {
    links.classList.toggle("open");
    toggle.classList.toggle("open");
  });
  links.querySelectorAll("a").forEach(function (a) {
    a.addEventListener("click", function () {
      links.classList.remove("open");
      toggle.classList.remove("open");
    });
  });

  // Scroll reveal
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });

  // İstatistik sayaçları (hero görününce)
  var counted = false;
  var hero = document.getElementById("hero");
  var counterIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting && !counted) {
        counted = true;
        document.querySelectorAll(".stat b[data-count]").forEach(function (el) {
          var target = parseFloat(el.getAttribute("data-count"));
          var isFloat = el.getAttribute("data-count").indexOf(".") > -1;
          var pad = el.getAttribute("data-count").length === 2 && !isFloat;
          var dur = 1400, start = performance.now();
          function tick(now) {
            var p = Math.min((now - start) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            var val = target * eased;
            el.textContent = isFloat ? val.toFixed(1) : (pad ? String(Math.floor(val)).padStart(2, "0") : Math.floor(val));
            if (p < 1) requestAnimationFrame(tick);
            else el.textContent = isFloat ? target.toFixed(1) : (pad ? String(target).padStart(2, "0") : target);
          }
          requestAnimationFrame(tick);
        });
      }
    });
  }, { threshold: 0.4 });
  if (hero) counterIO.observe(hero);

  // Menü sekmeleri
  var tabs = document.querySelectorAll(".menu-tab");
  var items = document.querySelectorAll(".menu-item");
  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      tabs.forEach(function (t) { t.classList.remove("active"); });
      tab.classList.add("active");
      var cat = tab.getAttribute("data-cat");
      items.forEach(function (it) {
        it.classList.toggle("hide", it.getAttribute("data-cat") !== cat);
      });
    });
  });
  // Başlangıçta sadece döner göster
  items.forEach(function (it) {
    if (it.getAttribute("data-cat") !== "doner") it.classList.add("hide");
  });

  // Köz partikülleri üret
  var embers = document.querySelector(".embers");
  if (embers && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var count = window.innerWidth < 600 ? 14 : 26;
    for (var i = 0; i < count; i++) {
      var s = document.createElement("span");
      s.style.left = Math.random() * 100 + "%";
      s.style.animationDuration = 6 + Math.random() * 8 + "s";
      s.style.animationDelay = Math.random() * 8 + "s";
      var size = 2 + Math.random() * 4;
      s.style.width = s.style.height = size + "px";
      embers.appendChild(s);
    }
  }
})();
