/*********************************************************************************

	Template Name: Belle - Multipurpose eCommerce Bootstrap4 HTML Template
	Description: A perfect template to build beautiful and unique Glasses websites. It comes with nice and clean design.
	Version: 1.0

**********************************************************************************/

/*************************************************
  1. Preloader Loading
  2. Promotional Bar Header
  3. Currency Show/Hide dropdown  
  4. Language Show/Hide dropdown
  5. Top Links Show/Hide dropdown
  6. Minicart Dropdown
  7. Sticky Header
  8. Search Trigger
  9. Mobile Menu
  10 Slick Slider
	 10.1 Homepage Slideshow 
	 10.2 Product Slider Slick
	 10.3 Product Slider Slick Style2
	 10.4 Product Slider Slick Style3
	 10.5 Product Slider Slick Fullwidth
	 10.6 Product Slider Slick Product Page
	 10.7 Collection Slider Slick
	 10.8 Collection Slider Slick 4 items
	 10.9 Logo Slider Slick
	 10.10 Testimonial Slider Slick
  11. Tabs With Accordian Responsive
  12. Sidebar Categories Level links
  13. Price Range Slider
  14. Color Swacthes
  15. Footer links for mobiles
  16. Site Animation
  17. SHOW HIDE PRODUCT TAG
  18. SHOW HIDE PRODUCT Filters
  19. Timer Count Down
  20. Scroll Top
  21. Height Product Grid Image
  22. Product details slider 2
  23. Product details slider 1
  24. Product Zoom
  25. Product Page Popup
  26. Quantity Plus Minus
  27. Visitor Fake Message
  28. Product Tabs
  29. Promotion / Notification Cookie Bar 
  30. Image to background js
  31. COLOR SWATCH ON COLLECTION PAGE
  32. Related Product Slider
  33. Infinite Scroll js
*************************************************/

