class ECCBreaker:
    def __init__(self):
        self.p = 1124575627794835616567  # 橢圓曲線的素數模數
        self.a = 7289870645149292820  # 橢圓曲線的 a 值
        self.b = 871152686138947806299  # 橢圓曲線的 b 值
        self.zero = (26268578989036317972, 447359380003772275836)  # 起始點 zero
        self.p1 = (983810924364991907519, 411824424919437929939)  # 起始點 p1
        self.p2 = (1098402780140240490917, 1079661110557516547244)  # 目標點 p2

    def inv_mod(self, x, pp):
        """模逆運算"""
        x = x % pp
        q, newT, r = 0, 1, pp
        t = 0
        while x != 0:
            t = r // x
            tmp2 = newT
            newT = (q + (pp - (t * newT % pp)) % pp) % pp
            q = tmp2

            tmp = x
            x = r - t * x
            r = tmp
        return q % self.p

    def add(self, P, Q):
        """橢圓曲線加法"""
        x1, y1 = P
        x2, y2 = Q
        if x1 == 0 and y1 == 0:
            return Q
        if x2 == 0 and y2 == 0:
            return P

        if x1 == x2 and y1 == y2:
            m = (self.a * ((x1 + x2) % self.p) + self.b) % self.p
        else:
            m = ((y2 - y1) * self.inv_mod(x2 - x1, self.p)) % self.p

        x3 = (((m - self.b) * self.inv_mod(self.a, self.p)) % self.p - self.zero[0]) % self.p
        y3 = (((x3 - self.zero[0]) * m) % self.p + self.zero[1]) % self.p
        return (x3 % self.p, y3 % self.p)

    def brute_force_key(self):
        """遞增暴力破解k"""
        k = 0
        current_point = (0, 0)  # 初始為 (0, 0)
        
        while True:
            # 每次遞增一個 p1
            current_point = self.add(current_point, self.p1)
            
            if current_point == self.p2:
                print(f"Found key: {k + 1}")
                break
            k += 1

if __name__ == "__main__":
    breaker = ECCBreaker()
    breaker.brute_force_key()
