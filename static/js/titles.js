var toggleButton = document.getElementById("ln-button");
var myDiv = document.getElementById("lnbar");

toggleButton.addEventListener("click", function () {
    myDiv.classList.toggle("visible");

    if (myDiv.classList.contains("visible")) {
        myDiv.style.display = "block";
        slideDown(myDiv);
    } else {
        slideUp(myDiv);
    }
});

function slideDown(element) {
    element.style.height = "0";
    element.style.overflow = "hidden";
    element.style.display = "block";

    var height = 0;
    var maxHeight = window.innerHeight - 140;
    var duration = 300; // Animation duration in milliseconds
    var startTime = null;

    function animate(timestamp) {
        if (!startTime) startTime = timestamp;

        var progress = timestamp - startTime;
        var percentage = Math.min(progress / duration, 1);
        height = percentage * maxHeight;
        element.style.height = height + "px";

        if (progress < duration) {
            requestAnimationFrame(animate);
        } else {
            element.style.height = "Calc(100vh - 140px);";
        }
    }

    requestAnimationFrame(animate);
}

function slideUp(element) {
    var height = window.innerHeight - 140;
    var duration = 300; // Animation duration in milliseconds
    var startTime = null;

    function animate(timestamp) {
        if (!startTime) startTime = timestamp;

        var progress = timestamp - startTime;
        var percentage = Math.max(1 - progress / duration, 0);
        height = percentage * height;
        element.style.height = height + "px";

        if (progress < duration) {
            requestAnimationFrame(animate);
        } else {
            element.style.display = "none";
        }
    }

    requestAnimationFrame(animate);
}

function checkScreenWidth() {
    if (window.innerWidth > 630) {
        myDiv.style.display = "block";
    } else {
        myDiv.style.display = "none";
    }
}

// Call the function initially
checkScreenWidth();

// Call the function on window resize
window.addEventListener("resize", checkScreenWidth);
