
    const CLAIM_AMOUNT: Int = 1;
    const INIT_SUPPLY: Int = 30000;

    message UserStake{
        amount: Int;
    }

    message UserWithdraw{
        amount: Int;
    }

    message StakeEvent{
        sender: Address;
        amount: Int;
    }

    contract AirDrop {

        total_balance: Int as uint256;
        user_info: map<Address, Int>;
        user_claim_info: map<Address, Bool>;

        init(version: Int) {
            self.user_info = emptyMap();
            self.total_balance = INIT_SUPPLY;
        }

        receive("AirDrop") {
            require(self.user_claim_info.get(sender()) == null, "Have claimed");
            let user_staked: Int = 0;
            if (self.user_info.get(sender()) != null) {
                user_staked = self.user_info.get(sender())!!;
            }
            self.total_balance = self.total_balance - CLAIM_AMOUNT;
            self.user_info.set(sender(), user_staked + CLAIM_AMOUNT);
            self.user_claim_info.set(sender(), true);
        }

        receive(msg: UserStake) {
            require(context().value > msg.amount, "Incorrect TON value");
            let user_staked: Int = 0;
            if (self.user_info.get(sender()) != null) {
                user_staked = self.user_info.get(sender())!!;
            }
            self.total_balance = self.total_balance + msg.amount;
            self.user_info.set(sender(), user_staked + msg.amount);
        }

        receive(msg: UserWithdraw) {
            require(self.user_info.get(sender()) != null && self.user_info.get(sender())!! != 0, "Nothing to withdraw");
            let user_staked: Int = 0;
            user_staked = self.user_info.get(sender())!!;
            require(msg.amount <= user_staked, "Insufficient balance");
            self.total_balance = self.total_balance - msg.amount;
            if (msg.amount == user_staked) {
                self.user_info.del(sender());
            } else {
                self.user_info.set(sender(), user_staked - msg.amount);
            }
        }

        get fun balance(): Int {
            return self.total_balance;
        }

        get fun is_solved(): Bool {
            return self.total_balance == 0;
        }



    }

