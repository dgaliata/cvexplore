async function searchCVE() {
    const cveId = document.getElementById("cveInput").value;
    const response = await fetch(`/api/v1/cve/${cveId}`);
    const data = await response.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
  }
  