(function ($) {
	// Start of use strict
	'use strict';
	
    /*-----------------------------------------
	  1. Preloader Loading ----------------------- 
	  -----------------------------------------*/
	function pre_loader(){
		$("#load").fadeOut();
		$('#pre-loader').delay(0).fadeOut('slow');
	}
	pre_loader();
		
	/*-----------------------------------------
	 2. Promotional Bar Header ------------------
	  -----------------------------------------*/
	function promotional_bar(){
		$(".closeHeader").on('click',function() {
			$(".promotion-header").slideUp();  
			Cookies.set('promotion', 'true', { expires: 1});  
			return false;
		});
	}
	promotional_bar();
	
	/*-----------------------------------------
	 3. Currency Show/Hide dropdown -----------
	  -----------------------------------------*/
	function currency_dropdown(){
		$(".selected-currency").on("click", function() {
		  $("#currencies").slideToggle();      
		});
		$("#currencies li").on("click", function() {
			$(this).parent().slideUp();
		});
	}
	currency_dropdown();
	
	/*-----------------------------------------
	  4. Language Show/Hide dropdown ----------
	  -----------------------------------------*/
	function language_dropdown(){  
		$(".language-dd").on("click", function() {
		  $("#language").slideToggle();      
		});
		$("#language li").on("click", function() {
			$(this).parent().slideUp();
		});
	}
	language_dropdown();
	
	/*-----------------------------------------
	  5. Top Links Show/Hide dropdown ---------
	  -----------------------------------------*/
	  function userlink_dropdown(){  
		$('.top-header .user-menu').on("click", function() {
			if ($(window).width() < 990 ) {
				$(this).next().slideToggle(300);
				$(this).parent().toggleClass("active");
			}
		});
	 }
	 userlink_dropdown();
	 
	 /*-----------------------------------------
	  6. Minicart Dropdown ---------------------
	  ------------------------------------------ */
	  function minicart_dropdown(){
		$(".site-header__cart").on("click", function(i) {
			i.preventDefault();
			$("#header-cart").slideToggle();
		});
		// Hide Cart on document click
		$("body").on("click", function(event ) {
		  var $target = $(event.target);
		  if(!$target.parents().is(".site-cart") && !$target.is(".site-cart")){
			$("body").find("#header-cart").slideUp();
		  }
		});
	  }
	 minicart_dropdown();
	
	/*-----------------------------------------
	  7. Sticky Header ------------------------
	  -----------------------------------------*/
	window.onscroll = function(){ myFunction() };
    function myFunction() {
      if($(window).width()>1199) {
            if($(window).scrollTop()>145){
              $('.header-wrap').addClass("stickyNav animated fadeInDown");                   
            } else {
              $('.header-wrap').removeClass("stickyNav fadeInDown");              
            }
       }
    }
	
	/*-----------------------------------------
	  8. Search Trigger -----------------------
	  ----------------------------------------- */
	function search_bar(){
		$('.search-trigger').on('click', function () {
			const search = $('.search');
	
			if (search.is('.search--opened')) {
				search.removeClass('search--opened');
			} else {
				search.addClass('search--opened');
				$('.search__input')[0].focus();
			}
		});
	}
	search_bar();
	$(document).on('click', function (event) {
		if (!$(event.target).closest('.search, .search-trigger').length) {
			$('.search').removeClass('search--opened');
		}
	});
	
	/*-----------------------------------------
	  9. Mobile Menu --------------------------
	  -----------------------------------------*/
	var selectors = {
      	body: 'body',
      	sitenav: '#siteNav',
      	navLinks: '#siteNav .lvl1 > a',
      	menuToggle: '.js-mobile-nav-toggle',
      	mobilenav: '.mobile-nav-wrapper',
      	menuLinks: '#MobileNav .anm',
      	closemenu: '.closemobileMenu'
	};
     
  	$(selectors.navLinks).each(function(){
        if($(this).attr('href') == window.location.pathname) $(this).addClass('active');
    })
	
  	$(selectors.menuToggle).on("click",function(){
      body: 'body',
      $(selectors.mobilenav).toggleClass("active");
      $(selectors.body).toggleClass("menuOn");
      $(selectors.menuToggle).toggleClass('mobile-nav--open mobile-nav--close');
    });
  
    $(selectors.closemenu).on("click",function(){
      body: 'body',
      $(selectors.mobilenav).toggleClass("active");
      $(selectors.body).toggleClass("menuOn");
      $(selectors.menuToggle).toggleClass('mobile-nav--open mobile-nav--close');
    });
    $("body").on('click', function (event) {
      var $target = $(event.target);
      if(!$target.parents().is(selectors.mobilenav) && !$target.parents().is(selectors.menuToggle) && !$target.is(selectors.menuToggle)){
          $(selectors.mobilenav).removeClass("active");
          $(selectors.body).removeClass("menuOn");
          $(selectors.menuToggle).removeClass('mobile-nav--close').addClass('mobile-nav--open');
      }
    });
	$(selectors.menuLinks).on('click', function(e) {
		e.preventDefault();
		$(this).toggleClass('anm-plus-l anm-minus-l');
		$(this).parent().next().slideToggle();
    });
	
	
	/*-----------------------------------------
	  10.1 Homepage Slideshow -----------------
	  -----------------------------------------*/
	  function home_slider(){
		 $('.home-slideshow').slick({
			dots: false,
			infinite: true,
			slidesToShow: 1,
			slidesToScroll: 1,
			fade: true,
			arrows: true,
			autoplay: true,
			autoplaySpeed: 4000,
			lazyLoad: 'ondemand'
		  });
	  }
	  home_slider();
	
	// Full Size Banner on the Any Screen
	$(window).resize(function() {
		var bodyheight = $(this).height() - 20;
		$(".sliderFull .bg-size").height(bodyheight);
	}).resize();
	
	/*-----------------------------------------
	  10.2 Product Slider Slick ---------------
	  -----------------------------------------*/
	function product_slider(){
	 $('.productSlider').slick({
		dots: false,
		infinite: true,
		slidesToShow: 4,
		slidesToScroll: 1,
		arrows: true,
		responsive: [
		{
		  breakpoint: 1024,
		  settings: {
			slidesToShow: 3,
			slidesToScroll: 1
		  }
		},
		{
		  breakpoint: 600,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 1
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1
		  }
		}
		]
	
	  });
	}
	product_slider();

	/*-----------------------------------------
	  10.3 Product Slider Slick Style2 --------
	  -----------------------------------------*/
	function product_slider1(){
		$('.productSlider-style1').slick({
			dots: false,
			infinite: true,
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			  }
			}
			]
		});
	}
	product_slider1();

	/*-----------------------------------------
	  10.4 Product Slider Slick Style3 --------
	  -----------------------------------------*/
	function product_slider2(){
		$('.productSlider-style2').slick({
			dots: false,
			infinite: true,
			slidesToShow: 5,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			  }
			}
			]
		});
	}
	product_slider2();

	/*-----------------------------------------
	  10.5 Product Slider Slick Fullwidth -----
	  ----------------------------------------- */
	  function product_slider_full(){
		$('.productSlider-fullwidth').slick({
			dots: false,
			infinite: true,
			slidesToShow: 6,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			  }
			}
			]
		});
	  }
	  product_slider_full();

	/*-----------------------------------------
	  10.6 Product Slider Slick Product Page --
	  ----------------------------------------- */
	function product_slider_ppage(){
		$('.productPageSlider').slick({
			dots: false,
			infinite: true,
			slidesToShow: 5,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 4,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 680,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 380,
			  settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			  }
			}
			]
		});
	}
	product_slider_ppage();

	/*-----------------------------------------
	  10.7 Collection Slider Slick ------------
	  ----------------------------------------- */
	function collection_slider(){
		$('.collection-grid').slick({
			dots: false,
			infinite: true,
			slidesToShow: 5,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 4,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			}
			]
		});
	}
	collection_slider();

	/*-----------------------------------------
	  10.8 Collection Slider Slick 4 items ----
	  ----------------------------------------- */	  
	function collection_slider1(){
		$('.collection-grid-4item').slick({
			dots: false,
			infinite: true,
			slidesToShow: 4,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			}
			]
		});
	}
	collection_slider1();

	/*-----------------------------------------
	  10.9 Logo Slider Slick ------------------
	  -----------------------------------------*/
	function logo_slider(){
		$('.logo-bar').slick({
			dots: false,
			infinite: true,
			slidesToShow: 6,
			slidesToScroll: 1,
			arrows: true,
			responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToShow: 4,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 1
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			}
			]
		});
	}
	logo_slider();

	/*-----------------------------------------
	  10.10 Testimonial Slider Slick ----------
	  -----------------------------------------*/
	function testimonial_slider(){
		$('.quotes-slider').slick({
			dots: false,
			infinite: true,
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: true,
		});
	}
	testimonial_slider();
	  
	/*-----------------------------------
	  11. Tabs With Accordian Responsive
	-------------------------------------*/
	$(".tab_content").hide();
	$(".tab_content:first").show();
	
	/* if in tab mode */
	$("ul.tabs li").on('click', function () {
		$(".tab_content").hide();
		var activeTab = $(this).attr("rel"); 
		$("#"+activeTab).fadeIn();		
		
		$("ul.tabs li").removeClass("active");
		$(this).addClass("active");
		
		$(".tab_drawer_heading").removeClass("d_active");
		$(".tab_drawer_heading[rel^='"+activeTab+"']").addClass("d_active");
		
		$('.productSlider').slick('refresh');
	
	});
	/* if in drawer mode */
	$(".tab_drawer_heading").on('click', function () {
		
		$(".tab_content").hide();
		var d_activeTab = $(this).attr("rel"); 
		$("#"+d_activeTab).fadeIn();
		
		$(".tab_drawer_heading").removeClass("d_active");
		$(this).addClass("d_active");
		
		$("ul.tabs li").removeClass("active");
		$("ul.tabs li[rel^='"+d_activeTab+"']").addClass("active");
		
		$('.productSlider').slick('refresh');
	});
	
	$('ul.tabs li').last().addClass("tab_last");
	
	/*-----------------------------------
	  End Tabs With Accordian Responsive
	-------------------------------------*/
	
	/*-----------------------------------
	  12. Sidebar Categories Level links
	-------------------------------------*/
	function categories_level(){
		$(".sidebar_categories .sub-level a").on("click", function() {
			$(this).toggleClass('active');
			$(this).next(".sublinks").slideToggle("slow");
		}); 
	}
	categories_level();
	
	$(".filter-widget .widget-title").on("click", function () {
		$(this).next().slideToggle('300');
		$(this).toggleClass("active");
	});
	
	/*-----------------------------------
	 13. Price Range Slider
	-------------------------------------*/
	// price_filter.js (for example)
