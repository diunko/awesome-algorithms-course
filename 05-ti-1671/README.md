
## 1671. Anansi's Cobweb

http://acm.timus.ru/problem.aspx?space=1&num=1671

Time limit: 1.0 second
Memory limit: 64 MB

Usatiy-Polosatiy XIII decided to destroy Anansi's home — his cobweb.
The cobweb consists of N nodes, some of which are connected by
threads. Let us say that two nodes belong to the same piece if it is
possible to get from one node to the other by threads.
Usatiy-Polosatiy has already decided which threads and in what order
he would tear and now wants to know the number of pieces in cobweb
after each of his actions.

### Input

The first line contains integers N and M — the number of nodes and
threads in the cobweb, respectively(2 ≤ N ≤ 100000; 1 ≤ M ≤ 100000).
Each of the next M lines contains two different integers — the 1-based
indices of nodes connected by current thread. The threads are numbered
from 1 to M in the order of description. Next line contains an integer
Q which denotes the quantity of threads Usatiy-Polosatiy wants to tear
(1 ≤ Q ≤ M). The last line contains numbers of these threads —
different integers separated by spaces.

### Output
Output Q integers — the number of pieces in Anansi's cobweb after each
of Usatiy-Polosatiy's action. Separate numbers with single spaces. 

