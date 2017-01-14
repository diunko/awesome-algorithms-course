#include <bits/stdc++.h>
#include <cstdint>
#include <algorithm>
#include <bitset>
#include <exception>

#include <cmath>

// template <typename T>
// std::ostream& operator<< (std::ostream& out, const std::vector<T>& v) {
//   if ( !v.empty() ) {
//     out << '[';
//     std::copy (v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
//     out << "\b\b]";
//   }
//   return out;
// }

int dbg = 0;
int stealth_debug = 0;

typedef unsigned long long int uint64;
typedef long long int int64;

typedef std::tuple<uint64, uint64> Server;

typedef union {
    struct {
        uint16_t magic;
        uint8_t  p;
        uint8_t  type;
        int32_t  x;
    } e;
    int64_t raw;
} Event_t;

int main ()
{

    int N, M;

    unsigned int t;
    
    std::cin >> N >> M;
    dbg && std::cout << "N, M: " << N << " " << M << " " << std::endl;

    std::vector<Event_t> events(N*4+M);

    // t = M;
    // dbg && std::cout << "sizeof Event: " << sizeof(Event_t) << std::endl;
    
    for (int i=0;i<N;i++){
        int32_t x;
        int32_t h;
        uint16_t l, r;
        
        std::cin >> x;
        std::cin >> h;
        std::cin >> l;
        std::cin >> r;

        dbg && std::cout << x << " " <<  h  << " " << l << " " << r << std::endl;

        l = 100-l;
        r = 100-r;

        events[i*4+0] = Event_t({
            .e = {
                .magic = 0,
                .p = uint8_t(l),
                .type = 1, // interval start
                .x = x - h,
            }
        });

        events[i*4+1] = Event_t({
            .e = {
                .magic = 0,
                .p = uint8_t(l),
                .type = 2, // interval end
                .x = x,
            }
        });

        events[i*4+2] = Event_t({
            .e = {
                .magic = 0,
                .p = uint8_t(r),
                .type = 1, // interval start
                .x = x + 1,
            }
        });

        events[i*4+3] = Event_t({
            .e = {
                .magic = 0,
                .p = uint8_t(r),
                .type = 2, // interval end
                .x = x + h + 1,
            }
        });
    }

    for (int i=0;i<M;i++){
        int32_t x;
        uint16_t magic;
        
        std::cin >> x >> magic;

        events[N*4+i] = Event_t({
            .e = {
                .magic = magic,
                .p = 0,
                .type = 3,
                .x = x,
            }
        });
    }

    std::sort(events.begin(), events.end(),
              [](Event_t a, Event_t b) { return a.raw < b.raw; });

    double magic = 0.0;
    double problog = 0.0;
    int zeros = 0;
    
    for (auto& e: events){
        // if (dbg) {
        //     std::cout << "{\n"
        //               << "    " << std::bitset<64>(e.raw) << std::endl
        //               << "    { x: " << e.e.x << std::endl
        //               << "      t: " << int(e.e.type) << std::endl
        //               << "      p: " << int(e.e.p) << std::endl
        //               << "      m: " << e.e.magic << " } }" << std::endl;
        //     std::cout << "(magic, prob, zeros): (" << magic << ", " << exp(problog) << ", " << zeros << ")" << std::endl;
        // }

        if (e.e.type == 1 ){
            if (e.e.p == 0){
                zeros += 1;
            } else {
                problog += log(double(e.e.p)/100.0);
            }
        } else if (e.e.type == 2){
            if (e.e.p == 0){
                zeros -= 1;
            } else {
                problog -= log(double(e.e.p)/100.0);
            }
        } else if (e.e.type == 3){
            if (zeros == 0){
                magic += exp(problog)*e.e.magic;
            }
        } else {
            throw std::exception();
        }

        if (dbg){
            std::cout << "(magic, prob, zeros): (" << magic << ", " << exp(problog) << ", " << zeros << ")" << std::endl;
        }
    }

    std::cout << magic << std::endl;
    
    return 0;
}