function price_slider() {
    // Read initial values from hidden inputs or default to [12, 100]
    let minVal = parseInt($("#id_min_price").val()) || 0;
    let maxVal = parseInt($("#id_max_price").val()) || 5000;

    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 10000,
        values: [minVal, maxVal],
        slide: function(event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        },
        change: function(event, ui) {
            // Update hidden fields so they get submitted to the server
            $("#id_min_price").val(ui.values[0]);
            $("#id_max_price").val(ui.values[1]);
        }
    });

    // Display initial text
    $("#amount").val(
        "$" + $("#slider-range").slider("values", 0) +
        " - $" + $("#slider-range").slider("values", 1)
    );
}

// Initialize the slider on page load
$(document).ready(function() {
    price_slider();
});

	
function color_swatches() {
    $(".swatch-btn1").on("click", function () {
        // Remove the 'checked' class from all swatches
        $(".swatch-btn1").removeClass("checked");

        // Add the 'checked' class to the clicked swatch
        $(this).addClass("checked");

        // Update the corresponding hidden input
        var color = $(this).data("color");
        $(`#color-filter-form input[name="color"][value="${color}"]`).prop("checked", true);

        // Submit the form
        $("#color-filter-form").submit();
    });

    // Reset button behavior
    $("#reset-color-btn").on("click", function (event) {
        event.preventDefault(); // Prevent default form submission
        $(".swatch-btn1").removeClass("checked");
        $("#color-filter-form input[name='color']").prop("checked", false);
        $("#color-filter-form").submit();
    });
}

