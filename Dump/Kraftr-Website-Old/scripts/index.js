document.getElementById('myVideo').addEventListener('ended',myHandler,false);
function myHandler(e) {
    console.log('Video ended')
    document.getElementsByClassName('videoContainer')[0].style.width = '95vw'
    document.getElementsByClassName('videoClass')[0].style.width = '95vw'    
    document.getElementsByClassName('splashscreen')[0].style.animation = "lightson 1.25s ease-in both"
    document.getElementsByClassName('splashwindow')[0].style.animation = "fadein 2.25s ease-in both "
    document.getElementsByClassName('herotext')[0].style.color = "var(--fontcolor)"
}

const buttons = document.querySelectorAll("[data-carousel-button]")

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const offset = button.dataset.carouselButton === "next" ? 1 : -1
    const slides = button
      .closest("[data-carousel]")
      .querySelector("[data-slides]")

    const activeSlide = slides.querySelector("[data-active]")
    let newIndex = [...slides.children].indexOf(activeSlide) + offset
    if (newIndex < 0) newIndex = slides.children.length - 1
    if (newIndex >= slides.children.length) newIndex = 0

    slides.children[newIndex].dataset.active = true
    delete activeSlide.dataset.active
  })
})