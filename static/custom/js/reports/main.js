
$(document).ready(function () {
  console.warn = (e) => {console.log(`Error ${e} has occured. `)};
  var jobProfile = getProfile(getCookie('user'));
  $("#dailyReportLink").click(function(){
    dailyReportRedirect(jobProfile);
  });
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function getProfile(cookie) {
  const pieces = cookie.split(':');
  const last = pieces.slice(-1)[0]
  return last.replace('"','')
}


function dailyReportRedirect(jobProfile) {
  switch (jobProfile) 
  {
    case "SC":
      window.location = "/./dashboard/daily-reports/Scan-Coordinator/form/";
      break;
  
    default:
      window.location = "/./login/";
  }
}

