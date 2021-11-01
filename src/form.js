import mammoth from 'mammoth'
import options from './options'
import _ from 'lodash'
import iconv from 'iconv-lite'

const fileDOM = document.querySelector('#file-upload')

const preview = document.querySelector('#preview')

const title = document.querySelector('#title')

const formDOM = document.querySelector('#form')

const url = document.querySelector('#url')

const template = _.template(require('./templates/template.shtml'))

// 将上传的文件读到buffer中
function readFileInputEventAsArrayBuffer(dom, callback) {
	var file = dom.files[0];

	var reader = new FileReader();
	
	reader.onload = function(loadEvent) {
			var arrayBuffer = loadEvent.target.result;
			callback(arrayBuffer);
	};
	
	reader.readAsArrayBuffer(file);
}


// 在预览区展示
function displayResult(result) {
	const html = template({
		title: title.value,
		content: result.value
	})
	document.getElementById("preview").innerHTML = html;
	
}

// 监听文件变化
const fileChangeHandler = (event) => {
	readFileInputEventAsArrayBuffer(event.target, function(arrayBuffer) {
		// 拿到buffer数组欧进行转换
		mammoth.convertToHtml({arrayBuffer: arrayBuffer}, options)
				.then(displayResult)
				.done();
	});
}

/* --------------- 下载 ----------------- */
export function createAndDownloadBlobFile(body, filename, extension = 'pdf') {
  const blob = new Blob([body]);
  const fileName = `${filename}.${extension}`;
  
	const link = document.createElement('a');
	// Browsers that support HTML5 download attribute
	if (link.download !== undefined) {
		const url = URL.createObjectURL(blob);
		link.setAttribute('href', url);
		link.setAttribute('download', fileName);
		link.style.visibility = 'hidden';
		document.body.appendChild(link);
		link.click();
		document.body.removeChild(link);
	}
}

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=gbk,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

const saveResult = (result) => {
	const title = formDOM.elements['title'].value
	const urlName = formDOM.elements['url-name'].value
	const filLoader = formDOM.elements['file-upload'].files[0]

	const html = template({
		title: title,
		content: result.value
	})

	// const buf = iconv.encode(html, 'GBK')
	// console.log(buf)

	// createAndDownloadBlobFile()
	download(`${urlName}.shtml`, html)
}

const fileSaveHandler = (dom) => {
	readFileInputEventAsArrayBuffer(dom, function(arrayBuffer) {
		// 拿到buffer数组欧进行转换
		mammoth.convertToHtml({arrayBuffer: arrayBuffer}, options)
				.then(saveResult)
				.done();
	});
}

const submitHandler = (event) => {
	event.preventDefault();
	console.log(event)
	const form = event.target
	
	const fileDom = form.elements['file-upload']
	
	fileSaveHandler(fileDom)
}

formDOM.addEventListener('submit', submitHandler, false);
fileDOM.addEventListener('change', fileChangeHandler)

