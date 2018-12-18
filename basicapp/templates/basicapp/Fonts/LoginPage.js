function login()
{
	var username = document.getElementById("username").value;
	var pass = document.getElementById("password").value;
	//Check for valid login page
	
	if(username == "harry")
	window.location.href="Homepage.html";
	
	if(username == "nitish")
		window.location.href="InstituteAdmin.html";

	if(username == "simran")
		window.location.href="superAdminHomepage.html"
}