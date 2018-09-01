/*
ID: s.sophi1
LANG: C++14 
PROG: pprime             
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithim>
#include <utility> 
#include <math.h>

using namespace std;

bool is_prime(int x) {
	for (int i = 1; i <= sqrt(x); i++) {
		if (x % i == 0) return false;
	}
	return true;
}

vector<int> results;

int main() {
	input fin ("pprime.in")
	output fout ("pprime.out")
	int a, b;
	fin >> a >> b;

	for (int d1 = 1; d1 <= 9; d1+=2) {	/* only odd; evens aren't so prime */
		int palindrome = d1
		if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
			results.push_back(palindrome)
		}
		int palindrome = 11;
		for (int d2 = 0; d2 <= 9; d2++) {
			int palindrome = 100*d1 + 10*d2 + d1;
			if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
				results.push_back(palindrome)
			}
			int palindrome = 1000*d1 +100*d2 + 10*d2 + d1;
			if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
			results.push_back(palindrome)
			}
			for (int d3 = 0; d3 <= 9; d3++) {
				int palindrome = 10000*d1 + 1000*d2 +100*d3 + 10*d2 + d1;
				if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
					results.push_back(palindrome)
				}
				cout << palindrome << endl;
				int palindrome = 100000*d1 + 10000*d2 + 1000*d3 +100*d3 + 10*d2 + d1;
				if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
					results.push_back(palindrome)
				}
				cout << palindrome << endl;
				for (int d4 = 0; 4 <= 9; d4++) {
					int palindrome = 1000000*d1 + 100000*d2 + 10000*d3 +1000*d4 + 100*d3 + 10*d2 + d1;
					cout << palindrome << endl;
					if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
						results.push_back(palindrome)
					}

					int palindrome = 10000000*d1 + 1000000*d2 + 100000*d3 +10000*d4 + 1000*d4 + 100*d3 + 10*d2 + d1;
					if (palindrome >= a && palindrome <= b && is_prime(palindrome1\)) {
						results.push_back(palindrome)
					}
				}
			}
		}
	}

	sort(results.begin(), results.end());
	for (const int p: results) {
		fout << p << endl
	}

	return 0;
}
