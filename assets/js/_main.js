/* ==========================================================================
   jQuery plugin settings and other scripts
   ========================================================================== */

$(document).ready(function () {
  // Theme: system preference by default, explicit choice wins
  var setTheme = function (theme) {
    var use_theme = theme || localStorage.getItem("theme") || $("html").attr("data-theme") ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var isDark = use_theme === "dark";
    $("html").attr("data-theme", isDark ? "dark" : null);
    if (!isDark) $("html").removeAttr("data-theme");
    $("#theme-toggle")
      .attr("aria-checked", isDark ? "true" : "false")
      .attr("aria-label", isDark ? "Dark theme" : "Light theme");
  };
  setTheme();

  var toggleTheme = function (forced) {
    var next = forced || ($("html").attr("data-theme") === "dark" ? "light" : "dark");
    localStorage.setItem("theme", next);
    setTheme(next);
  };
  $("#theme-toggle").on("click", function () {
    toggleTheme();
    if (window.gtag) gtag("event", "theme_toggle", { theme: $("html").attr("data-theme") || "light" });
  });

  /* Follow the OS if the visitor has never chosen explicitly */
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
    if (!localStorage.getItem("theme")) setTheme(e.matches ? "dark" : "light");
  });

  /* Analytics: name the outbound clicks */
  document.querySelectorAll(".pub-links a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (!window.gtag) return;
      var entry = a.closest(".pub-entry");
      gtag("event", "resource_click", {
        resource_type: a.textContent.trim(),
        publication: entry ? entry.querySelector(".pub-title").textContent.trim() : null
      });
    });
  });

  document.querySelector(".author__contact")?.addEventListener("click", function () {
    if (window.gtag) gtag("event", "contact_click", { method: "linkedin" });
  });

  // These should be the same as the settings in _variables.scss
  const scssLarge = 925; // pixels

  // Sticky footer
  var bumpIt = function () {
    $("body").css("margin-bottom", $(".page__footer").outerHeight(true));
  },
    didResize = false;

  bumpIt();

  $(window).resize(function () {
    didResize = true;
  });
  setInterval(function () {
    if (didResize) {
      didResize = false;
      bumpIt();
    }
  }, 250);

  // FitVids init
  fitvids();

  // Follow menu drop down
  $(".author__urls-wrapper button").on("click", function () {
    $(".author__urls").fadeToggle("fast", function () { });
    $(".author__urls-wrapper button").toggleClass("open");
  });

  // Restore the follow menu if toggled on a window resize
  jQuery(window).on('resize', function () {
    if ($('.author__urls.social-icons').css('display') == 'none' && $(window).width() >= scssLarge) {
      $(".author__urls").css('display', 'block')
    }
  });

  // init smooth scroll, this needs to be slightly more than then fixed masthead height
  $("a").smoothScroll({ offset: -65 });

  // add lightbox class to all image links
  $("a[href$='.jpg'],a[href$='.jpeg'],a[href$='.JPG'],a[href$='.png'],a[href$='.gif']").addClass("image-popup");

  // Magnific-Popup options
  $(".image-popup").magnificPopup({
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      tError: '<a href="%url%">Image #%curr%</a> could not be loaded.',
    },
    removalDelay: 500, // Delay in milliseconds before popup is removed
    // Class that is added to body when popup is open.
    // make it unique to apply your CSS animations just to this exact popup
    mainClass: 'mfp-zoom-in',
    callbacks: {
      beforeOpen: function () {
        // just a hack that adds mfp-anim class to markup
        this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
      }
    },
    closeOnContentClick: true,
    midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
  });

});
