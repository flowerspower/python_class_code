/*
ID: s.sophi1
LANG: C++14 
PROG: sprime             
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility> 
#include <math.h>

using namespace std;

ofstream fout ("sprime.out");

bool is_prime(int x) {
	for (int i = 2; i <= sqrt(x); i++) {
		if (x % i == 0) return false;
	}
	return true;
}

vector<int> results;

int is_super_prime(int number) {
	int num_len = to_string(number).length();
	for (int i = 0; i < num_len; i++) {
		if (is_prime(number)) 
			number = number/10;
		else return false;
	}
	return true;
}

int potential_super_primes(int length, string curr_num) {
	if (curr_num.length() == length) {
		if (is_super_prime(atoi(curr_num.c_str())))
			fout << curr_num << endl;
	}
	else {
		string first_num[4] = {"2", "3", "5", "7"};
		string not_first_num[4] = {"1", "3", "7", "9"};
		if (curr_num.length() == 0) {
			for (const string num: first_num) {
				potential_super_primes(length, curr_num+num);
			}
		}
		else {
			for (const string num: not_first_num) {
				potential_super_primes(length, curr_num+num);
			}
		}
	}
}
int main() {
	ifstream fin ("sprime.in");
	int length;
	fin >> length;
	potential_super_primes(length, "");

	return 0;
}
