const links = document.querySelectorAll('a');
links.forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const href = link.href;
    const loadingOverlay = document.getElementById('loading-overlay');

    // Blur effect is applied to the body
    document.body.classList.add('loading');

    loadingOverlay.style.display = 'block';

    // Three dots animation
    let dots = 0;
    const dotInterval = setInterval(() => {
      const loadingText = document.querySelector('.loading-text');
      loadingText.textContent = `Loading${'.'.repeat(dots)}`;
      dots = (dots % 3) + 1;
    }, 150);

    // Navigate to the new page after a short delay
    setTimeout(() => {
      clearInterval(dotInterval);
      loadingOverlay.style.display = 'none';
      document.body.classList.remove('loading');
      window.location.href = href;
    }, 750);
  });
});