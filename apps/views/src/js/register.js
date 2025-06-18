const registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const formData = {
        username: username,
        email: email,
        password: password,
    };
    const response = await axios.post("/api/auth/register", formData);
    console.log(response)
    if (response.data.code == 201) {
        showToast("注册成功", "info");
    }
})
