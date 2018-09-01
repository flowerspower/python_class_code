/*
ID: s.sophi1
LANG: C++14 
PROG: ariprog               
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <utility> 

using namespace std;

int search_length;

set<pair<int, int>> try_all_possibilities(set<int> bisquares, bool bisquares_flags[]) {
	set<pair<int, int>> a_and_bs;
    vector<int> bisquares_list(bisquares.begin(), bisquares.end());
    sort(bisquares_list.begin(), bisquares_list.end());
    
    for (int i = 0; i <= bisquares.size()-search_length; i++) {
    	int a = bisquares_list[i];
    	int num = bisquares_list.back() - bisquares_list[0];
    	for (int j = 1; j <= (num-a)/(search_length-1); j++) {
    		int b = j;
    		bool bad = false;
    		for (int x=search_length-1; x>=0; x--) {
    			if (!bisquares_flags[a + (x*b)]) {
    				bad = true;
    				break;
    			} 
    		}

    		if (!bad)
    			a_and_bs.insert({b, a});
    	}
    } 
      
    return a_and_bs;
}


int main() {
	ifstream fin ("ariprog.in");
    ofstream fout ("ariprog.out");
    
    int pq_limit;
    fin >> search_length >> pq_limit;

    bool bisquares_flags[2*pq_limit*pq_limit] {false};


    set<int> bisquare_set;
    for (int p = 0; p <= pq_limit; p++) {
        for (int q = p; q <= pq_limit; q++) {
            int bisquare = p*p + q*q;
            bisquares_flags[bisquare] = true;
            bisquare_set.insert(bisquare);
        }
    }

    auto thing = try_all_possibilities(bisquare_set, bisquares_flags);
    if (!thing.empty()) {
    	for (const auto & p: thing)
    		fout << p.second << " " << p.first << endl;
    }	
    else 
    	fout << "NONE" << endl;
    return 0;
}

