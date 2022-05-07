const assert = require("assert");

String.prototype.unique = function () {
	return this.split("")
		.reverse()
		.reduceRight(
			(acc, char) =>
				acc.includes(char.toUpperCase()) ? acc : acc + char.toUpperCase(),
			""
		);
};

class Cijfer {
	constructor(sleutelwoord) {
		const unique_chars = sleutelwoord.unique().split("");
		const unique_chars_sorted = [...unique_chars].sort();
		this.kolommen = unique_chars.map((char) =>
			unique_chars_sorted.findIndex((c) => c === char)
		);
	}

	codeer(word) {
		let code = "";

		const diff =
			(this.kolommen.length - (word.length % this.kolommen.length)) %
			this.kolommen.length;

		// expand word w "?" to fit number of columns
		for (let i = 0; i < diff; i++) {
			word += "?";
		}

		// construct code
		for (let i = 0; i < this.kolommen.length; i++) {
			const col_i = this.kolommen.findIndex((ii) => ii === i);
			for (let j = 0; j < word.length / this.kolommen.length; j++) {
				code += word[col_i + j * this.kolommen.length];
			}
		}

		return code;
	}

	decodeer(code) {
		assert(code.length % this.kolommen.length === 0, "ongeldig bericht");
		let word = "";
		const height = code.length / this.kolommen.length;
		for (let j = 0; j < height; j++) {
			for (let ii = 0; ii < this.kolommen.length; ii++) {
				const i = this.kolommen[ii];
				word += code[i * height + j];
			}
		}
		return word;
	}
}

const cijfer = new Cijfer("STARWARS");
console.log(cijfer.kolommen);
// [ 2, 3, 0, 1, 4 ]
console.log(cijfer.codeer("HelpmeObiWanKenobi"));
// lbKipie?HeaoeOnbmWn?
console.log(cijfer.decodeer("lbKipie?HeaoeOnbmWn?"));
// HelpmeObiWanKenobi??

let cijfer01 = new Cijfer("agile");
console.log(cijfer01.kolommen);
// [ 0, 2, 3, 4, 1 ]
console.log(
	cijfer01.codeer(
		"Science is the knowledge of consequences, and dependence of one fact upon another."
	)
);
// Sc keone, neoapnrns l ousdec fuae?cetndfsn dd ncoo.i hog ecaeeoetnt?eiewecqenpnf   h?
console.log(
	cijfer01.decodeer(
		"Sc keone, neoapnrns l ousdec fuae?cetndfsn dd ncoo.i hog ecaeeoetnt?eiewecqenpnf   h?"
	)
);
// Science is the knowledge of consequences, and dependence of one fact upon another.???
