function solve(speed, road) {
    let speedLimit;

    switch (road) {
        case 'motorway': speedLimit = 130; break;
        case 'interstate': speedLimit = 90; break;
        case 'city': speedLimit = 50; break;
        case 'residential': speedLimit = 20; break;

    }

    if (speed <= speedLimit) {
        return `Driving ${speed} km/h in a ${speedLimit} zone`;
    }

    let status;
    let speedDiv = speed - speedLimit;

    if (speedDiv <= 20) {
        status = 'speeding';
    }

    else if (speedDiv > 20 && speedDiv <= 40) {
        status = 'excessive speeding';
    }

    else {
        status = 'reckless driving';
    }

    return `The speed is ${speed - speedLimit} km/h faster than the allowed speed of ${speedLimit} - ${status}`;
}

console.log(solve(200, 'motorway'));
