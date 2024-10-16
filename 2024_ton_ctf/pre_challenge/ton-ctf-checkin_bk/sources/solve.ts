import { Address, contractAddress } from "@ton/core";
import { beginCell, toNano, WalletContractV4, internal, fromNano } from "@ton/ton";
import { mnemonicToPrivateKey } from "ton-crypto";
import { TonClient4 } from "@ton/ton";
import { Checkin } from "./output/Checkin_Checkin";

(async () => {
    const client = new TonClient4({
        endpoint: "https://sandbox-v4.tonhubapi.com", // 🔴 Test-net API endpoint
        // endpoint: "http://65.21.223.95:8081/jsonRPC",
    });

    // open the contract address
    let init = await Checkin.init(BigInt(1));
    let workchain = 0; //we are working in basechain.
    let contract_address = contractAddress(workchain, init);
    let contract = await Checkin.fromAddress(contract_address);
    let contract_open = await client.open(contract);

    let mnemonics = (process.env.mnemonics_2 || "").toString(); // 🔴 Change to your own, by creating .env file!
    console.log(`mnemonics: ${mnemonics}`);
    //return;

    let keyPair = await mnemonicToPrivateKey(mnemonics.split(" "));
    let secretKey = keyPair.secretKey;
    let deployer_wallet = WalletContractV4.create({ workchain, publicKey: keyPair.publicKey });
    console.log(deployer_wallet.address);

    let deployer_wallet_contract = client.open(deployer_wallet);
    let seqno: number = await deployer_wallet_contract.getSeqno();
    let sendAmount = toNano("0.01");

    await deployer_wallet_contract.sendTransfer({
        seqno,
        secretKey,
        messages: [
            internal({
                to: contract_address,
                value: sendAmount,
                body: 'set',
            }),
        ],
    });
    
    console.log("Counter Value: " + (await contract_open.getGetCounter()));
    console.log("Is Solved: " + (await contract_open.getIsSolved()));

})();
