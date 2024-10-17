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
    for_init: Int;
    a:Int;
    b:Int;
    zero:Point;

    init(for_init: Int) {
        self.p = 1124575627794835616567;
        self.a = 7289870645149292820;
        self.b = 871152686138947806299;
        self.zero = Point{x:26268578989036317972,y:447359380003772275836};
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
        return q % self.p;
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
        let m: Int = 0;
        if (x1 == x2 && y1 == y2) {
            m = ((self.a * ((x1 + x2) % self.p) % self.p) + self.b) % self.p;
        } else {
            m = (((y2 - y1) % self.p) * self.invMod(x2 - x1, self.p)) % self.p;
        }
        x3 = ((((m-self.b)*self.invMod(self.a,self.p))%self.p) - self.zero.x) % self.p;
        y3 = (((x3 - self.zero.x)*m)%self.p + self.zero.y)%self.p;
        return Point{x: x3 % self.p, y: y3 % self.p};
    }

    fun scalar_multiplication(P: Point, n: Int): Point {
        let Q:Point = Point{x:0, y:0};

        while (n > 0) {
            if (n % 2 == 1) {
                Q = self.add(Q, P);
            }
            P = self.add(P, P);
            n = n >>1;
        }
            
        return Q
    }

    receive(msg: Key){
        let p1: Point = Point{x: 983810924364991907519, y: 411824424919437929939};
        let p2: Point = Point{x: 1098402780140240490917, y: 1079661110557516547244};
        let ans: Point = self.scalar_multiplication(p1, msg.k);
        if (ans.x == p2.x && ans.y == p2.y) {
            self.is_solve = true;
        }
    }

    get fun check(k: Int): Point {
        let p1: Point = Point{x: 983810924364991907519, y: 411824424919437929939};
        return self.scalar_multiplication(p1, k);
    }

    get fun is_solved(): Bool {
        return self.is_solve;
    }

}