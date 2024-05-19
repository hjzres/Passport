let worth_inputs = document.getElementsByClassName("worth");
let worth_num = document.getElementById("worth-num");

for (let i = 0; i < worth_inputs.length; i++) {
    worth_inputs[i].addEventListener("click", () => {
        worth_num.innerHTML = i + 1;
    });
}