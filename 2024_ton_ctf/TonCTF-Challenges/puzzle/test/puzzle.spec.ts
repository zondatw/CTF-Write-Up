import { Blockchain, SandboxContract, TreasuryContract } from '@ton/sandbox';
import { toNano } from '@ton/core';
import { Puzzle } from '../sources/output/Puzzle_Puzzle';
import '@ton/test-utils';

describe('Playground', () => {
    let blockchain: Blockchain;
    let deployer: SandboxContract<TreasuryContract>;
    let puzzle: SandboxContract<Puzzle>;

    beforeEach(async () => {
        blockchain = await Blockchain.create();

        puzzle = blockchain.openContract(await Puzzle.fromInit(1n));

        deployer = await blockchain.treasury('deployer');

        const deployResult = await puzzle.send(
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
            to: puzzle.address,
            deploy: true,
            success: true,
        });
    });

    it('should deploy', async () => {
        // the check is done inside beforeEach
        // blockchain and playground are ready to use
    });

    it('solve', async () => {

        for (let i = 0; i < 2; ++i) {
            await puzzle.send(
                deployer.getSender(),
                { value: toNano('0.05') },
                "Opeorate5"
            );
        }
        for (let i = 0; i < 6; ++i) {
            await puzzle.send(
                deployer.getSender(),
                { value: toNano('0.05') },
                "Opeorate3"
            );
        }
        for (let i = 0; i < 5; ++i) {
            await puzzle.send(
                deployer.getSender(),
                { value: toNano('0.05') },
                "Opeorate6"
            );
        }

        await puzzle.send(
            deployer.getSender(),
            { value: toNano('0.05') },
            "Check"
        );

        const resSolve = await puzzle.getIsSolved();
        console.log("Address of our contract: " + puzzle.address);
        console.log(`solve status: ${resSolve}`);
        expect(resSolve).toBe(true);
    });
});
