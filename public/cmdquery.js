function checkQuery() {
    var cmdbar = document.getElementById("cmdbar");
    var cmdquery = cmdbar.value;
    var output = document.getElementById("output");
    if(cmdquery == "getRBLX deploy") {
        output.value = "testing123"
    }
    alert("Enter a valid command")
}