import "@stdlib/deploy";


message DrawNFT{
    luckynumber: Int;
}

contract Receivers with Deployable {
    
    flag: Int = 0;

    init (c: Int) {
        
    }

    receive(msg:DrawNFT){
        let c: Cell = beginCell().storeAddress(myAddress()).storeAddress(sender()).storeUint(now(), 64).endCell();
        let verify: Int = c.hash();
        let key: Int = 0; 

        if ( msg.luckynumber > 0 ) {
            key = verify % 100;
            if ( msg.luckynumber == key ){
                self.notify("Congratulations on winning the prize!".asComment());
                self.flag = 1;
            }
            self.notify("no success yet!".asComment());
        } 
    }

    get fun is_solved():Bool{
        if(self.flag>0){
            return true;
        }
        return false;
    }

}