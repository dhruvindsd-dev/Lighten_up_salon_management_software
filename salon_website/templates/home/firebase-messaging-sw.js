importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"
);

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
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
let messaging = firebase.messaging();

// background service worker
messaging.setBackgroundMessageHandler((payload) => {
  console.log(
    "[Firebase-messaging-sw.js] Received background message ",
    payload
  );
  // Customize notification here
  const notificationTitle = payload.data.title;
  const notificationOptions = {
    body: payload.data.body,
    // icon: 'ikg /firebase-logo.png'
  };
  // fetch("/token_ver").then((result) => {
  // console.log("[FETCHED RESULT IS ]", result);
  // });

  return self.registration.showNotification(
    notificationTitle,
    notificationOptions
  );
});
