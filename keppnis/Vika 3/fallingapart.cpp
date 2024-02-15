#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>


typedef long long ll;
using namespace std;

int main() {
	ll i;
	ll pieces;
	ll alice = 0;
	ll bob = 0;
	cin >> pieces;
	vector<ll> piecesList(pieces);

	for (i = 0; i < pieces; i++) {
		cin >> piecesList[i];
	}

	sort(piecesList.rbegin(), piecesList.rend());

	for (i = 0; i < pieces; i++) {
		if (i % 2 == 0) {
			alice += piecesList[i];
		}
		else {
			bob += piecesList[i];
		}
	}
	cout << alice << " " << bob << "\n";
	return 0;
}