function validateForm() {
    let name = document.getElementById("name").value;
    if(name === "") {
        alert("Name cannot be empty");
        return false;
    }
    return true;
}
