function showToast(message, type = "info", duration = 3000) {
    let background = "#3b82f6";

    if (type === "success") background = "#22c55e";
    if (type === "error") background = "#ef4444";
    if (type === "warning") background = "#f59e0b";

    Toastify({
        text: message,
        duration: duration,
        close: true,
        gravity: "top",
        position: "right",
        backgroundColor: background,
        stopOnFocus: true
    }).showToast();
}
