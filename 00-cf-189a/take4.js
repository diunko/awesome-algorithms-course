
var numbers = readline().split(" ").map(function(x) { return parseInt(x); });

var N = numbers[0]
var nn = numbers.slice(1).sort()
var a = nn[0], b = nn[1], c = nn[2]

print(slow(a,b,c,N))

function slow(a,b,c,N) {
  var S = 0
  var S0 = 0
  var x = Math.floor(N/a)
  while(-1<x){
    var z = Math.floor((N-x*a)/c)
    while(-1<z){
      var y = Math.floor((N-x*a-z*c)/b)
      if (x*a+y*b+z*c === N) {
        S0 = x+y+z
        if (S0 > S) {
          S = S0
        }
      }
      z-=1
    }
    x-=1
  }
  return S
}

