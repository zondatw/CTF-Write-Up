import { Address, contractAddress } from "@ton/core";
import { TonClient4 } from "@ton/ton";
import { ECC } from "./output/ECC_ECC";

(async () => {
    const client = new TonClient4({
        endpoint: "https://sandbox-v4.tonhubapi.com", // 🔴 Test-net API endpoint
        // endpoint: "http://65.21.223.95:8081/jsonRPC",
    });

    // open the contract address
    let init = await ECC.init(BigInt(1));
    let workchain = 0; //we are working in basechain.
    let contract_address = contractAddress(workchain, init);
    // let contract_address = Address.parse("UQBpyyPRr1dZM7SGdY74F8Egd7V-hWlx3_o292sWdR9jqmCM")
    let contract = await ECC.fromAddress(contract_address);
    let contract_open = await client.open(contract);

    let pResult = await contract_open.getCheck(BigInt(2));
    console.log(`Counter Value: ${pResult.x} ${pResult.y}`);
    let isSolve = await contract_open.getIsSolved();
    console.log(`Is Solved: ${isSolve}`);
})();
