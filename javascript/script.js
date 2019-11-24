var operand1 = '';
var operand2 = '';
var operator = '';
var result = 0;

function addOperand(op) {
    console.log('hocche');
    if (!operator) {
        operand1 += op;
        document.getElementById('display').value += op;
    } else {
        operand2 += op;
        document.getElementById('display').value += op;
    }
}

function addOperator(op) {
    operator = op;
    document.getElementById('display').value += operator;
}

function eq() {
    var v1 = parseInt(operand1);
    var v2 = parseInt(operand2);
        console.log(v1);
        console.log(v2);
        console.log(result);
    if (operator == '+') {
        console.log(v1);
        console.log(v2);
        console.log(result);
        result = v1 + v2;
        document.getElementById('display').value = result;
    } else if (operator == '-') {
        result = v1 - v2;
        document.getElementById('display').value = result;

    } else if (operator == '*') {
        result = v1 * v2;
        document.getElementById('display').value = result;

    } else if (operator == "/") {
        result = v1 / v2;
        document.getElementById('display').value = result;

    }
    else {}
}

function clearAll() {
    operand1 = operand2 = operator = '';
    document.getElementById('display').value = '';
}
console.log('hocche to');