color_swatches();


function brand_filter() {
	// Submit the form whenever a brand checkbox is toggled
	document.querySelectorAll("#brand-filter-form input[type='checkbox']").forEach(function(checkbox) {
	  checkbox.addEventListener('change', function() {
		document.getElementById("brand-filter-form").submit();
	  });
	});
  
	// Reset: uncheck all, then submit
	const resetBtn = document.getElementById('reset-brand-btn');
	if (resetBtn) {
	  resetBtn.addEventListener('click', function(event) {
		event.preventDefault();
		document.querySelectorAll("#brand-filter-form input[type='checkbox']").forEach(function(cb) {
		  cb.checked = false;
		});
		document.getElementById("brand-filter-form").submit();
	  });
	}
  }
  
  // Initialize
  brand_filter();


  document.querySelectorAll('.buy-now-button').forEach(button => {
    button.addEventListener('click', function () {
        const productSlug = this.dataset.productSlug;
        const quantity = this.dataset.productQuantity;

        fetch('/buy-now/', {
            method: 'POST',
            body: JSON.stringify({
                slug: productSlug,
                quantity: quantity,
            }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken, // Include CSRF token for security
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.redirect_url) {
                window.location.href = data.redirect_url; // Redirect to checkout page
            } else if (data.error) {
                alert(data.error); // Show error message
            }
        });
    });
});


