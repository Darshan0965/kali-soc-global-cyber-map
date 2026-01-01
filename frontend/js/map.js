// Initialize Map (REAL WORLD MAP)
const map = L.map('map', {
    worldCopyJump: true
}).setView([20, 0], 2);

// OpenStreetMap Tiles (REAL MAP)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

// Store lines & markers
let layers = [];

// Draw attack line
function drawAttack(attack) {
    const src = [attack.source.lat, attack.source.lng];
    const dst = [attack.target.lat, attack.target.lng];

    const color =
        attack.severity === "Critical" ? "#ff0033" :
        attack.severity === "High" ? "#ff6600" :
        attack.severity === "Medium" ? "#ffcc00" :
        "#00ff99";

    const line = L.polyline([src, dst], {
        color: color,
        weight: 2,
        opacity: 0.8
    }).addTo(map);

    const srcMarker = L.circleMarker(src, {
        radius: 6,
        color: color,
        fillOpacity: 0.9
    }).addTo(map);

    const dstMarker = L.circleMarker(dst, {
        radius: 8,
        color: "#ffffff",
        fillOpacity: 1
    }).addTo(map);

    layers.push(line, srcMarker, dstMarker);
}

// Update Table
function updateTable(attacks) {
    const table = document.getElementById("attack-table");
    table.innerHTML = "";

    attacks.forEach(a => {
        const row = `
            <tr class="sev-${a.severity}">
                <td>${a.timestamp}</td>
                <td>${a.attack_type}</td>
                <td>${a.source_country}</td>
                <td>${a.target_country}</td>
                <td>${a.severity}</td>
                <td>${a.threat_score}</td>
                <td>${a.detected_by.join(", ")}</td>
            </tr>
        `;
        table.innerHTML += row;
    });
}

// Fetch live attacks
async function fetchAttacks() {
    try {
        const res = await fetch("http://127.0.0.1:5000/api/live-attacks");
        const attacks = await res.json();

        layers.forEach(l => map.removeLayer(l));
        layers = [];

        attacks.forEach(drawAttack);
        updateTable(attacks);

    } catch (e) {
        console.error("Backend not running");
    }
}

// Auto refresh every 3 seconds
setInterval(fetchAttacks, 3000);
fetchAttacks();