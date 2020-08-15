$(window).on("load", () => {
  $(".spinner").delay(1000).fadeOut(1000);
});

$(document).ready(() => {
  checkCookie();

  $("#dark").click(() => {
    $("body, html").toggleClass("dark-mode");

    if (getCookie("dark") === "exist") {
      setCookie("dark", "");
    } else {
      setCookie("dark", "exist");
    }
  });
});

function setCookie(cname, cvalue) {
  let d = new Date(); // 3 days
  d.setTime(d.getTime() + 3 * 24 * 60 * 60 * 1000);
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkCookie() {
  if (getCookie("dark") === "exist") {
    $("body, html").addClass("dark-mode");
  } else {
    $("body, html").removeClass("dark-mode");
  }
}
