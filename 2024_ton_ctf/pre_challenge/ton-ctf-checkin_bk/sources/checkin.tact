contract Checkin {
    counter: Int;

    init(c: Int) {
        self.counter = 0;
    }

    receive("increase: 1") {
        self.counter = self.counter + 1;
    }

    receive("set") {
        self.counter = 100;
    }

    get fun get_counter(): Int {
        return self.counter;
    }

    get fun is_solved(): Bool {
        return self.counter == 100;
    }
}
