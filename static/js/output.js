const body = document.body
const headerbar = document.getElementById('headerbar')
const initialScroll = window.pageYOffset
const userAgent = navigator.userAgent.match(/firefox|fxios/i)
// var card = document.getElementById('card')

if (initialScroll > 10) {
  headerbar.classList.add('bg-slate-200')
  headerbar.classList.add(`${userAgent ? 'bg-opacity-90' : 'bg-opacity-30'}`)
  headerbar.style.backdropFilter = 'saturate(180%) blur(20px)'
}

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset
  if (currentScroll > 10) {
    headerbar.classList.add('bg-slate-200')
    headerbar.classList.add(`${userAgent ? 'bg-opacity-90' : 'bg-opacity-30'}`)
    headerbar.style.backdropFilter = 'saturate(180%) blur(20px)'
  } else {
    headerbar.classList.remove('bg-slate-200')
    headerbar.classList.remove(
      `${userAgent ? 'bg-opacity-90' : 'bg-opacity-30'}`,
    )
    headerbar.style.backdropFilter = 'blur(0px)'
  }
})

function linkHandler(event) {
  event.stopPropagation()
}

for (let i = 1; i <= 6; i++) {
  const card = document.getElementById(`card${i}`)
  card.addEventListener('click', function (e) {
    e.stopPropagation()
    if (card.classList.contains('card--flipped')) {
      card.classList.add('card--unflip')
      setTimeout(function () {
        card.classList.remove('card--flipped', 'card--unflip')
      }, 500)
    } else {
      card.classList.add('card--flipped')
    }
  })
  card.addEventListener('mouseleave', e => {
    e.stopPropagation()
    if (card.classList.contains('card--flipped')) {
      setTimeout(function () {
        card.classList.add('card--unflip')
        setTimeout(function () {
          card.classList.remove('card--flipped', 'card--unflip')
        }, 500)
      }, 1000)
    }
  })
}
