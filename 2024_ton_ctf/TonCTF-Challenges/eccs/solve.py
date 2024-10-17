class ECCBreaker:
    def __init__(self):
        self.p = 738077334260605249  # 橢圓曲線的素數模數
        self.a = 1  # 橢圓曲線的 a 值
        self.b = 2  # 橢圓曲線的 b 值
        self.p1 = (627636259244800403, 317346088871876181)  # 起點 p1
        self.p2 = (456557409365020317, 354112687690635257)  # 目標點 p2

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
        return q

    def add(self, P, Q):
        """橢圓曲線上的兩點加法"""
        x1, y1 = P
        x2, y2 = Q

        if x1 == 0 and y1 == 0:
            return Q
        if x2 == 0 and y2 == 0:
            return P

        if x1 == x2 and y1 == y2:
            s = ((3 * (x1 * x1) + self.a) * self.inv_mod(2 * y1, self.p)) % self.p
            x3 = (s * s - 2 * x1) % self.p
            y3 = (s * (x1 - x3) - y1) % self.p
        else:
            s = ((y2 - y1) * self.inv_mod(x2 - x1, self.p)) % self.p
            x3 = (s * s - x1 - x2) % self.p
            y3 = (s * (x1 - x3) - y1) % self.p

        return (x3 % self.p, y3 % self.p)

    def brute_force_key(self):
        """遞增暴力破解 k"""
        k = 0
        current_point = (0, 0)  # 開始點為 (0, 0)
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
