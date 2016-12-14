#include <bits/stdc++.h>

bool fncomp (char lhs, char rhs) {return lhs<rhs;}

int dbg = 0;

int stealth_debug = 0;

typedef unsigned long long int uint64;

typedef std::tuple<uint64, uint64> Server;

uint64 max_sum;


int main ()
{

    int N, K;

    
    std::cin >> N;
    std::cin >> K;

    dbg && std::cout << "N, K: " << N << " " << K << std::endl;

    std::set<Server> servers;

    std::vector<uint64> S(N);
    std::vector<uint64> M(N);
    std::vector<uint64> E(N);

    for (int i=0;i<N;i++){
        std::cin >> S[i];
        std::cin >> M[i];
    }

    
    
    for (int i=0;i<N; i++){

        uint64 max = 0;
        
        if (servers.size() < K){
            max = S[i];
            uint64 e = max + M[i];
            servers.emplace(Server(e, servers.size()));
            E[i] = e;
        } else {
            auto m = servers.begin();
            max = std::max(std::get<0>(*m), S[i]);
            auto si = std::get<1>(*m);
            servers.erase(m);

            uint64 e = max + M[i];
            servers.emplace(Server(e, si));
            E[i] = e;
        }

    }

    if (stealth_debug){
        dbg = 1;
    }    
    // dbg && std::cout << "servers contains:";
    // for (auto& x: servers) {
    //     dbg && std::cout << " [" << x << "]";
    // }
    // dbg && std::cout << '\n';
    
    std::stringstream buffer;
    
    for (auto& x: E){
        buffer << x << std::endl;
    }

    std::cout << buffer.str();
    

    return 0;
}