/*-----------------------------------
   15. Size Button Filter
-------------------------------------*/
function size_button_filter() {
    // When a size button is clicked
    $(".swatch-btn").on("click", function() {
      var size = $(this).data("size");
      // Toggle .checked class
      $(this).toggleClass("checked");
      // Update the hidden radio
      var radio = $("input[name='size'][value='" + size + "']");
      // If using radio for single selection, you might want to
      // uncheck all others first. But let's keep your toggle approach:
      radio.prop("checked", $(this).hasClass("checked"));
      // Submit
      $("#size-filter-form").submit();
    });
  }

  // RESET button
  function size_button_reset() {
    $("#reset-size-btn").on("click", function() {
      // Remove checked class from all
      $(".swatch-btn").removeClass("checked");
      // Uncheck all radio
      $("input[name='size']").prop("checked", false);
      // Submit form again
      $("#size-filter-form").submit();
    });
  }

  // Initialize
  $(document).ready(function() {
    size_button_filter();
    size_button_reset();
  });

	
	/*-----------------------------------
	  15. Footer links for mobiles
	-------------------------------------*/
	function footer_dropdown(){
		$(".footer-links .h4").on('click', function () {
			if($(window).width() < 766){
			  $(this).next().slideToggle();
			  $(this).toggleClass("active");
			}
		});  
	}
	footer_dropdown();
	
	//Resize Function 
	var resizeTimer;
	$(window).resize(function (e) {
		clearTimeout(resizeTimer);
		resizeTimer = setTimeout(function () {
			$(window).trigger('delayed-resize', e);
		}, 250);
	});
	$(window).on("load resize",function(e){
		if ($(window).width() > 766 ) {
			$(".footer-links ul").show();
		}
		else {
			$(".footer-links ul").hide();
		}
	});
	
	
	/*-------------------------------
	  16. Site Animation
	----------------------------------*/
	  if($(window).width() < 771) {
		  $('.wow').removeClass('wow');
	  }
	  var wow = new WOW(
	  {
		boxClass:     'wow',      // animated element css class (default is wow)
		animateClass: 'animated', // animation css class (default is animated)
		offset:       0,          // distance to the element when triggering the animation (default is 0)
		mobile:       false,       // trigger animations on mobile devices (default is true)
		live:         true,       // act on asynchronously loaded content (default is true)
		callback:     function(box) {
		  // the callback is fired every time an animation is started
		  // the argument that is passed in is the DOM node being animated
		},
		scrollContainer: null // optional scroll container selector, otherwise use window
	  }
	);
	wow.init();
	
  	/*-------------------------------
	  17. SHOW HIDE PRODUCT TAG
	----------------------------------*/
	$(".product-tags li").eq(10).nextAll().hide(); 
	$('.btnview').on('click', function () {
	$(".product-tags li").not('.filter--active').show();
	 $(this).hide();
	});
	
  	/*-------------------------------
	  18. SHOW HIDE PRODUCT Filters
	----------------------------------*/
    $('.btn-filter').on("click", function() {
       $(".filterbar").toggleClass("active");
    });
    $('.closeFilter').on("click", function() {
      $(".filterbar").removeClass("active");
    });
  	// Hide Cart on document click
    $("body").on('click', function (event) {
      var $target = $(event.target);
      if(!$target.parents().is(".filterbar") && !$target.is(".btn-filter")){
        $(".filterbar").removeClass("active");
      }
    });
	
	/*-------------------------------
	 19. Timer Count Down
	----------------------------------*/
	$('[data-countdown]').each(function () {
		var $this = $(this),
			finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function (event) {
			$this.html(event.strftime('<span class="ht-count days"><span class="count-inner"><span class="time-count">%-D</span> <span>Days</span></span></span> <span class="ht-count hour"><span class="count-inner"><span class="time-count">%-H</span> <span>HR</span></span></span> <span class="ht-count minutes"><span class="count-inner"><span class="time-count">%M</span> <span>Min</span></span></span> <span class="ht-count second"><span class="count-inner"><span class="time-count">%S</span> <span>Sc</span></span></span>'));
		});
	});
	
	/*-------------------------------
	 20.Scroll Top ------------------
	---------------------------------*/
	function scroll_top(){
		$("#site-scroll").on("click", function() {
			$("html, body").animate({ scrollTop: 0 }, 1000);
				return false;
		}); 
	}
	scroll_top();
	
	$(window).scroll(function(){    
		if($(this).scrollTop()>300){
		  $("#site-scroll").fadeIn();
		} else {
		   $("#site-scroll").fadeOut();
		}
	});
	
	/*-------------------------------
	  21. Height Product Grid Image
	----------------------------------*/
	function productGridView() {
	  var gridRows = []; 
	  var tempRow = [];
	  productGridElements = $('.grid-products .item');
	  productGridElements.each(function (index) {
		if ($(this).css('clear') != 'none' && index != 0) {
		  gridRows.push(tempRow);
		  tempRow = []; 
		}
		tempRow.push(this);
	
		if (productGridElements.length == index + 1) {
		  gridRows.push(tempRow);
		}
	  });
	
	  $.each(gridRows, function () {
		var tallestHeight = 0;
		var tallestHeight1 = 0;
		$.each(this, function () {
		  $(this).find('.product-image > a').css('height', '');
		  elHeight = parseInt($(this).find('.product-image').css('height'));
		  if (elHeight > tallestHeight) { tallestHeight = elHeight; }
		});
	
		$.each(this, function () {
		  if($(window).width() > 768) {
			$(this).find('.product-image > a').css('height', tallestHeight);
		  }
		});
	  });
	}
	
	/*----------------------------
       22. Product details slider 2
    ------------------------------ */
	function product_thumb(){
		$('.product-dec-slider-2').slick({
			infinite: true,
			slidesToShow: 5,
			vertical: true,
			slidesToScroll: 1,
			centerPadding: '60px'
		});
	}
	product_thumb();
	
	/*----------------------------
       23. Product details slider 1
    ------------------------------ */
	function product_thumb1(){
		$('.product-dec-slider-1').slick({
			infinite: true,
			slidesToShow: 6,
			stageMargin: 5,
			slidesToScroll: 1
		});
	}
	product_thumb1();
	
	/*--------------------------
      24. Product Zoom
	---------------------------- */
	function product_zoom(){
		$(".zoompro").elevateZoom({
			gallery: "gallery",
			galleryActiveClass: "active",
			zoomWindowWidth: 300,
			zoomWindowHeight: 100,
			scrollZoom: false,
			zoomType: "inner",
			cursor: "crosshair"
		});
	}
	product_zoom();
	
	/*--------------------------
      25. Product Page Popup ---
	---------------------------- */
    function video_popup(){
		if($('.popup-video').length){
			$('.popup-video').magnificPopup({
				type: 'iframe',
				mainClass: 'mfp-fade',
				removalDelay: 160,
				preloader: false,
				fixedContentPos: false
			});
		}
	}
	video_popup();
	
	function size_popup(){
		$('.sizelink').magnificPopup({
			type:'inline',
			midClick: true
		});
	}
	size_popup();
	
	function inquiry_popup(){
		$('.emaillink').magnificPopup({
			type:'inline',
			midClick: true
		});
	}
	inquiry_popup();
	

