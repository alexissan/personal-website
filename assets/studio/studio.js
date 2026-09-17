const menuButton = document.querySelector('.menu-toggle');
const mobileNav = document.querySelector('#mobile-nav');
menuButton.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!expanded));
  mobileNav.hidden = expanded;
});
mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  mobileNav.hidden = true;
  menuButton.setAttribute('aria-expanded', 'false');
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !mobileNav.hidden) {
    mobileNav.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.focus();
  }
});
const form = document.getElementById('brief-form');
if (form) {
const copy = JSON.parse(document.getElementById('contact-copy').textContent);
form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const fields = new FormData(form);
  const name = fields.get('name').trim();
  const message = fields.get('message').trim();
  if (!name || !message) {
    const input = !name ? form.elements.name : form.elements.message;
    input.value = '';
    input.reportValidity();
    return;
  }
  const body = `${copy.emailbody[0]}\n\n${copy.emailbody[1]} ${name}.\n${copy.emailbody[2]} ${fields.get('business').trim() || '—'}.\n\n${copy.emailbody[3]}\n${message}`;
  window.location.href = `mailto:alexis.santos.perez@gmail.com?subject=${encodeURIComponent(copy.subject)}&body=${encodeURIComponent(body)}`;
  document.getElementById('form-status').textContent = copy.status;
});

}
