function loadRightVerticalNavbar()
{
	document.getElementsByClassName("rightContent")[0].style.display="none";
	document.getElementsByClassName("right")[0].style.width="0%";
	document.getElementsByClassName('overlappingBlock')[0].style.width="23%";
	document.getElementsByClassName("overlappingBlockContent")[0].style.display="block";
}

function closeRightVerticalNavbar()
{
	document.getElementsByClassName("overlappingBlockContent")[0].style.display="none";
	document.getElementsByClassName("overlappingBlock")[0].style.width="0%";
	document.getElementsByClassName('right')[0].style.width="23%";
	document.getElementsByClassName("rightContent")[0].style.display="block";
}