/*----------------------------------
  Quantity Plus Minus in Cart
------------------------------------*/
function qnt_incre() {
    $(document).on("click", ".qtyBtn", function () {
        const qtyField = $(this).closest(".qtyField").find(".qty");
        const oldValue = parseInt(qtyField.val());
        let newVal = oldValue;

        // Update quantity based on button clicked
        if ($(this).hasClass("plus")) {
            newVal += 1;
        } else if ($(this).hasClass("minus") && oldValue > 1) {
            newVal -= 1;
        }

        // Set the updated value in the input field
        qtyField.val(newVal);

        // Get item ID from the row
        const itemId = $(this).closest("tr").data("item-id");

        // Send AJAX request to update the backend
        $.ajax({
            url: "/update-cart-item/",
            type: "POST",
            data: {
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
                item_id: itemId,
                quantity: newVal,
            },
            success: function (response) {
                // Update subtotal and total price in DOM
                $(`#subtotal-${itemId}`).text(response.subtotal.toFixed(2));
                $("#total-price").text(response.total_price.toFixed(2));
            },
            error: function (xhr, status, error) {
                console.error("Error updating cart:", error);
            },
        });

        console.log("Updated Quantity in Input Field:", newVal);
    });
}
qnt_incre();




// /*----------------------------------
//   Add to Cart Functionality
// ------------------------------------*/
// $(".product-form__cart-submit").on("click", function () {
//     var productSlug = $(this).data("product-slug");

//     // Fetch the updated quantity directly from the input field
//     var quantity = parseInt($("#Quantity").val());  // Get the value from the input field

//     // Debugging: Log the raw quantity value just before sending
//     console.log("Before sending, Raw Quantity Field Value:", $("#Quantity").val());
//     console.log("Sending quantity:", quantity);

//     var color = $("input[name='color']:checked").val();
//     var size = $("input[name='size']:checked").val();

//     // Ensure quantity is valid
//     if (!quantity || quantity < 1) {
//         alert("Please select a valid quantity.");
//         return;
//     }

//     if (!color || !size) {
//         alert("Please select both color and size.");
//         return;
//     }

//     // Debugging: Log the data to be sent
//     console.log("Sending data to backend:", {
//         csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
//         slug: productSlug,
//         quantity: quantity,
//         color: color,
//         size: size
//     });

