let encoder = function(data, mapping_int, mapping) {
   OA = new Date().getHours()
    YA = function() {
        return [1879, 1921, 1952, 1976, 2018].reduce((function(E, I) {
            return E + Number(new Date('7/1/'.concat(I)))
        }
        ), 0)
    }
    YA = YA()

    NA = performance.timeOrigin
    fA = Math.floor(254 * Math.random())
    LA = 1 + ((1664525 * ((cA = ~~((SA = (YA + OA + NA) * fA) + 1111602120)) < 0 ? 1 + ~cA : cA) + 1013904223) % 4294967296 / 4294967296 * 82 | 0)

    zA = 83

    oA = function(A, Q) {
        for (var E, I, C = ~~(A + mapping_int), g = C < 0 ? 1 + ~C : C, D = {}, M = mapping.split(""), w = zA; w; )
            E = (g = 1103515245 * g + 12345 & 2147483647) % w,
            I = M[w -= 1],
            M[w] = M[E],
            M[E] = I,
            D[M[w]] = (w + Q) % zA;
        return D[M[0]] = (0 + Q) % zA,
        [D, M.join("")]
    }(SA, LA)

    nA = oA[0]
    rA = oA[1]

    xA = /[a-z\d.,/#!$%^&*;:{}=\-_~()\s]/i

    function encode(A) {
        var Q, B, E, I, C, D;
        return (I = "" + A,
        C = rA,
        D = I.length,
        I + C.substring(D, zA)).split(" ").reverse().join(" ").split("").reverse().map((Q = LA,
        B = rA,
        E = nA,
        function(A) {
            var I, C;
            return A.match(xA) ? B[(I = Q,
            C = E[A],
            (C + I) % zA)] : A
        }
        )).join("")
    }
    return encode(data)
}
let map = "(Fb&CNBV73xWc1YGzRO$#oJ2Dpn-X/Kvs;qu8!:Ei_m6)Te*^Zkyw.lA=h,9jrH%fI ~SU}{L4PaM0g5tQd" // this changes for each version, use logic from encoder.py to retrieve it eg: use map.json
let map_int = 1111602120 // this changes for each version, use logic from encoder.py to retrieve it eg: use map.json

let e = encoder(map_int, map,'ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x00009A49) Direct3D11 vs_5_0 ps_5_0, D3D11)')
console.log(e)
