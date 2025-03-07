// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        const headerOffset = 100;
        const elementPosition = target.offsetTop;
        const offsetPosition = elementPosition - headerOffset;

        window.scrollTo({
            top: offsetPosition,
            behavior: "smooth"
        });
    });
});

// Progress bar animation
const progressBars = document.querySelectorAll('.progress-bar');
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            if (entry.target.classList.contains('progress-bar')) {
                entry.target.style.width = entry.target.getAttribute('data-value') + '%';
            }
        }
    });
}, observerOptions);

// Observe elements
document.querySelectorAll('.fade-up, .progress-bar, .timeline-item').forEach(el => {
    observer.observe(el);
});

// Initialize tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
});

// Typed.js initialization
document.addEventListener('DOMContentLoaded', function() {
    if(document.querySelector('.typed-text')) {
        new Typed('.typed-text', {
            strings: [
                'Backend Development',
                'Data Engineering',
                'Architecture Cloud',
                'Optimisation des Systèmes de Santé'
            ],
            typeSpeed: 50,
            backSpeed: 30,
            backDelay: 2000,
            loop: true
        });
    }
});

// Particle background
particlesJS('particles-js', {
    particles: {
        number: {
            value: 30,
            density: {
                enable: true,
                value_area: 1500
            }
        },
        color: {
            value: ["#0f62fe", "#4589ff", "#78a9ff"]
        },
        shape: {
            type: "circle"
        },
        opacity: {
            value: 0.15,
            random: true,
            anim: {
                enable: true,
                speed: 0.3,
                opacity_min: 0.05,
                sync: false
            }
        },
        size: {
            value: 1.5,
            random: true,
            anim: {
                enable: true,
                speed: 2,
                size_min: 0.1,
                sync: false
            }
        },
        line_linked: {
            enable: true,
            distance: 150,
            color: "#0f62fe",
            opacity: 0.1,
            width: 1
        },
        move: {
            enable: true,
            speed: 0.6,
            direction: "none",
            random: true,
            straight: false,
            out_mode: "out",
            bounce: false,
            attract: {
                enable: true,
                rotateX: 600,
                rotateY: 1200
            }
        }
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: {
                enable: true,
                mode: "grab"
            },
            onclick: {
                enable: true,
                mode: "push"
            },
            resize: true
        },
        modes: {
            grab: {
                distance: 180,
                line_linked: {
                    opacity: 0.25
                }
            },
            push: {
                particles_nb: 1
            }
        }
    },
    retina_detect: true
}); 
