function loadAddInstitute()
{
	document.getElementsByClassName("allInstitutesBlock")[0].style.display="none";
	document.getElementsByClassName("changePasswordBlock")[0].style.display="none";
	document.getElementsByClassName("modifyInstituteBlock")[0].style.display="none";
	document.getElementsByClassName("addInstituteBlock")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[3].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="lightgrey";
}
function loadModifyInstitute()
{
	document.getElementsByClassName("allInstitutesBlock")[0].style.display="none";
	document.getElementsByClassName("changePasswordBlock")[0].style.display="none";
	document.getElementsByClassName("addInstituteBlock")[0].style.display="none";
	document.getElementsByClassName("modifyInstituteBlock")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[3].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="lightgrey";
}
function loadAllInstitute()
{
	document.getElementsByClassName("changePasswordBlock")[0].style.display="none";
	document.getElementsByClassName("modifyInstituteBlock")[0].style.display="none";
	document.getElementsByClassName("addInstituteBlock")[0].style.display="none";
	document.getElementsByClassName("allInstitutesBlock")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[3].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="lightgrey";
}
function loadChangePassword()
{
	document.getElementsByClassName("allInstitutesBlock")[0].style.display="none";
	document.getElementsByClassName("modifyInstituteBlock")[0].style.display="none";
	document.getElementsByClassName("addInstituteBlock")[0].style.display="none";
	document.getElementsByClassName("changePasswordBlock")[0].style.display="block";

	document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
	document.getElementsByClassName("leftBodyUlLi")[3].style.backgroundColor="lightgrey";
}