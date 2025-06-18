
const loginForm = document.getElementById('loginForm');

loginForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    const username = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const remember = document.getElementById('remember').checked;
    const formData = {
        username: username,
        password: password,
    };
    const response = await axios.post("/api/auth/login", formData);
    console.log(response)
    if (response.data.code == 200) {
        alert("登陆成功")
    }
})