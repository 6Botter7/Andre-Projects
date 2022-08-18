const diceNo1 = ["1","2","3","4","5","6"]
const diceNo2 = ["1","2","3","4","5","6"]

function roll(){
    return Math.floor(Math.random(0, 5)+1)
};

function diceRoll(){
    let diceIndex1 = roll();
    let diceIndex2 = roll();
    let d1 = diceNo1[diceIndex1];
    let d2 = diceNo2[diceIndex2];
    console.log(d1);
    console.log(d2);
};

diceRoll()
console.log(roll)
console.log(diceRoll);