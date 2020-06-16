const notification_btn = (status) => {
  let get_notified = document.querySelector("#get_notified");
  let notified = document.querySelector("#notified");
  if (status === "granted") {
    notified.style.display = "block";
    notified.classList.add("has-text-success");
    get_notified.style.display = "none";
  } else if (status === "default") {
    get_notified.style.display = "block";
    notified.style.display = "none";
  } else {
    // blocked
    get_notified.style.display = "none";
    notified.style.display = "block";
    notified.classList.add("has-text-danger");
    notified.addEventListener("mouseover", () => {
      notified.style.cursor = "pointer";
    });
    notified.addEventListener("click", () => {
      window.location.href = "/blocked_notifications";
    });

    notified.innerHTML =
      "You have blocked us. Click Here to Enable Notifications";
  }
};

// local storage should have details of the user while :
// 1. making a appointment ...
