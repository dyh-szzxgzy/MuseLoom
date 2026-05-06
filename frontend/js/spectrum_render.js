function renderSpectrum(canvasId, bins) {
  const canvas = document.getElementById(canvasId);
  if (!canvas || !bins) {
    return;
  }

  const context = canvas.getContext("2d");
  const width = canvas.width;
  const height = canvas.height;
  context.clearRect(0, 0, width, height);

  const barWidth = width / bins.length;
  bins.forEach((value, index) => {
    const barHeight = Math.max(6, value * height);
    const x = index * barWidth;
    const y = height - barHeight;

    const gradient = context.createLinearGradient(0, y, 0, height);
    gradient.addColorStop(0, "#f6c177");
    gradient.addColorStop(1, "#af5e2c");

    context.fillStyle = gradient;
    context.fillRect(x + 1, y, barWidth - 2, barHeight);
  });
}
