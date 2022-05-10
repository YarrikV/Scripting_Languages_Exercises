const assert = require("assert");
const comb_errMsg = "ongeldige combinatie";
const disc_errMsg = "ongeldige schijf";

class Combinatieslot {
	// selt combinatieslot voor
	constructor(solution, m = 9) {
		// m is max value
		this.maxVal = m;
		this.solution = [...solution];
		this.combination = Array(solution.length).fill(0);

		// check if combination is valid
		assert(
			solution.length > 0 &&
				Math.min(...solution) >= 0 &&
				Math.max(...solution) <= m,
			comb_errMsg
		);
	}

	toString() {
		// returns string representation of comb lock
		return [...this.combination]
			.reverse()
			.reduceRight((acc, number) => acc + number + "-", "")
			.slice(0, -1);
	}

	open() {
		// check if lock is open
		return this.solution.every(
			(solution_num, index) => solution_num === this.combination[index]
		);
	}

	roteer(disc_nrs, disc_amount) {
		// turn lock disc_nr with disc_amount
		// roteer(0,5) rotates first disc (index 0) with 5

		// disc_nrs must always be an array
		disc_nrs = [].concat(disc_nrs);

		// check if disc_nrs are all valid
		assert(
			disc_nrs.every(
				(disc_nr) => disc_nr >= 0 && disc_nr < this.solution.length
			),
			disc_errMsg
		);

		// rotate discs
		for (const disc_nr of disc_nrs) {
			this.combination[disc_nr] =
				(this.combination[disc_nr] + disc_amount) % (1 + this.maxVal);
		}
	}
}

const slot = new Combinatieslot([14, 13, 2, 7, 6], 16);
console.log(slot.toString());
// 0-0-0-0-0

slot.roteer([0, 2, 4], 6);
console.log(slot.toString());
// 6-0-6-0-6
slot.roteer([1, 3, 2], 13);
console.log(slot.toString());
// 6-13-2-13-6
slot.roteer([0, 3], 8);
console.log(slot.toString());
// 14-13-2-4-6
slot.roteer(3, 3);
console.log(slot.toString());
// 14-13-2-7-6
console.log(slot.open());
// true