//     // Proceed with the AJAX request
//     $.ajax({
//         url: "/add-to-cart/",
//         type: "POST",
//         data: {
//             csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
//             slug: productSlug,
//             quantity: quantity,
//             color: color,
//             size: size,
//         },
//         success: function (response) {
//             alert(response.message + ". Quantity: " + response.quantity);
//         },
//         error: function (xhr, status, error) {
//             alert("Something went wrong. Please try again.");
//         },
//     });
// });

/*----------------------------------
  Add to Cart Functionality
------------------------------------*/
$(".product-form__cart-submit").on("click", function () {
    var productSlug = $(this).data("product-slug");

    // Fetch the updated quantity directly from the input field
    var quantity = parseInt($("#Quantity").val());

    console.log("Before sending, Raw Quantity Field Value:", $("#Quantity").val());
    console.log("Sending quantity:", quantity);

    var color = $("input[name='color']:checked").val();
    var size = $("input[name='size']:checked").val();

    // Ensure quantity is valid
    if (!quantity || quantity < 1) {
        alert("Please select a valid quantity.");
        return;
    }

    if (!color || !size) {
        alert("Please select both color and size.");
        return;
    }

    console.log("Sending data to backend:", {
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        slug: productSlug,
        quantity: quantity,
        color: color,
        size: size
    });

    // Proceed with the AJAX request
    $.ajax({
        url: "/add-to-cart/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            slug: productSlug,
            quantity: quantity,
            color: color,
            size: size,
        },
        success: function (response) {
            alert(response.message + ". Quantity: " + response.quantity);
        },
        error: function (xhr, status, error) {
            alert("Something went wrong. Please try again.");
        },
    });
});

/*----------------------------------
  Buy Now Functionality
------------------------------------*/
$(".shopify-payment-button__button").on("click", function () {
    var productSlug = $(".product-form__cart-submit").data("product-slug");

    // Fetch the updated quantity directly from the input field
    var quantity = parseInt($("#Quantity").val());

    console.log("Before sending, Raw Quantity Field Value:", $("#Quantity").val());
    console.log("Sending quantity:", quantity);

    var color = $("input[name='color']:checked").val();
    var size = $("input[name='size']:checked").val();

    // Ensure quantity is valid
    if (!quantity || quantity < 1) {
        alert("Please select a valid quantity.");
        return;
    }

    if (!color || !size) {
        alert("Please select both color and size.");
        return;
    }

    console.log("Sending data to backend for Buy Now:", {
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        slug: productSlug,
        quantity: quantity,
        color: color,
        size: size
    });

    // Proceed with the AJAX request
    $.ajax({
        url: "/buy-now/", // Separate endpoint for Buy Now
        type: "POST",
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            slug: productSlug,
            quantity: quantity,
            color: color,
            size: size,
        },
        success: function (response) {
            if (response.redirect_url) {
                // Redirect to the checkout page
                window.location.href = response.redirect_url;
            } else {
                alert("Unable to proceed. Please try again.");
            }
        },
        error: function (xhr, status, error) {
            alert("Something went wrong. Please try again.");
        },
    });
});



// document.getElementById("checkout-form").addEventListener("submit", function (event) {
//     const termsCheckbox = document.getElementById("cartTearm");

