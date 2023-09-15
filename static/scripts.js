function setMode(mode) {
    var mode1 = document.getElementById("mode1");
    var mode2 = document.getElementById("mode2");
    var modeButtons = document.querySelectorAll(".modeButton");

    if (mode === 1) {
        mode1.classList.remove("hidden");
        mode2.classList.add("hidden");
        modeButtons[0].classList.add("selected");
        modeButtons[1].classList.remove("selected");
    } else {
        mode1.classList.add("hidden");
        mode2.classList.remove("hidden");
        modeButtons[0].classList.remove("selected");
        modeButtons[1].classList.add("selected");
    }
}

// form handling
const form = document.querySelector("#mode1-form");
const result = document.querySelector("#result");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    fetch(`http://${document.location.host}/api/v1/predict`, {
        method: "POST",
        body: new FormData(form),
    })
        .then((response) => response.json())
        .then((responseJson) => {
            result.innerHTML = `Given account is <b>${responseJson["result"]}</b>`;
        })
        .catch(function (err) {
            console.log(`Error: ${err}`);
        });

    return false;
});
