import "@stdlib/deploy";

struct Point {
    x: Int;
    y: Int;
}

message Key {
    k: Int
}

contract ECC with Deployable {

    is_solve: Bool;
    p: Int;
    a: Int;
    b: Int;
    for_init: Int;

    init(for_init: Int) {
        self.p = 738077334260605249;
        self.a = 1;
        self.b = 2;
        self.is_solve = false;
        self.for_init = for_init;

    }

    fun invMod(_x: Int, _pp: Int): Int {
        _x = _x % _pp;
        let q: Int = 0;
        let newT: Int = 1;
        let r: Int = _pp;
        let t: Int = 0;
        while (_x != 0) {
            t = r / _x;
            let tmp2: Int = newT;
            newT = ((q + (_pp - ((t * newT )% _pp)) %  _pp));
            q = tmp2;

            let tmp: Int = _x;
            _x = r - t * _x;
            r = tmp;
        }
        return q
    }


    fun add(P: Point, Q: Point) :Point {
        let x1: Int = P.x;
        let y1: Int = P.y;
        let x2: Int = Q.x;
        let y2: Int = Q.y;
        let x3: Int = 0;
        let y3: Int = 0;

        if (x1 == 0 && y1 == 0) {
            return Q;
        }

        if (x2 == 0 && y2 == 0) {
            return P;
        }

        if (x1 == x2 && y1 == y2) {
            let s: Int = (((3 * (x1 * x1) + self.a) % self.p) * self.invMod(2 * y1, self.p) % self.p);
            x3 = (((s * s) % self.p) - 2 * x1);
            y3 = (s * (x1 - x3)) % self.p - y1;
            return Point{x: x3 % self.p, y: y3 % self.p};
        } else {
            let s: Int = ((y2 - y1) * self.invMod(x2 - x1, self.p) % self.p);
            x3 = (s * s) % self.p - x1 - x2;
            y3 = (s * (x1 - x3)) % self.p - y1;
            return Point{x: x3 % self.p, y: y3 % self.p};
        }

    }

    fun scalar_multiplication(P: Point, n: Int): Point {
        let Q:Point = Point{x:0, y:0};
        dump(n);
        while (n > 0) {
            if (n % 2 == 1) {
                Q = self.add(Q, P);
            }
            P = self.add(P, P);
            n = n >> 1;
        }
            
        return Q
    }

    receive(msg: Key){
        let p1: Point = Point{x: 627636259244800403, y: 317346088871876181};
        let p2: Point = Point{x: 456557409365020317, y: 354112687690635257};
        let ans: Point = self.scalar_multiplication(p1, msg.k);
        if (ans.x == p2.x && ans.y == p2.y) {
            self.is_solve = true;
        }
    }

    get fun check(k: Int): Point {
        let p1: Point = Point{x: 627636259244800403, y: 317346088871876181};
        return self.scalar_multiplication(p1, k);
    }

    get fun is_solved(): Bool {
        return self.is_solve;
    }

}