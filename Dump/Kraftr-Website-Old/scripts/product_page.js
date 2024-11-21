
const photoContainers = document.querySelectorAll('.photo-container');
photoContainers.forEach((container) => {
  container.addEventListener('mouseenter', function() {
    const video = this.querySelector('.video1');
    video.style.opacity = 1;
    video.play();
  });


  container.addEventListener('mouseleave', function() {
    const video = this.querySelector('.video1');
    video.style.opacity = 0; 
    video.pause(); 
  });
});
