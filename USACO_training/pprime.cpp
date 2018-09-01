/*
ID: s.sophi1
LANG: C++14 
PROG: pprime             
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility> 
#include <math.h>

using namespace std;

bool is_prime(int x) {
	for (int i = 2; i <= sqrt(x); i++) {
		if (x % i == 0) return false;
	}
	return true;
}

vector<int> results;

int main() {
	ifstream fin ("pprime.in");
	ofstream fout ("pprime.out");
	int a, b;
	fin >> a >> b;
	int palindrome;
	for (int d1 = 1; d1 <= 9; d1+=2) {	/* only odd; evens aren't so prime */
		palindrome = d1;
		if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
			results.push_back(palindrome);
		}
		palindrome = 10*d1+d1;
		if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
			results.push_back(palindrome);
		}
		for (int d2 = 0; d2 <= 9; d2++) {
			palindrome = 100*d1 + 10*d2 + d1;
			if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
				results.push_back(palindrome);
			}
			palindrome = 1000*d1 +100*d2 + 10*d2 + d1;
			if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
			results.push_back(palindrome);
			}
			for (int d3 = 0; d3 <= 9; d3++) {
				palindrome = 10000*d1 + 1000*d2 +100*d3 + 10*d2 + d1;
				if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
					results.push_back(palindrome);
				}
				palindrome = 100000*d1 + 10000*d2 + 1000*d3 +100*d3 + 10*d2 + d1;
				if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
					results.push_back(palindrome);
				}
				for (int d4 = 0; d4 <= 9; d4++) {
					palindrome = 1000000*d1 + 100000*d2 + 10000*d3 +1000*d4 + 100*d3 + 10*d2 + d1;
					if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
						results.push_back(palindrome);
					}

					palindrome = 10000000*d1 + 1000000*d2 + 100000*d3 +10000*d4 + 1000*d4 + 100*d3 + 10*d2 + d1;
					if (palindrome >= a && palindrome <= b && is_prime(palindrome)) {
						results.push_back(palindrome);
					}
				}
			}
		}
	}

	sort(results.begin(), results.end());
	for (const int p: results) {
		fout << p << endl;
	}

	return 0;
}