//     if (!termsCheckbox.checked) {
//         event.preventDefault(); // Stop form submission
//         alert("Please agree to the terms and conditions before proceeding.");
//     }
// });


	
	/*----------------------------------
	  27. Visitor Fake Message
	------------------------------------*/
    var userLimit = $(".userViewMsg").attr('data-user'),
        userTime = $(".userViewMsg").attr('data-time');
    $(".uersView").text(Math.floor((Math.random() * userLimit)));
    setInterval(function(){
    	$(".uersView").text(Math.floor((Math.random() * userLimit)));
	}, userTime);

	/*----------------------------------
	  28. Product Tabs
	------------------------------------*/
	$(".tab-content").hide();
	$(".tab-content:first").show();
	/* if in tab mode */
	$(".product-tabs li").on('click', function () {
		$(".tab-content").hide();
		var activeTab = $(this).attr("rel"); 
		$("#"+activeTab).fadeIn();		
		
		$(".product-tabs li").removeClass("active");
		$(this).addClass("active");
		
		$(this).fadeIn();
      	if($(window).width()<767) {
          var tabposition = $(this).offset();
          $("html, body").animate({ scrollTop: tabposition.top }, 700);
        }
	});
    
    $('.product-tabs li:first-child').addClass("active");
	$('.tab-container h3:first-child + .tab-content').show();
	
	/* if in drawer mode */
	$(".acor-ttl").on("click", function() {
		$(".tab-content").hide();
		var activeTab = $(this).attr("rel"); 
		$("#"+activeTab).fadeIn();
		
		$(".acor-ttl").removeClass("active");
		$(this).addClass("active");
	});

    
    $(".reviewLink").on('click', function(e){
      e.preventDefault();
        $(".product-tabs li").removeClass("active");
      	$(".reviewtab").addClass("active");
        var tab = $(this).attr("href");
        $(".tab-content").not(tab).css("display", "none");
        $(tab).fadeIn();
      	var tabposition = $("#tab2").offset();
      	if($(window).width()<767) {
          $("html, body").animate({ scrollTop: tabposition.top-50 }, 700);
        } else{
          $("html, body").animate({ scrollTop: tabposition.top-80 }, 700);
        }
    });
	
	/*--------------------------------------
	  29. Promotion / Notification Cookie Bar 
	  -------------------------------------- */
	  function cookie_promo(){
		  if(Cookies.get('promotion') != 'true') {   
			 $(".notification-bar").show();         
		  }
		  $(".close-announcement").on('click',function() {
			$(".notification-bar").slideUp();  
			Cookies.set('promotion', 'true', { expires: 1});  
			return false;
		  });
	  }
	  cookie_promo();
	 /* --------------------------------------
	 	End Promotion / Notification Cookie Bar 
	 -------------------------------------- */
	 
	 /* --------------------------------------
	 	30. Image to background js
	 -------------------------------------- */
    $(".bg-top" ).parent().addClass('b-top');
    $(".bg-bottom" ).parent().addClass('b-bottom');
    $(".bg-center" ).parent().addClass('b-center');
    $(".bg-left" ).parent().addClass('b-left');
    $(".bg-right" ).parent().addClass('b-right');
    $(".bg_size_content").parent().addClass('b_size_content');
    $(".bg-img").parent().addClass('bg-size');
    $(".bg-img.blur-up" ).parent().addClass('');
    jQuery('.bg-img').each(function() {

        var el = $(this),
            src = el.attr('src'),
            parent = el.parent();

        parent.css({
            'background-image': 'url(' + src + ')',
            'background-size': 'cover',
            'background-position': 'center',
            'background-repeat': 'no-repeat'
        });

        el.hide();
    });
	/* --------------------------------------
	 	End Image to background js
	 -------------------------------------- */
	
	/*----------------------------------
	32. Related Product Slider ---------
	------------------------------------*/
	function related_slider(){
		$('.related-product .productSlider').slick({
		  dots: false,
		  infinite: true,
		  item: 5,
		  slidesToScroll: 1,
		  responsive: [
			{
			  breakpoint: 1024,
			  settings: {
				slidesToScroll: 1,
			  }
			},        
			{
			  breakpoint: 767,
			  settings: {
				slidesToScroll: 1,
			  }
			}
		  ]
		});
	}
	related_slider();
	/*----------------------------------
	  End Related Product Slider
	  ------------------------------------*/
	
	/*-----------------------------------
	  33. Infinite Scroll js
	  -------------------------------------*/
	function load_more(){
        $(".product-load-more .item").slice(0, 8).show();
        $(".loadMore").on('click', function (e) {
            e.preventDefault();
            $(".product-load-more .item:hidden").slice(0, 4).slideDown();
            if ($(".product-load-more .item:hidden").length == 0) {
                $(".infinitpagin").html('<div class="btn loadMore">no more products</div>');
            }
        });
    }
	load_more();
	
	function load_more_post(){
        $(".blog--grid-load-more .article").slice(0, 3).show();
        $(".loadMorepost").on('click', function (e) {
            e.preventDefault();
            $(".blog--grid-load-more .article:hidden").slice(0, 1).slideDown();
            if ($(".blog--grid-load-more .article:hidden").length == 0) {
                $(".loadmore-post").html('<div class="btn loadMorepost">No more Blog Post</div>');
            }
        });
    }
	load_more_post();
	/*-----------------------------------
	  End Infinite Scroll js
	  -------------------------------------*/
	

})(jQuery);
