<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Mini Web Browser</title>
  <style>
    body { font-family: sans-serif; margin: 0; }
    #toolbar { background: #333; color: white; padding: 8px; display: flex; gap: 8px; }
    #toolbar input { flex: 1; padding: 6px; }
    #toolbar button { padding: 6px 12px; }
    #viewer { width: 100%; height: 90vh; border: none; }
  </style>
</head>
<body>
  <div id="toolbar">
    <button onclick="goBack()">⬅️</button>
    <button onclick="goForward()">➡️</button>
    <button onclick="reload()">🔄</button>
    <input id="url" type="text" placeholder="Nhập URL..." />
    <button onclick="navigate()">Đi</button>
  </div>
  <iframe id="viewer"></iframe>

  <script>
    let historyStack = [];
    let currentIndex = -1;

    function navigate() {
      const url = document.getElementById("url").value;
      if (!url) return;
      const fullUrl = url.startsWith("http") ? url : "https://" + url;
      document.getElementById("viewer").src = fullUrl;
      historyStack = historyStack.slice(0, currentIndex + 1);
      historyStack.push(fullUrl);
      currentIndex++;
    }

    function goBack() {
      if (currentIndex > 0) {
        currentIndex--;
        document.getElementById("viewer").src = historyStack[currentIndex];
        document.getElementById("url").value = historyStack[currentIndex];
      }
    }

    function goForward() {
      if (currentIndex < historyStack.length - 1) {
        currentIndex++;
        document.getElementById("viewer").src = historyStack[currentIndex];
        document.getElementById("url").value = historyStack[currentIndex];
      }
    }

    function reload() {
      if (currentIndex >= 0) {
        document.getElementById("viewer").src = historyStack[currentIndex];
      }
    }
  </script>
</body>
</html>
