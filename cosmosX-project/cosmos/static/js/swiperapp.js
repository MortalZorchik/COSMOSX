
const sliderMain = new Swiper('.slider_main', {
	freeMode: true,
	centeredSlides: true,
	mousewheel: true,
	parallax: true,
	breakpoints: {
		0: {
			slidesPerView: 1.1,
			spaceBetween: 20
		},

		601: {
			slidesPerView: 1,
			spaceBetween: 20,
		},
		801:{
			slidesPerView: 1,
			spaceBetween: 20,
		},
		1025:{
			slidesPerView: 2.1,
			spaceBetween: 60,
		},
		1100: {
			slidesPerView: 2.3,
			spaceBetween: 60,
		},
		1200: {
			slidesPerView: 2.5,
			spaceBetween: 60,
		}
	}
})
const sliderBg = new Swiper('.slider_bg', {
	centeredSlides: true,
	parallax: true,
	spaceBetween: 60,
	slidesPerView: 3.5
})
sliderMain.controller.control = sliderBg

document.querySelectorAll('.slider__item').forEach(item => {
	item.addEventListener('click', event => {
		item.classList.toggle('opened')
	})
})

let desc = document.querySelector('.description')
sliderMain.on('slideChange', e => {
		if (document.documentElement.scrollWidth>="1025"){
			sliderMain.activeIndex > 0 ? desc.classList.add('hidden') : desc.classList.remove('hidden')
		}
		if(document.documentElement.scrollWidth<="1025" && desc.classList.contains('hidden')){
			desc.classList.remove('hidden')
		}

})
