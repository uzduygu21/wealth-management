document.addEventListener("DOMContentLoaded", () => {
    if (window.location.href.indexOf("login") == -1 && window.location.href.indexOf("register") == -1
        && window.location.href.indexOf("account") == -1 && window.location.href.indexOf("questions") == -1
        && window.location.href.indexOf("quiz") == -1) {
        document.querySelector("#our-approach").style.display = 'none';
        document.querySelector("#our-services").style.display = 'none';
        document.querySelector("#our-history").style.display = 'none';

        document.querySelector("#approach").addEventListener('click', () => load_about());
        document.querySelector("#services").addEventListener('click', () => load_services());
        document.querySelector("#history").addEventListener('click', () => load_history());

    }
    if (window.location.href.indexOf("account") != -1) {
        document.querySelector("#account-div").style.display = 'none';
        document.querySelector(".add-circle").style.display = 'block';
        document.querySelector(".remove-circle").style.display = 'none';
        document.querySelector("#rates-table").style.display = 'none';

        var editForm = document.querySelectorAll(".edit-form");
        for (let i = 0; i < editForm.length; i++) {
            editForm[i].style.display = 'none';
        }
    }

})


function load_about() {
    document.querySelector("#our-approach").style.display = 'block';
    document.querySelector("#home").style.display = 'none';
    document.querySelector("#our-services").style.display = 'none';
    document.querySelector("#our-history").style.display = 'none';
}

function load_services() {
    document.querySelector("#our-approach").style.display = 'none';
    document.querySelector("#home").style.display = 'none';
    document.querySelector("#our-services").style.display = 'block';
    document.querySelector("#our-history").style.display = 'none';
}

function load_history() {
    document.querySelector("#our-approach").style.display = 'none';
    document.querySelector("#home").style.display = 'none';
    document.querySelector("#our-services").style.display = 'none';
    document.querySelector("#our-history").style.display = 'block';
}

function contact_advisor() {
    let question = document.querySelector("#question").value;
    fetch('/contact', {
        method: 'POST',
        body: JSON.stringify({
            question: question
        })
    })
        .then(response => {
            response.json()
        })
        .then(result => console.log(result))
}

function add_account() {
    document.querySelector("#account-div").style.display = 'block';
    document.querySelector(".add-circle").style.display = 'none';
    document.querySelector(".remove-circle").style.display = 'block';
    document.querySelector(".plus-btn").addEventListener('click', () => {
        document.querySelector("#account-div").style.display = 'none';
        document.querySelector(".add-circle").style.display = 'block';
        document.querySelector(".remove-circle").style.display = 'none';
        location.reload();
    })
}

function create_account() {
    let accountnum = document.querySelector("#account-num").value;
    let amount = document.querySelector("#amount").value;
    let bank = document.querySelector("#bank").value;
    fetch('/account', {
        method: 'POST',
        body: JSON.stringify({
            accountnum: accountnum,
            amount: amount,
            bank: bank
        })
    })
        .then(response => {
            response.json()
            location.reload();
        })
        .then(result => console.log(result))
}

function show_stocks() {
    fetch('https://api.exchangeratesapi.io/latest?base=USD')
        .then(response => response.json())
        .then(data => {
            document.querySelector("#rates-table").style.display = 'block';

            document.querySelector("#AUD").innerHTML = data.rates.AUD;
            document.querySelector("#BGN").innerHTML = data.rates.BGN;
            document.querySelector("#BRL").innerHTML = data.rates.BRL;
            document.querySelector("#CAD").innerHTML = data.rates.CAD;
            document.querySelector("#CHF").innerHTML = data.rates.CHF;
            document.querySelector("#CNY").innerHTML = data.rates.CNY;
            document.querySelector("#CZK").innerHTML = data.rates.CZK;
            document.querySelector("#DKK").innerHTML = data.rates.DKK;
            document.querySelector("#EUR").innerHTML = data.rates.EUR;
            document.querySelector("#GBP").innerHTML = data.rates.GBP;
            document.querySelector("#HKD").innerHTML = data.rates.HKD;
        });
}

function submit_quiz() {
    let cust_answers = [];
    let cust_score = 0;
    let correct_answers = ["1-C", "2-D", "3-B", "4-A", "5-D", "6-B", "7-B", "8-A", "9-C", "10-D"];
    var radios = document.querySelectorAll('input[type="radio"]:checked');
    for (i = 0; i < radios.length; i++) {
        cust_answers.push(radios[i].value);
    }
    for (i = 0; i < correct_answers.length; i++) {
        if (cust_answers.includes(correct_answers[i])) {
            cust_score += 10;
        }
    }
    document.querySelector(".modal-title").innerHTML = `Score: ${cust_score}`;
    fetch('/quiz', {
        method: 'POST',
        body: JSON.stringify({
            score: cust_score
        })
    })
        .then(response => {
            response.json()
        })
        .then(result => console.log(result))
}

function del_account(id) {
    fetch(`/del_edit/${id}`, {
        method: 'DELETE',
    })
        .then(res => {
            res.text()
            location.reload();
        })
        .then(res => console.log(res))
}

function edit_account(id) {
    document.querySelector(`#edit-form-${id}`).style.display = 'block';
    document.querySelector(`#regular-form-${id}`).style.display = 'none';

    document.querySelector(`#cancel-edited-${id}`).addEventListener('click', () => location.reload());



    document.querySelector(`#save-edited-${id}`).addEventListener('click', () => {
        document.querySelector(`#edit-form-${id}`).style.display = 'none';
        document.querySelector(`#regular-form-${id}`).style.display = 'block';
        let editedBank = document.querySelector(`.bank-text-${id}`).value;
        let editedAccountNum = document.querySelector(`.accountnum-text-${id}`).value;
        let editedAmount = document.querySelector(`.amount-text-${id}`).value;

        console.log(editedAmount, editedBank, editedAccountNum)

        fetch(`/del_edit/${id}`, {
            method: 'POST',
            body: JSON.stringify({
                id: id,
                accountnum: editedAccountNum,
                bank: editedBank,
                amount: editedAmount
            })
        })
            .then(response => {
                response.text()
                location.reload();
            })
            .then(p => {
                console.log(p)
            })
    })
}