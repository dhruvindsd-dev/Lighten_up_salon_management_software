var firebaseConfig = {
  apiKey: "AIzaSyADIG5COZpFunikdaa6M9WOLOhTAdCNlcU",
  authDomain: "testing-pwa-5f25a.firebaseapp.com",
  databaseURL: "https://testing-pwa-5f25a.firebaseio.com",
  projectId: "testing-pwa-5f25a",
  storageBucket: "testing-pwa-5f25a.appspot.com",
  messagingSenderId: "135835589513",
  appId: "1:135835589513:web:e77b56c912dab0bf001f58",
  measurementId: "G-6YP9Z9T5W0",
};
// if ("serviceWorker" in navigator) {
//   navigator.serviceWorker
//     .register("/offline-sw.js")
//     .then(function (registration) {
//       console.log("Registration successful, scope is:", registration.scope);
//     })
//     .catch(function (error) {
//       console.log("Service worker registration failed, error:", error);
//     });
// }
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
let messaging = firebase.messaging();
messaging.usePublicVapidKey(
  "BDwwGV-SNWo4O7nHG6raDK__I0ALnPpv2uOeqe_W7qXciMD8fdwdWQaL_jvFXKAXS-T1hZ5CjnQ6sLb78zVo8RU"
);
// get token and send it to server for evaluation.
const get_firebase_token = () => {
  // initialloy network token is taken from network, then it is retrieved from cache.
  messaging.getToken().then((currentToken) => {
    console.log("[Current Token ]", currentToken);
    localStorage.main_token_item = currentToken;
    //  sending token to the server
    // fetch(`/notification_token_csrf/${currentToken}`).then((result) => {
    //   console.log("[FETCHED RESULT IS ]", result);
    // });
  });
  // Callback fired if Instance ID token is updated.
  messaging.onTokenRefresh(() => {
    messaging.getToken().then((refreshedToken) => {
      // sending token to server using fetch ------
      // fetch(`/notification_token_csrf/${currentToken}`).then((result) => {
      //   console.log("[FETCHED RESULT IS ]", result);
      // });
    });
  });
};

const clould_messaging = () => {
  const notification_status = Notification.permission;
  notification_btn(notification_status);
  if (notification_status === "granted") {
    get_firebase_token();
  }
  if (notification_status === "default") {
    // ask for notification permission
    Notification.requestPermission().then((permission) => {
      clould_messaging();
    });
  }
};

if (
  Notification.permission === "granted" ||
  Notification.permission === "denied"
) {
  clould_messaging();
}

let deferredPrompt;
const addBtn = document.querySelector(".install_pwa");
addBtn.style.display = "none";

window.addEventListener("beforeinstallprompt", (e) => {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  e.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = e;
  // Update UI to notify the user they can add to home screen
  addBtn.style.display = "block";

  addBtn.addEventListener("click", (e) => {
    // hide our user interface that shows our A2HS button
    addBtn.style.display = "none";
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then((choiceResult) => {
      if (choiceResult.outcome === "accepted") {
        console.log("User accepted the A2HS prompt");
      } else {
        console.log("User dismissed the A2HS prompt");
      }
      deferredPrompt = null;
    });
  });
});
