const assert = require("assert");

const validKleuren = ["C", "D", "H", "S"];
const validRangen = [
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"10",
	"J",
	"Q",
	"K",
	"A",
];

String.prototype.isValidKaart = function () {
	const rang = this.slice(0, -1);
	const kleur = this.slice(-1);
	// valid rang & color
	const validRang = validRangen.includes(rang.toUpperCase());
	const validKleur = validKleuren.includes(kleur.toUpperCase());

	// same capitalization needed because capitalization means which face is up
	const sameCapitalization = ["J", "Q", "K", "A"].includes(rang.toUpperCase())
		? (rang.toUpperCase() === rang && kleur.toUpperCase() === kleur) ||
		  (rang.toLowerCase() === rang && kleur.toLowerCase() === kleur)
		: true;
	return validKleur && validRang && sameCapitalization;
};

// bovenste kaart : eerste element van de array kaarten
class Stapel {
	constructor(array_stapel) {
		assert(
			Array.isArray(array_stapel) &&
				[...new Set(array_stapel)].length === array_stapel.length &&
				array_stapel.every((kaart) => kaart.isValidKaart()),
			"ongeldige kaarten"
		);
		this.stapel = [...array_stapel];
	}

	toArray() {
		return this.stapel;
	}

	isVisible(kaart) {
		return kaart.search(/[a-z]/) === -1;
	}

	flip(n) {
		// this = "AH"
		this.stapel[n] =
			this.stapel[n] === this.stapel[n].toUpperCase()
				? this.stapel[n].toLowerCase()
				: this.stapel[n].toUpperCase();
	}

	toString() {
		var tekst = "";
		for (const kaart of this.stapel) {
			if (this.isVisible(kaart)) {
				tekst += kaart + " ";
			} else {
				tekst += "** ";
			}
		}
		return tekst.slice(0, -1);
	}

	countSideUp() {
		return this.stapel
			.map((kaart) => this.isVisible(kaart))
			.reduceRight(
				(count, isVisibleBool) => (isVisibleBool ? count + 1 : count),
				0
			);
	}

	splitsen(n) {
		const stapel = [...this.stapel];
		if (n === undefined) {
			n = this.beeldzijdeBoven();
		}
		return [new Stapel(stapel.slice(0, n)), new Stapel(stapel.slice(n))];
	}

	selectie_omdraaien(n) {
		// flips cards at positions given by n
		// without changing card positions
		// if no n is given => flip all cards
		// if type(n) == int => first n cards
		// if type(n) == array => cards flipped at indices given by n
		if (n === undefined) {
			n = [...Array(this.stapel.length).keys()];
		} else {
			n = [].concat(n.map((number) => number - 1));
		}

		for (const index of n) {
			this.flip(index);
		}
		return this;
	}

	bovenste_omdraaien(a) {
		// takes top a cards and flips the order and sides
		this.stapel = this.stapel
			.slice(0, a)
			.reverse()
			.concat(this.stapel.slice(a));
		this.selectie_omdraaien(
			Array.from(Array(a).keys()).map((number) => number + 1)
		);
		return this;
	}

	couperen(a) {
		// De methode moet de bovenste kaarten afnemen van de stapel,
		// en deze kaarten onder de resterende kaarten van de stapel schuiven.
		this.stapel = this.stapel.slice(a).concat(this.stapel.slice(0, a));
		return this;
	}
}

const stapel = new Stapel([
	"AH",
	"3S",
	"KC",
	"4H",
	"3D",
	"10H",
	"8D",
	"5D",
	"7C",
	"QS",
]);

console.log(stapel.selectie_omdraaien().toString());
// ** ** ** ** ** ** ** ** ** **
console.log(stapel.bovenste_omdraaien(2).toString());
// 3S AH ** ** ** ** ** ** ** **
console.log(stapel.couperen(4).toString());
// ** ** ** ** ** ** 3S AH ** **
console.log(stapel.selectie_omdraaien([2, 4, 6, 8, 10]).toString());
// ** 10H ** 5D ** QS 3S ** ** 4H
