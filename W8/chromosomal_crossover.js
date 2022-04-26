function crossoverpunten(c1, c2) {
    var crossover_amount = 0;
    var c1_copy = [...c1];
    var c2_copy = [...c2];
    var num1 = c1_copy.shift();
    var num2 = c2_copy.shift();
    while (num1 != undefined && num2 != undefined) {
        if (num1 == num2) {
            crossover_amount++;
            num1 = c1_copy.shift();
            num2 = c2_copy.shift();
        } else if (num1 > num2) {
            num2 = c2_copy.shift();
        } else if (num1 < num2) {
            num1 = c1_copy.shift();
        }
    }
    return crossover_amount;
}

function maximaleSom(c1, c2) {
    var som1 = [0];
    var som2 = [0];

    var c1_copy = [...c1];
    var c2_copy = [...c2];
    var num1 = c1_copy.shift();
    var num2 = c2_copy.shift();
    while (!(num1 == undefined && num2 == undefined)) {
        if (num1 == num2) {

            som1.push(num1)
            num1 = c1_copy.shift();

            som2.push(num2)            
            num2 = c2_copy.shift();

        } else if (num1 > num2 || num1 == undefined) {
            som2[som2.length-1] += num2;
            num2 = c2_copy.shift();
            
        } else if (num1 < num2 || num2 == undefined) {
            som1[som1.length-1] += num1;
            num1 = c1_copy.shift();
        }
    }
    
    var max_som = 0;
    var num1 = som1.shift();
    var num2 = som2.shift();
    while (!(num1 == undefined && num2 == undefined)) {
        max_som += Math.max(num1, num2)
        num1 = som1.shift();
        num2 = som2.shift();
    }
    return max_som;
}
