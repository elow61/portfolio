'use_strict';

/**
 * Display or hide an element on HTML DOM by using the class 'active'
 * @param {*} elem The element to display or hide
 */
const toggleElement = function (elem) { elem.classList.toggle('active'); }

/**
 * Manage the display aside profile
 */
const btnArrow = document.querySelector('[data-arrow-down]');
const profile = document.querySelector("[data-aside='profile']");
btnArrow.addEventListener('click', () => {toggleElement(profile);});

/**
 * Manage the main menu and display the different sections
 */
const navLinks = document.querySelectorAll('[data-nav-link]');
const pages = document.querySelectorAll('[data-page]');
const footer = document.querySelector('footer');
// add event to all nav link
for (let i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', function () {
        for (let i = 0; i < pages.length; i++) {
            if (this.dataset.link === pages[i].dataset.page) {
                pages[i].classList.add('active');
                navLinks[i].classList.add('active');
                window.scrollTo(0, 0);
                if (this.dataset.link === 'contact') {
                    footer.classList.add('active');
                } else {
                    footer.classList.remove('active');
                }
            } else {
                pages[i].classList.remove('active');
                navLinks[i].classList.remove('active');
            }
        }
    });
}

// Manage projects
const navProjects = document.querySelectorAll('[data-nav-project]')
const projects = document.querySelectorAll('[data-project]')

for (let i = 0; i < navProjects.length; i++) {
    navProjects[i].addEventListener('click', function () {
        if (this.dataset.navProject == navProjects[i].dataset.navProject) {
            navProjects[i].classList.add('active');
        }
        displayProjects(nav=navProjects[i]);
    })
}
/**
 * Display projects according to the nav link clicked
 * @param {object} nav - nav (project category) clicked
 */
displayProjects = function (nav) {
    for (let i = 0; i < projects.length; i++) {
        // Manage projects
        if (nav.dataset.navProject === projects[i].dataset.project || nav.dataset.navProject === 'all') {
            projects[i].classList.add('active');
            window.scrollTo(0, 0);
        } else {
            projects[i].classList.remove('active');
        }
        // Manage nav projects
        anotherNav = document.querySelectorAll('[data-nav-project]:not([data-nav-project="' + nav.dataset.navProject + '"])');
        for (let i = 0; i < anotherNav.length; i++) {
            anotherNav[i].classList.remove('active');
        }
    }
}
