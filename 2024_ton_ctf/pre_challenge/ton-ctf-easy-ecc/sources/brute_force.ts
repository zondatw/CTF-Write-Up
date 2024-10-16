import { Address, contractAddress } from "@ton/core";
import { beginCell, toNano, WalletContractV4, internal, fromNano } from "@ton/ton";
import { mnemonicToPrivateKey } from "ton-crypto";
import { TonClient4 } from "@ton/ton";
import { ECC } from "./output/ECC_ECC";

(async () => {
    const client = new TonClient4({
        endpoint: "https://sandbox-v4.tonhubapi.com", // 🔴 Test-net API endpoint
    });

    // open the contract address
    let init = await ECC.init(BigInt(1));
    let workchain = 0; //we are working in basechain.
    let contract_address = contractAddress(workchain, init);
    let contract = await ECC.fromAddress(contract_address);
    let contract_open = await client.open(contract);

    for (let testData = 0; testData < 1000000000000000000; testData++) {
        try {
            let pResult = await contract_open.getCheck(BigInt(testData));
            console.log(`Counter Value: (${testData}) ${pResult.x} ${pResult.y}`);
            if (pResult.x === BigInt("588309170674817669") && pResult.y === BigInt("301293331892257609")) {
                break;
            }
        } catch (e) {
            // console.log(`Error history: (${testData})`);
            // console.log(`Error: ${e}`);
        }
    }
    let isSolve = await contract_open.getIsSolved();
    console.log(`Is Solved: ${isSolve}`);

})();
