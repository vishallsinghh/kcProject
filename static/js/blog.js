const body = document.body
const headerbar = document.getElementsByClassName('header')[0]
const initialScroll = window.pageYOffset
// var card = document.getElementById('card')

if (initialScroll > 10) {
  headerbar.style.backdropFilter = 'saturate(180%) blur(20px)'
  headerbar.style.backgroundColor = 'rgba(226, 232, 240, 0.3)'
}

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset
  console.log('weeee')
  if (currentScroll > 10) {
    headerbar.style.backdropFilter = 'saturate(180%) blur(20px)'
    headerbar.style.backgroundColor = 'rgba(226, 232, 240, 0.3)'
  } else {
    headerbar.style.backdropFilter = 'blur(0px)'
    headerbar.style.backgroundColor = 'rgba(226, 232, 240, 0.3)'
  }
})
