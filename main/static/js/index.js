
const latestDiv = document.querySelector('#latest')
const categorizeDiv = document.querySelector('#categorized')

document.addEventListener("DOMContentLoaded", (event) => {
	getData("all")
})


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

function getData(category) 
{
	fetch(`content/${category}`, {
	headers: {
			'Content-Type': 'application/json',
		},
		cache: 'no-store',
	}).then(response => response.json()).then(data => {
		if (category == "all")
		{
			latestDiv.innerText = ""
			createPost("vertical-post", "ver-desc", data[0], latestDiv, "small")
			let horsDiv = document.createElement('div')
			for (var i = 1; i < 4; i++)
			{
				createPost("horizantal-post", "hor-desc", data[i], horsDiv, "small")
			}
			latestDiv.appendChild(horsDiv)
			let eightyDiv = document.createElement('div')
			eightyDiv.style = "width: 80%;"
			
			createSection("music", "موسيقى", eightyDiv, data.slice(4, 6))
			
			// منوعات
			let sidenav = document.createElement('div')
			sidenav.setAttribute('id', 'sidenav')
			let sidenavTitle = document.createElement('div')
			let sidenavH = document.createElement('h2')
			sidenavH.innerText = "منوعات"
			sidenavTitle.appendChild(sidenavH)
			sidenav.appendChild(sidenavTitle)
			for (var i = 0; i < 6; i++)
			{
				createLink(data[i].title, data[i].date, sidenav)
			}
			categorizeDiv.appendChild(eightyDiv)
			categorizeDiv.appendChild(sidenav)
		}
		
	}).catch(error => console.log(error))
}

setInterval(nextSlide, 7000);
currentSlide(1);

function getPost(data)
{
	latestDiv.innerText = ""
	categorizeDiv.innerText = ""
	let eightyDiv = document.createElement('div')
	eightyDiv.style = "width: 80vw;"
	createPost("vertical-post-full", "ver-desc", data, eightyDiv, "full")
	categorizeDiv.appendChild(eightyDiv)
	// أخبار ذات صلة
	let sidenav = document.createElement('div')
	sidenav.setAttribute('id', 'sidenav')
	let sidenavTitle = document.createElement('div')
	let sidenavH = document.createElement('h2')
	sidenavH.innerText = "أخبار ذات صلة"
	sidenavTitle.appendChild(sidenavH)
	sidenav.appendChild(sidenavTitle)
	
	categorizeDiv.appendChild(sidenav)
}

function createPost(postClass, desClass, data, parentDiv, type)
{
	let post = document.createElement('div')
	post.classList.add(postClass)
	let img = document.createElement('img')
	img.src = data.img
	post.appendChild(img)
	let desc = document.createElement('div')
	desc.align = "justify"
	desc.classList.add(desClass)
	let title = document.createElement('h3')
	title.onclick = (event) => {
		getPost(data)
	}
	title.innerText = data.title
	let small = document.createElement('small')
	small.innerText = data.date
	desc.appendChild(title)
	desc.appendChild(small)
	let descp = document.createElement('p')
	if (type == "small")
	{
		descp.innerText = data.description
	} else {
		descp.innerText = data.content
	}
	desc.appendChild(descp)
	post.appendChild(desc)
	parentDiv.appendChild(post)
	return
}

function createLink(title, date, parentDiv)
{
	let div = document.createElement('div')
	let h = document.createElement('h3')
	let small = document.createElement('small')
	h.innerText = title
	small.innerText = date
	div.classList.add('post-link')
	div.appendChild(h)
	div.appendChild(small)
	parentDiv.appendChild(div)
	return 
}

function createSection(category, header, parentDiv, data)
{
	let title = document.createElement('div')
	title.classList.add('section-title')
	let h = document.createElement('h1')
	h.innerText = header
	title.appendChild(h)
	parentDiv.appendChild(title)
	let div = document.createElement('div')
	div.setAttribute('id', "category")
	for (var i = 0; i < data.length; i++)
	{
		createPost("horizantal-small-post", "hor-desc", data[i], div, "small")
	}
	parentDiv.appendChild(div)
}