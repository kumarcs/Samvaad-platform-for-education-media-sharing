function loadUserProfile()
{
	document.getElementsByClassName("changePasswordBlock")[0].style.display="none";
	document.getElementsByClassName("modifyUserBlock")[0].style.display="none";
	document.getElementsByClassName("userProfile")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="lightgrey";
}
function loadModifyUser()
{
	document.getElementsByClassName("changePasswordBlock")[0].style.display="none";
	document.getElementsByClassName("userProfile")[0].style.display="none";
	document.getElementsByClassName("modifyUserBlock")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="lightgrey";
}
function loadChangePassword()
{
	document.getElementsByClassName("userProfile")[0].style.display="none";
	document.getElementsByClassName("modifyUserBlock")[0].style.display="none";
	document.getElementsByClassName("changePasswordBlock")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="lightgrey";
}