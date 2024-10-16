import { Blockchain, SandboxContract, TreasuryContract } from '@ton/sandbox';
import { toNano } from '@ton/core';
import { Receivers } from '../sources/output/CTF_Receivers';
import '@ton/test-utils';

describe('Playground', () => {
    let blockchain: Blockchain;
    let deployer: SandboxContract<TreasuryContract>;
    let receiver: SandboxContract<Receivers>;

    beforeEach(async () => {
        blockchain = await Blockchain.create();

        receiver = blockchain.openContract(await Receivers.fromInit(1n));

        deployer = await blockchain.treasury('deployer');

        const deployResult = await receiver.send(
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
            to: receiver.address,
            deploy: true,
            success: true,
        });
    });

    it('should deploy', async () => {
        // the check is done inside beforeEach
        // blockchain and playground are ready to use
    });

    it('solve', async () => {

        for (let i = 0; i <= 100; i++) {
            const res = await receiver.send(
                deployer.getSender(),
                { value: toNano('0.5') },
                {
                    $$type: "DrawNFT",
                    luckynumber: BigInt(i),
                },
            );
            const resSolve = await receiver.getIsSolved();
            if (resSolve) {
                break;
            }
        }

        const resSolve = await receiver.getIsSolved();
        console.log("Address of our contract: " + receiver.address);
        console.log(`solve status: ${resSolve}`);
        expect(resSolve).toBe(true);
    });
});
