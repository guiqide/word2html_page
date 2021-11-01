const filebox = document.querySelector('#file-box')

const dragoverHandler = (event) => {
	event.preventDefault()
}

const dragHandler = (event) => {
	console.log(event)
}

filebox.addEventListener('dragover', dragoverHandler)

filebox.addEventListener('drag', dragHandler)