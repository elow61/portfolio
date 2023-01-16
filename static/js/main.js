'use_strict';

const toggleElement = function (elem) { elem.classList.toggle('active'); }

const btnArrow = document.querySelector('[data-arrow-down]');
const profile = document.querySelector("[data-aside='profile']");
btnArrow.addEventListener('click', () => {toggleElement(profile);});

// page navigation variables
const navLinks = document.querySelectorAll('[data-nav-link]');
const pages = document.querySelectorAll('[data-page]');
const footer = document.querySelector('footer');
// add event to all nav link
for (let i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', function () {
        for (let i = 0; i < pages.length; i++) {
            if (this.innerHTML.toLowerCase() === pages[i].dataset.page) {
                pages[i].classList.add('active');
                navLinks[i].classList.add('active');
                window.scrollTo(0, 0);
                if (this.innerHTML.toLowerCase() === 'contact') {
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
// const overlay = document.querySelector('section.projects .overlay');

// navProjects.forEach((list) => {
// 	list.addEventListener('mouseover', () => {
// 		let position = list.getBoundingClientRect();
// 		overlay.classList.add('active');
// 		overlay.style.left = position.x + 'px';
// 		overlay.style.top = position.y + 'px';
// 		overlay.style.height = position.height + 'px';
// 		overlay.style.width = position.width + 'px';
// 	});
// 	list.addEventListener('mouseout', () => {
// 		overlay.classList.remove('active');
// 	});
// });


for (let i = 0; i < navProjects.length; i++) {
    navProjects[i].addEventListener('click', function () {
        if (this.dataset.navProject == navProjects[i].dataset.navProject) {
            navProjects[i].classList.add('active');
        } else {
            navProjects[i].classList.remove('active');
        }
        displayProjects(nav=navProjects[i]);
    })
}

displayProjects = function (nav) {
    for (let i = 0; i < projects.length; i++) {
        if (nav.dataset.navProject === projects[i].dataset.project || nav.dataset.navProject === 'all') {
            projects[i].classList.add('active');
            window.scrollTo(0, 0);
        } else {
            projects[i].classList.remove('active');
        }
    }
}