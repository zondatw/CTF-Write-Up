import { Address, contractAddress, Sender } from "@ton/core";
import { beginCell, toNano, WalletContractV4, internal, fromNano } from "@ton/ton";
import { mnemonicToPrivateKey } from "ton-crypto";
import { TonClient4 } from "@ton/ton";
import { ECC, Key, storeKey } from "./output/ECC_ECC";

(async () => {
    const client = new TonClient4({
        endpoint: "https://sandbox-v4.tonhubapi.com", // 🔴 Test-net API endpoint
        // endpoint: "http://65.21.223.95:8081/jsonRPC",
    });

    // open the contract address
    let init = await ECC.init(BigInt(1));
    let workchain = 0; //we are working in basechain.
    let contract_address = contractAddress(workchain, init);
    // let contract_address = Address.parse("UQBpyyPRr1dZM7SGdY74F8Egd7V-hWlx3_o292sWdR9jqmCM");
    let contract = await ECC.fromAddress(contract_address);
    let contract_open = await client.open(contract);


    const key_payload: Key = {$$type: "Key", k: 2n};
    const body = beginCell().store(storeKey(key_payload)).endCell();


    let mnemonics = (process.env.mnemonics_2 || "").toString(); // 🔴 Change to your own, by creating .env file!
    console.log(`mnemonics: ${mnemonics}`);
    //return;

    let keyPair = await mnemonicToPrivateKey(mnemonics.split(" "));
    let secretKey = keyPair.secretKey;
    let deployer_wallet = WalletContractV4.create({ workchain, publicKey: keyPair.publicKey });
    console.log(deployer_wallet.address);

    let deployer_wallet_contract = client.open(deployer_wallet);
    let seqno: number = await deployer_wallet_contract.getSeqno();
    let sendAmount = toNano("1");
    console.log(`seqno: ${seqno}`);

    let response = await contract_open.send(
        deployer_wallet_contract.sender(secretKey),
        {value: sendAmount},
        {
            $$type: "Key",
            k: 2n
        }
    );

    // let response = await deployer_wallet_contract.sendTransfer({
    //     seqno,
    //     secretKey,
    //     messages: [
    //         internal({
    //             to: contract_address,
    //             value: sendAmount,
    //             body: body,
    //         }),
    //     ],
    // });
    console.log(`response: ${response}`);

    let isSolve = await contract_open.getIsSolved();
    console.log(`Is Solved: ${isSolve}`);

})();
