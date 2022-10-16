let clock = () => {
    let date = new Date();
    let hrs = date.getHours();
    let mins = date.getMinutes();
    let secs = date.getSeconds();
    /*
    let period = "AM"

    if (hrs == 0) {
        hrs = 12;
    } else if (hrs >= 12) {
        hrs = hrs - 12;
        period = "PM";
    }
    */

    // Prepend 0 if number is less than 10
    hrs = hrs < 10 ? "0" + hrs : hrs;
    mins = mins < 10 ? "0" + mins : mins;
    secs = secs < 10 ? "0" + secs : secs;

    let time = `${hrs}:${mins}`;
    // let time = `${hrs}:${mins}:${secs}`; // Time with seconds
    // let time = `${hrs}:${mins} ${period}`; // American style
    // let time = `${hrs}:${mins}:${secs} ${period}`; // American style with seconds
    document.getElementById("clock").innerHTML = time;
    setTimeout(clock, 1000); // refreshes every second
};

window.onload = function () {
    clock();
};
