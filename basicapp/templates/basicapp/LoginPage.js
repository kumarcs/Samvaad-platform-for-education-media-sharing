function login()
{
	var username = document.getElementById("username").value;
	var pass = document.getElementById("password").value;
	//Check for valid login page
	alert("Homepage.html/"+username);
	window.location.href="Homepage.html/"+username;
}