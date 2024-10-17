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

    it('solve', async () => {
        const res = await ecc.send(
            deployer.getSender(),
            { value: toNano('1') },
            {
                $$type: "Key",
                k: 844279n,
            },
        );
        const resSolve = await ecc.getIsSolved();

        console.log("Address of our contract: " + ecc.address);
        console.log(`solve status: ${resSolve}`);
        expect(resSolve).toBe(true);
    });
});
