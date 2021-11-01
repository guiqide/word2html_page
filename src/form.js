import mammoth from 'mammoth'
import config from './config'
import _ from 'lodash'

const file = document.querySelector('#file-upload')

const preview = document.querySelector('#preview')

const filebox = document.querySelector('#file-box')

const title = document.querySelector('#title')

const template = _.template(require('./templates/template.shtml'))

function readFileInputEventAsArrayBuffer(event, callback) {
	var file = event.target.files[0];

	var reader = new FileReader();
	
	reader.onload = function(loadEvent) {
			var arrayBuffer = loadEvent.target.result;
			callback(arrayBuffer);
	};
	
	reader.readAsArrayBuffer(file);
}


function displayResult(result) {
	const html = template({
		title: title.value,
		content: result.value
	})
	document.getElementById("preview").innerHTML = html;
	
}

const fileChangeHandler = (event) => {
	readFileInputEventAsArrayBuffer(event, function(arrayBuffer) {
		mammoth.convertToHtml(Object.assign({}, {arrayBuffer: arrayBuffer}, config))
				.then(displayResult)
				.done();
	});
}

file.addEventListener('change', fileChangeHandler)

