#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
	vector<long int> v = {6, 65, 534, 23, 9223372036854775807};
	
	long int largest_number = LONG_MIN;
	cout << largest_number << endl;
	for (auto num: v) {
		if (num > largest_number){
			largest_number = num;
		}

	}
	cout << largest_number << endl;
	return 0;
}