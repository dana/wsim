window.onload = function () {
    const canvas = document.getElementById("canvas-element");
    const ctx = canvas.getContext("2d");

    const gridSize = 100;
    const circles = [];

    const camera = {
        x: 0,
        y: 0,
        zoom: 1
    };

    let isDragging = false;
    let lastMouseX = 0;
    let lastMouseY = 0;

    // Generate circle data once
    function setup() {
        const containerWidth = canvas.width;
        const containerHeight = canvas.height;
        const cellWidth = containerWidth / gridSize;
        const cellHeight = containerHeight / gridSize;
        const radius = Math.min(cellWidth, cellHeight) / 2 - 1;

        for (let row = 0; row < gridSize; row++) {
            for (let col = 0; col < gridSize; col++) {
                circles.push({
                    row,
                    col,
                    radius,
                    hue: Math.random() * 360
                });
            }
        }
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.translate(camera.x, camera.y);
        ctx.scale(camera.zoom, camera.zoom);

        const cellWidth = canvas.width / gridSize;
        const cellHeight = canvas.height / gridSize;

        circles.forEach(circle => {
            const x = circle.col * cellWidth + cellWidth / 2;
            const y = circle.row * cellHeight + cellHeight / 2;

            ctx.beginPath();
            ctx.arc(x, y, circle.radius, 0, 2 * Math.PI);
            ctx.fillStyle = "hsl(" + circle.hue + ", 100%, 50%)";
            ctx.fill();
            ctx.closePath();
        });

        ctx.restore();
    }

    canvas.addEventListener('mousedown', (e) => {
        isDragging = true;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
    });

    canvas.addEventListener('mouseup', () => {
        isDragging = false;
    });

    canvas.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const deltaX = e.clientX - lastMouseX;
        const deltaY = e.clientY - lastMouseY;
        camera.x += deltaX;
        camera.y += deltaY;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
        draw();
    });

    canvas.addEventListener('wheel', (e) => {
        e.preventDefault();
        const zoomFactor = 1.1;
        const mouseX = e.clientX - canvas.offsetLeft;
        const mouseY = e.clientY - canvas.offsetTop;

        const worldX = (mouseX - camera.x) / camera.zoom;
        const worldY = (mouseY - camera.y) / camera.zoom;

        if (e.deltaY < 0) {
            // Zoom in
            camera.zoom *= zoomFactor;
        } else {
            // Zoom out
            camera.zoom /= zoomFactor;
        }

        camera.x = mouseX - worldX * camera.zoom;
        camera.y = mouseY - worldY * camera.zoom;

        draw();
    });

    setup();
    draw();
};
