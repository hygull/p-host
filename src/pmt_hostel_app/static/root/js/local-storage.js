if(localStorage){
	if(localStorage.getItem("pmtBoysHostelData")) {
		document.getElementById("pmt-register").style.display = "none";
		document.getElementById("pmt-login").style.display = "none";
		document.getElementById("pmt-logout").style.display = "block";
		document.getElementById("pmt-profile").style.display = "block";
	} else {
		document.getElementById("pmt-register").style.display = "block";
		document.getElementById("pmt-login").style.display = "block";
		document.getElementById("pmt-logout").style.display = "none";
		document.getElementById("pmt-profile").style.display = "none";
	}
} else {
	alert("Your browser does not support localStorage, please upgrade or look for different browser");
}