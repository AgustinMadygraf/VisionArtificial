const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;

document.addEventListener("DOMContentLoaded", () => {
    let but = document.getElementById("but");
    let mediaDevices = navigator.mediaDevices;
    let video = document.getElementById("vid");
    video.muted = true;
    var media;
    but.addEventListener("click", () => {

        // Accessing the user camera and video.
        mediaDevices
            .getUserMedia({
                video: true,
                audio: true,
            })
            .then((stream) => {
                // Changing the source of video to current stream.
                video.srcObject = stream;
                video.addEventListener("loadedmetadata", () => {
                    video.play();
                });
            })
            .catch(alert);
    });
    let printme = {
        call: function(caller, vid, currentTime, e) {
            var img = vid.image;
            console.log("printing:", caller, img.width, img.height, currentTime, e);
        }
    };

    function pick_image() {
        getVideoImage(video, secs, printme);
        let imgCanvas = document.getElementById("image-canvas");
        let vid = videoToImg(video);
        let img = vid.image;
        console.log("image to convert dimensions:", img);
        imgCanvas.replaceChildren(img);
        console.log("image data", vid.data);
    }
    setInterval(pick_image, 3);

    /* let scrshot = document.getElementById("pick");
    scrshot.addEventListener("click", pick_image); */
});

function videoToImg(video) {
    var canvas = document.createElement('canvas');
    canvas.height = video.videoHeight;
    canvas.width = video.videoWidth;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    putLineInCanvas(canvas);
    var img = new Image();
    img.src = canvas.toDataURL();
    return {image: img};
}

function getVideoImage(video, secs, callback) {
  console.log("Take screenshot with", video, secs);
  var me = this;
  video.onloadedmetadata = function() {
    if ('function' === typeof secs) {
      secs = secs(this.duration);
    }
    this.currentTime = Math.min(Math.max(0, (secs < 0 ? this.duration : 0) + secs), this.duration);
    console.log("currentTime", this.currentTime);
    let vid = videoToImg(video);
    img = vid.image;
    callback.call(me, vid, this.currentTime, undefined);
  };

  video.onseeked = function(e) {
    callback.call(me, undefined, this.currentTime, e);
  };

  video.onerror = function(e) {
    callback.call(me, undefined, undefined, e);
  };
}

function putLineInCanvas(canvas) {
    const pos = maxVerticalJumpPixelPos(canvas);
    vertLineInCanvas(canvas, pos.pos);
}

function maxVerticalJumpPixelPos(canvas) {
    const ctx = canvas.getContext('2d');

    let heightMid = Math.floor(canvas.height/2);
    let heightCotas = {lo: heightMid - halfEvalHeight, hi: heightMid + halfEvalHeight};

    let widthMid = Math.floor(canvas.width/2);
    let widthCotas = {lo: widthMid - halfEvalWidth, hi: widthMid + halfEvalWidth};

    let vertAdd = [];
    let horizDiff = [];
    let maxDiff = {diff: -256*3*2*halfEvalHeight, pos: 0};

    for (let x = widthCotas.lo; x < widthCotas.hi; x++) {
        let arr_x = x - widthCotas.lo;
        vertAdd.push(0);
        for (let y = heightCotas.lo; y < heightCotas.hi; y++) {
            let point = ctx.getImageData(x, y, 1, 1).data;
            vertAdd[arr_x] = vertAdd[arr_x] + (point[0]+point[1]+point[2]);
        }
        if (arr_x > 1) {
            horizDiff.push(vertAdd[arr_x] - vertAdd[arr_x-1]);
            if (horizDiff[arr_x-2] > maxDiff.diff) {
                maxDiff.pos = x-1;
                maxDiff.diff = horizDiff[arr_x-2];
            }
        }
    }
    return maxDiff;
}

function vertLineInCanvas(canvas, pos) {
    console.log("Drawing line in position", pos);
    const context = canvas.getContext('2d');
    context.strokeStyle = 'yellow'; // Color of the line
    context.lineWidth = 2; // Width of the line

    // Draw the vertical line
    context.beginPath();
    context.moveTo(pos, 0);
    context.lineTo(pos, canvas.height);
    context.stroke();
}
