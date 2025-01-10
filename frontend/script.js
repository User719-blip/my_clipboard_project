
const apiUrl = "http://127.0.0.1:8000";

document.getElementById("add-button").addEventListener("click", async () => {
  const content = prompt("Enter content to add to clipboard:");
  if (content) {
    const response = await fetch(`${apiUrl}/add`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content }),
    });
    const data = await response.json();
    alert("Item added successfully with ID: " + data.id);
  }
});


document.getElementById("refresh-button").addEventListener("click", async () => {
  const response = await fetch(`${apiUrl}/get_all`);
  const items = await response.json();
  alert("Clipboard Items:\n" + JSON.stringify(items, null, 2));
});


document.getElementById("delete-button").addEventListener("click", async () => {
  const confirmDelete = confirm("Are you sure you want to delete all items?");
  if (confirmDelete) {
    const response = await fetch(`${apiUrl}/delete_all`, { method: "DELETE" });
    const data = await response.json();
    alert(data.message);
  }
});


document.getElementById("qr-button").addEventListener("click", () => {
  alert("QR functionality coming soon!");
});

document.getElementById("star-button").addEventListener("click", () => {
  alert("Star functionality coming soon!");
});
