const assert = require("assert");

// bovenste kaart : eerste element van de array kaarten
class Stapel {
	constructor(array_stapel) {
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

	beeldzijdeBoven() {
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

	omdraaien(n) {
		if (n == undefined) {
			n = [...Array(this.stapel.length).keys()];
		} else {
			n = [].concat(n);
		}

		for (const index of n) {
			this.flip(index);
		}
		return this;
	}

	evenveelNaarBovenAls(andere_stapel) {
		return this.beeldzijdeBoven() == andere_stapel.beeldzijdeBoven();
	}
}
