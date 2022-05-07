const assert = require("assert");

class Zeshoek {
	constructor(q, r) {
		this.q = q;
		this.r = r;

		Object.seal(this); // no properties (this.test)
		Object.freeze(this); // no change of property values
	}

	richtingen(richting) {
		return {
			NW: [0, -1],
			NO: [1, -1],
			O: [1, 0],
			ZO: [0, 1],
			ZW: [-1, 1],
			W: [-1, 0],
		}[richting];
	}

	buren_arr() {
		return ["NW", "NO", "O", "ZO", "ZW", "W"];
	}

	toString() {
		return "Zeshoek(" + this.q + ", " + this.r + ")";
	}

	afstand(other) {
		return (
			0.5 *
			(Math.abs(this.q - other.q) +
				Math.abs(this.r - other.r) +
				Math.abs(this.q + this.r - other.q - other.r))
		);
	}

	buur(richting) {
		assert(this.richtingen(richting) !== undefined, "ongeldige richting");
		let dq;
		let dr;
		[dq, dr] = this.richtingen(richting);
		return new Zeshoek(this.q + dq, this.r + dr);
	}

	pad(path) {
		if (path.startsWith("O") || path.startsWith("W")) {
			// console.log(path.slice(0, 1), path.slice(1));
			return this.buur(path.slice(0, 1)).pad(path.slice(1));
		} else if (
			path.startsWith("NO") ||
			path.startsWith("ZO") ||
			path.startsWith("NW") ||
			path.startsWith("ZW")
		) {
			// console.log(path.slice(0, 2), path.slice(2));
			return this.buur(path.slice(0, 2)).pad(path.slice(2));
		} else {
			// at the end
			assert(path.length === 0, "ongeldig pad");
			return this;
		}
	}

	buren() {
		const buren = [];
		for (const buur_richting of this.buren_arr()) {
			buren.push(this.buur(buur_richting));
		}
		return buren;
	}
}
