document.addEventListener("DOMContentLoaded", function () {
    timeoutTime = 1000;

    setTimeout(function () {
        document.getElementById('video-container').classList.add('fade-out');
    }, timeoutTime);
});