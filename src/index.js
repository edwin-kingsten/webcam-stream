import "./styles.css";
import io from "socket.io-client";

const canvas = document.querySelector("canvas");
const video = document.querySelector("video");
const ctx = canvas.getContext("2d");

const socket = io("https://web-strmr.tk/"); // TODO: SERVER URL HERE

navigator.mediaDevices.getUserMedia({ video: true, audio: false }).then((d) => {
  console.log(d);
  document.querySelector("video").srcObject = d;
});

var stop = false;
var frameCount = 0;
var fps, fpsInterval, startTime, now, then, elapsed;

startAnimating(1);

function startAnimating(fps) {
  fpsInterval = 1000 / fps;
  then = Date.now();
  startTime = then;
  console.log(startTime);
  animate();
}

function animate() {
  if (stop) {
    return;
  }

  requestAnimationFrame(animate);

  now = Date.now();
  elapsed = now - then;

  if (elapsed > fpsInterval) {
    then = now - (elapsed % fpsInterval);

    if (video.play) {
      var aspect = video.videoHeight / video.videoWidth;
      var wantedWidth = 360;
      var height = Math.round(wantedWidth * aspect);
      canvas.width = wantedWidth;
      canvas.height = height;
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

      // const img = document.querySelector("img");
      // img.src = canvas.toDataURL();

      // console.log(canvas.toDataURL())
      socket.emit("image", { data: canvas.toDataURL() });
      // Here the image is being send
    }

    // var sinceStart = now - startTime;
    // var currentFps = Math.round(1000 / (sinceStart / ++frameCount) * 100) / 100;
  }
}

socket.on('image1', ({data}) => {
  console.log(data.data);
})
