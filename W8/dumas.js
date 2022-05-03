function codeersleutel(sleuteltekst) {
    var sleutel = {};

    var index = 1;
    for (const char of sleuteltekst.toUpperCase()) {
        if (char.match(/[^\ ]/)) {
            if (sleutel[char]) {
                sleutel[char].push(index)
            } else {
                sleutel[char] = [index]
            }
            index += 1;
        }
    }
    return sleutel
}

function codeer(tekst, sleuteltekst) {
    const sleutel = codeersleutel(sleuteltekst);
    var code = [];
    tekst = tekst.toUpperCase();
    var slice_of_text = "";

    for (const index in tekst) {
        const char = tekst[index];
        slice_of_text += char;
        
        const occurence = slice_of_text.split(char).length - 1;
        code.push(sleutel[char][(occurence-1) % sleutel[char].length]);
    }
    return code
}

var sleutel = codeersleutel('Lost time is never found again.');
console.log(sleutel['N']);
//[11, 19, 25]
console.log(sleutel['E']);
//[8, 12, 14]
console.log(sleutel['.']);
// [26]

var sleuteltekst = 'Lost time is never found again.';
console.log(codeer('nondeterminativeness', sleuteltekst));
// [11, 2, 19, 20, 8, 4, 12, 15, 7, 6, 25, 21, 5, 9, 13, 14, 11, 8, 3, 10]
console.log(codeer('interdenominationalism', sleuteltekst));
// [6, 11, 4, 8, 15, 20, 12, 19, 2, 7, 9, 25, 21, 5, 24, 17, 11, 23, 1, 6, 3, 7]
console.log(codeer('gastroenteroanastomosis', sleuteltekst));
// [22, 21, 3, 4, 15, 2, 8, 11, 5, 12, 15, 17, 23, 19, 21, 10, 4, 2, 7, 17, 3, 6, 10]
