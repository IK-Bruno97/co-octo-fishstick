const steps = Array.from(document.querySelectorAll("form .step"));
const nextBtn = document.querySelectorAll("form .next-btn");
const prevBtn = document.querySelectorAll("form .previous-btn");
const form = document.querySelector("form");

nextBtn.forEach((button) => {
    button.addEventListener("click", () => {
        changeStep("next");
    });
});

prevBtn.forEach((button) => {
    button.addEventListener("click", () => {
        changeStep("prev");
    });
});

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const inputs = {};
    form.querySelectorAll("input").forEach((input) => {
        const {name, value} = input;
        inputs[name] = value;
    });
    console.log(inputs);
    submitData(inputs)
    form.reset();
});

let submitData = async (formValue) => {
    let url = '/receipt/'
    let response = await fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':  formValue.csrfmiddlewaretoken
        },
        body: JSON.stringify(formValue)
    })
    console.log(JSON.stringify(formValue))
    let data = await response.json()
    console.log('Data: ', data)
}

function changeStep(btn) {
    let index = 0;
    const active = document.querySelector(".active");
    index = steps.indexOf(active);
    steps[index].classList.remove("active");
    if (btn === "next"){
        index++;
    } else if (btn === "prev"){
        index--;
    }
    steps[index].classList.add("active");
}
