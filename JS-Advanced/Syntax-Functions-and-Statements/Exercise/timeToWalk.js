function solve(steps, lengthOfStep, speed) {
    let distanceMeters = (steps * lengthOfStep);
    let distanceKm = distanceMeters / 1000;

    let timeBreak = Math.floor(distanceMeters / 500);
    let timeMin = (distanceKm / speed) * 60 + timeBreak
    let timeSec = Math.round(timeMin * 60)
    let timeMs = timeSec * 1000

    return new Date(timeMs).toISOString().substr(11, 8);

}

console.log(solve(2564, 0.7, 5.5));