#include <bits/stdc++.h>

bool fncomp (char lhs, char rhs) {return lhs<rhs;}

int dbg = 0;

int stealth_debug = 0;

typedef unsigned long long int uint64;

typedef std::tuple<uint64, uint64, uint64> Range;

uint64 max_sum;


int main ()
{

    int N;

    std::cin >> N;
    
    std::vector<uint64> A(N);
    std::vector<uint64> I(N);
    std::vector<uint64> S(N);

    for (int i=0;i<N;i++){
        std::cin >> A[i];
    }
    
    for (int i=0;i<N;i++){
        std::cin >> I[i];
        I [i] -= 1;
    }

    // if (A [0] == 4540) {
    //     stealth_debug = 1;
    // }
    
    std::map<long int, Range> ranges;
    //ranges.emplace(1, Range(123,1,1));

    //dbg && std::cout << "ranges contains:";
    for (auto& x: ranges) {
        //std::cout << " [" << x.first << ':' << x.second << ']';
        //dbg && std::cout << " [" << x.first << ": (" << std::get<0>(x.second)<< "," << std::get<1>(x.second) << "," << std::get<2>(x.second)<< ")]";
    }
    //dbg && std::cout << '\n';

    //dbg && std::cout << "A: [";
    for (auto& x: A){
        //dbg && std::cout << x <<", ";
    }
    //dbg && std::cout << "]\n";
    
    //dbg && std::cout << "I: [";
    for (auto& x: I){
        //dbg && std::cout << x <<", ";
    }
    //dbg && std::cout << "]\n";

    max_sum = 0;

    for (int i = N-1; 0 <= i; i--){
        
        //dbg && std::cout << "max_sum: " << max_sum << std::endl;
        S[i] = max_sum;

        //dbg && std::cout << "i: " << i << std::endl;
        
        Range R(I[i], I[i]+1, A[I[i]]);

        //dbg && std::cout << "R: (" << std::get<0>(R) << ","  << std::get<1>(R) << "," << std::get<2>(R) << ")" << std::endl;
        
        auto ub = ranges.upper_bound(I[i]);
        auto hint = ranges.end();

        if (ranges.size() != 0 &&  ub != ranges.begin()){
            auto prev = std::prev(ub); //should be non-empty

            // should we attach to previous range?
            auto& r0 = std::get<1>((*prev).second);
            if (r0 == I[i]){
                auto R0 = std::move((*prev).second);
                //dbg && std::cout << "merge with previous: " << "R0: (" << std::get<0>(R0) << ","  << std::get<1>(R0) << "," << std::get<2>(R0) << ")" << std::endl;
                ranges.erase(prev);

                std::get<0>(R) = std::get<0>(R0);
                // leave get<1> from R as is
                std::get<2>(R) += std::get<2>(R0);
            }
        }
        
        if (ub != ranges.end()){
            hint = ub;
            if (std::get<1>(R) == (*ub).first) {
                // if *i is adjacent to ub, remove ub and merge with i
                auto R1 = std::move((*ub).second);
                hint = ranges.erase(ub);

                // std::get<0>(R) leave as is
                std::get<1>(R) = std::get<1>(R1);
                std::get<2>(R) += std::get<2>(R1);
            }
        }

        if (stealth_debug && i < 5){
            std::cout << "R: (" << std::get<0>(R)<< "," << std::get<1>(R) << "," << std::get<2>(R)<< ")]" << std::endl;
            std::cout << "ranges contains:";
            for (auto& x: ranges) {
                std::cout << " [" << x.first << ": (" << std::get<0>(x.second)<< "," << std::get<1>(x.second) << "," << std::get<2>(x.second)<< ")]";
            }
            std::cout << '\n';
        }
        
        auto sum = std::get<2>(R);
        ranges.emplace_hint(hint, std::get<0>(R), R);

        if(max_sum < sum){
            max_sum = sum;
        }
    }

    if (stealth_debug){
        dbg = 1;
    }    
    dbg && std::cout << "ranges contains:";
    for (auto& x: ranges) {
        dbg && std::cout << " [" << x.first << ": (" << std::get<0>(x.second)<< "," << std::get<1>(x.second) << "," << std::get<2>(x.second)<< ")]";
    }
    dbg && std::cout << '\n';
    

    for (auto& x: S){
        std::cout << x << std::endl;
    }
    
    return 0;
}
