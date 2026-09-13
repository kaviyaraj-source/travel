(function () {
    'use strict';

    /* ===== Navbar scroll effect ===== */
    const navbar = document.getElementById('navbar');
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');

    function handleScroll() {
        navbar.classList.toggle('scrolled', window.scrollY > 60);
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    menuToggle.addEventListener('click', () => {
        menuToggle.classList.toggle('active');
        navLinks.classList.toggle('open');
    });

    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            menuToggle.classList.remove('active');
            navLinks.classList.remove('open');
        });
    });

    /* ===== Hero carousel ===== */
    const slides = document.querySelectorAll('.hero-slide');
    const heroPrev = document.getElementById('heroPrev');
    const heroNext = document.getElementById('heroNext');
    const heroDotsContainer = document.getElementById('heroDots');
    let currentSlide = 0;
    let heroInterval;

    if (slides.length > 0) {
        slides.forEach((_, i) => {
            const dot = document.createElement('button');
            dot.classList.add('hero-dot');
            if (i === 0) dot.classList.add('active');
            dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
            dot.addEventListener('click', () => goToSlide(i));
            heroDotsContainer.appendChild(dot);
        });

        const dots = heroDotsContainer.querySelectorAll('.hero-dot');

        function goToSlide(index) {
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');

            currentSlide = (index + slides.length) % slides.length;

            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');

            resetHeroAnimations();
        }

        function resetHeroAnimations() {
            const activeSlide = slides[currentSlide];
            activeSlide.querySelectorAll('.animate-up').forEach(el => {
                el.style.animation = 'none';
                el.offsetHeight;
                el.style.animation = '';
            });
        }

        function nextSlide() { goToSlide(currentSlide + 1); }
        function prevSlide() { goToSlide(currentSlide - 1); }

        heroNext.addEventListener('click', nextSlide);
        heroPrev.addEventListener('click', prevSlide);

        function startAutoplay() {
            heroInterval = setInterval(nextSlide, 6000);
        }

        function stopAutoplay() {
            clearInterval(heroInterval);
        }

        document.getElementById('hero').addEventListener('mouseenter', stopAutoplay);
        document.getElementById('hero').addEventListener('mouseleave', startAutoplay);
        startAutoplay();
    }

    /* ===== Animated counters ===== */
    const statNumbers = document.querySelectorAll('.stat-number');
    let statsAnimated = false;

    function animateCounter(el) {
        const target = parseFloat(el.dataset.target);
        const isDecimal = el.dataset.decimal === 'true';
        const duration = 2000;
        const start = performance.now();

        function update(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = target * eased;

            el.textContent = isDecimal ? current.toFixed(1) : Math.floor(current).toLocaleString();

            if (progress < 1) {
                requestAnimationFrame(update);
            }
        }

        requestAnimationFrame(update);
    }

    function checkStats() {
        if (statsAnimated) return;
        const statsSection = document.querySelector('.stats');
        if (!statsSection) return;

        const rect = statsSection.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.85) {
            statsAnimated = true;
            statNumbers.forEach(el => animateCounter(el));
        }
    }

    window.addEventListener('scroll', checkStats, { passive: true });
    checkStats();

    /* ===== Scroll reveal ===== */
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    revealElements.forEach(el => revealObserver.observe(el));

    /* ===== Testimonials slider ===== */
    const track = document.getElementById('testimonialTrack');
    const dotsContainer = document.getElementById('testimonialDots');
    const cards = track ? track.querySelectorAll('.testimonial-card') : [];

    if (cards.length > 0) {
        let testimonialIndex = 0;
        let cardsPerView = getCardsPerView();

        function getCardsPerView() {
            if (window.innerWidth <= 768) return 1;
            if (window.innerWidth <= 1024) return 2;
            return 3;
        }

        const maxIndex = () => Math.max(0, cards.length - cardsPerView);

        for (let i = 0; i <= maxIndex(); i++) {
            const dot = document.createElement('button');
            dot.classList.add('testimonial-dot');
            if (i === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToTestimonial(i));
            dotsContainer.appendChild(dot);
        }

        const testimonialDots = dotsContainer.querySelectorAll('.testimonial-dot');

        function goToTestimonial(index) {
            testimonialIndex = Math.min(index, maxIndex());
            const cardWidth = cards[0].offsetWidth + 24;
            track.style.transform = `translateX(-${testimonialIndex * cardWidth}px)`;

            testimonialDots.forEach((d, i) => d.classList.toggle('active', i === testimonialIndex));
        }

        window.addEventListener('resize', () => {
            cardsPerView = getCardsPerView();
            goToTestimonial(Math.min(testimonialIndex, maxIndex()));
        });

        setInterval(() => {
            goToTestimonial(testimonialIndex >= maxIndex() ? 0 : testimonialIndex + 1);
        }, 5000);
    }

    /* ===== Form success message ===== */
    const formSuccess = document.getElementById('formSuccess');
    if (window.location.hash.includes('submitted=1') || window.location.search.includes('submitted=1')) {
        formSuccess.classList.add('show');
        history.replaceState(null, '', '/#contact');
    }

    /* ===== Smooth anchor scrolling offset ===== */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    /* ===== Parallax on about images ===== */
    const aboutImages = document.querySelector('.about-images');
    if (aboutImages) {
        window.addEventListener('scroll', () => {
            const rect = aboutImages.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                const offset = (rect.top - window.innerHeight / 2) * 0.05;
                aboutImages.style.transform = `translateY(${offset}px)`;
            }
        }, { passive: true });
    }
})();
