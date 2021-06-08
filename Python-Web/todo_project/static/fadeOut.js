const x = document.getElementById('roko');
if (x != null) {
    let rokoOpacity = 1;

    setTimeout(() => {
        roko();
    }, 3000);

    function roko() {
        rokoOpacity -= 0.2;
        x.style.opacity = String(rokoOpacity.toFixed(1));

        if (rokoOpacity > 0) {
            setTimeout(() => {
                roko()
            }, 50);
        } else {
            x.remove();
        }
    }

}