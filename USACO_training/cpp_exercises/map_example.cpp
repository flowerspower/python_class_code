#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
	map<string, pair<int, float>> cart {
		{"carrot", pair<int, float>(6, 9.99)},
		{"mushroom", pair<int, float>(7, 6.99)},
		{"dandelion", pair<int, float>(20, 0.99)},
		{"cabbage", pair<int, float>(5, 15.99)}
	};
	float total_amount = 0;

	for (const auto & kv: cart) {
		total_amount += kv.second.first * kv.second.second;
	}

	cout << "Total: " << total_amount << endl;
	return 0;
}
