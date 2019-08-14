function openEntry(evt, entryNumber) {
	//Declare all variables
	var i, tabcontent, tablinks;

	//Get all elements with class="tabcontent" and hide them
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}

	//Get all elements with class="tablinks" and remove the class "active"
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}

	// Show the current tab; and add an active class to the button that opened the tab
	document.getElementById(entryNumber).style.display = "block";
	evt.currentTarget.className += " active";
}

function defaultEntry() {
	//Get the element with id="default" and click on it
	document.getElementById("default").click();
}

addEventListener("load", defaultEntry);

var modalBtns = [...document.querySelectorAll(".button")];
modalBtns.forEach(function(btn){
	btn.onclick = function() {
		var modal = btn.getAttribute('data-modal');
		document.getElementById(modal).style.display = "block";
		}
	});

var closeBtns = [...document.querySelectorAll(".close")];
closeBtns.forEach(function(btn){
btn.onclick = function() {
		var modal = btn.closest('.modal');
		modal.style.display = "none";
}
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	if (event.target.className === "modal") {
		event.target.style.display = "none";
	}
}