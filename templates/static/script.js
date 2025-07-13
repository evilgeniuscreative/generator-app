function toggleInput(mode) {
    document.getElementById('inputMode').value = mode;
    document.getElementById('csvInput').style.display = mode === 'csv' ? 'block' : 'none';
    document.getElementById('manualInput').style.display = mode === 'manual' ? 'block' : 'none';
  }
  