/*progress bar*/
const scrollIndicator = document.querySelector('.scroll-progress');

window.addEventListener('scroll', () => {
  const windowHeight = window.innerHeight;
  const fullHeight = document.body.clientHeight;
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  const percent = (scrollTop / (fullHeight - windowHeight)) * 100;

  scrollIndicator.style.width = `${percent}%`;
});
