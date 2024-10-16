import { Blockchain, SandboxContract, TreasuryContract } from '@ton/sandbox';
import { toNano } from '@ton/core';
import { ECC } from '../sources/output/ECC_ECC';
import '@ton/test-utils';

describe('Playground', () => {
    let blockchain: Blockchain;
    let deployer: SandboxContract<TreasuryContract>;
    let ecc: SandboxContract<ECC>;

    beforeEach(async () => {
        blockchain = await Blockchain.create();

        ecc = blockchain.openContract(await ECC.fromInit(1n));

        deployer = await blockchain.treasury('deployer');

        const deployResult = await ecc.send(
            deployer.getSender(),
            {
                value: toNano('0.05'),
            },
            {
                $$type: 'Deploy',
                queryId: 0n,
            }
        );

        expect(deployResult.transactions).toHaveTransaction({
            from: deployer.address,
            to: ecc.address,
            deploy: true,
            success: true,
        });
    });

    it('should deploy', async () => {
        // the check is done inside beforeEach
        // blockchain and playground are ready to use
    });

    it('send key', async () => {
        const res = await ecc.send(
            deployer.getSender(),
            { value: toNano('0.5') },
            {
                $$type: "Key",
                k: 2n,
            },
        );

        // console.log(res);
        // We'll need only the body of the observed message:
        const firstMsgBody = res.externals[0].body;
        
        // Now, let's parse it, knowing that it's a text message.
        // NOTE: In a real-world scenario,
        //       you'd want to check that first or wrap this in a try...catch
        const firstMsgText = firstMsgBody.asSlice().loadStringTail().replace(/\u0000/g, '');
        
        // "But to the Supes? Absolutely diabolical."
        console.log(firstMsgText);

        const resSolve = await ecc.getIsSolved();

        console.log("Address of our contract: " + ecc.address);
        console.log(`solve status: ${resSolve}`);
    });

    it('get solve', async () => {
        const res = await ecc.getIsSolved();

        console.log("Address of our contract: " + ecc.address);
        console.log(res);
    });
});
