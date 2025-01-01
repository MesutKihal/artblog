function currentSlide(n)
{
	if (n > 4)
	{
		n = 1;
	} else if (n < 1)
	{
		n = 4
	}
	let slideImg = document.getElementById(`slideImg${n}`);
	let slideDot = document.getElementById(`dot${n}`);
	for (var i = 1; i <= 4; i++)
	{
		let tempSlide = document.getElementById(`slideImg${i}`);
		let tempDot = document.getElementById(`dot${i}`);
		tempSlide.style.display = "none";
		tempDot.style.opacity = "0.5";
	}
	slideImg.style = "";
	slideDot.style.opacity = "1";
}

function nextSlide()
{
	let slides = document.getElementsByName("slideItem");
	let current = null;
	slides.forEach(slide => {
		if (slide.style.display === "")
		{
			current = slide;
		}
	})
	currentSlide(Number(current.id.slice(-1)) + 1);
}

function prevSlide()
{
	let slides = document.getElementsByName("slideItem");
	let current = null;
	slides.forEach(slide => {
		if (slide.style.display === "")
		{
			current = slide;
		}
	})
	currentSlide(Number(current.id.slice(-1)) - 1);
}

setInterval(nextSlide, 7000);
currentSlide(1);