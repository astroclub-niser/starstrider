// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
// import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD1lah2Hpp5FmCeQkzwLey8rMUaUfnhCGU",
  authDomain: "starstrider-bb52e.firebaseapp.com",
  projectId: "starstrider-bb52e",
  storageBucket: "starstrider-bb52e.appspot.com",
  messagingSenderId: "1085762459033",
  appId: "1:1085762459033:web:3bbf4ba49fd6f67c932f08",
  measurementId: "G-TLHHY0VGY9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);