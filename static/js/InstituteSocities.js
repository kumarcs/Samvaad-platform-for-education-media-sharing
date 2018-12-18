
function loadAddSociety()
{
  document.getElementsByClassName("allSocietyBlock")[0].style.display="none";
  document.getElementsByClassName("modifySocietyBlock")[0].style.display="none";
  document.getElementsByClassName("addSocietyBlock")[0].style.display="block";

  document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
  document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
  document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="lightgrey";
}
function loadModifySociety()
{
  document.getElementsByClassName("allSocietyBlock")[0].style.display="none";
  document.getElementsByClassName("addSocietyBlock")[0].style.display="none";
  document.getElementsByClassName("modifySocietyBlock")[0].style.display="block";

  document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="inherit";
  document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
  document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="lightgrey";
}
function loadAllSociety()
{
  document.getElementsByClassName("modifySocietyBlock")[0].style.display="none";
  document.getElementsByClassName("addSocietyBlock")[0].style.display="none";
  document.getElementsByClassName("allSocietyBlock")[0].style.display="block";

  document.getElementsByClassName("leftBodyUlLi")[1].style.backgroundColor="inherit";
  document.getElementsByClassName("leftBodyUlLi")[0].style.backgroundColor="inherit";
  document.getElementsByClassName("leftBodyUlLi")[2].style.backgroundColor="lightgrey";
}