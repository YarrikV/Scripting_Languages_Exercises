const assert = require("assert");

String.prototype.isAlpha = function () {
	return this.search(/^[A-Z]+$/i) === 0; // check if string only consist of alpha chars
};

function letterwaarde(letters) {
	const values = {};

	letters = `${letters}`.toUpperCase();
	const len = letters.length;
	assert(len % 2 === 1 && letters.isAlpha(), "ongeldige letterreeks");

	var n = -(len - 1) / 2;
	for (const letter of letters) {
		if (letter in values) {
			assert(false, "ongeldige letterreeks");
		}
		values[letter] = n;
		n += 1;
	}
	return values;
}

function woordwaarde(planet, letters) {
	planet = `${planet}`.toUpperCase();
	const key = letterwaarde(letters);
	var value = 0;
	for (const letter of planet) {
		assert(letter in key, "ontbrekende letters");
		value += key[letter];
	}
	return value;
}

function alignering(planets, letters) {
	var alignment_n = woordwaarde(planets.shift(), letters);
	for (const planet of planets) {
		const value = woordwaarde(planet, letters);
		if (alignment_n + 1 !== value) {
			return false;
		}
		alignment_n += 1;
	}
	return true;
}

function CustomSortPlanets(a, b, letters) {
	return (
		woordwaarde(a, letters) - woordwaarde(b, letters) || a.localeCompare(b)
	);
}

function rangschik1(planets, letters) {
	planets.sort((a, b) => CustomSortPlanets(a, b, letters));
}

function rangschik2(planets, letters) {
	planets = [...planets];
	planets.sort((a, b) => CustomSortPlanets(a, b, letters));
	return planets;
}
