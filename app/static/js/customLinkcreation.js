
document.getElementById("myChecker").addEventListener("click", function() {
    toggle('custShortUrl');
});

function toggle(obj) {

	var el = document.getElementById(obj);

	el.style.display = (el.style.display != 'none' ? 'none' : '' );

}

if (document.getElementById("myCheck")) {
	document.getElementById("myCheck").addEventListener("click", function() {
	    toggle('customShortUrl');
	});

	function toggle(obj) {

		var el = document.getElementById(obj);

		el.style.display = (el.style.display != 'none' ? 'none' : '' );

	}
}