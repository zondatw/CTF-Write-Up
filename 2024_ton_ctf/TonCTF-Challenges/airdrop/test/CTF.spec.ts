import { Blockchain, SandboxContract, TreasuryContract } from '@ton/sandbox';
import { toNano } from '@ton/core';
import { AirDrop } from '../sources/output/Airdrop_AirDrop';
import '@ton/test-utils';

describe('Playground', () => {
    let blockchain: Blockchain;
    let deployer: SandboxContract<TreasuryContract>;
    let airdrop: SandboxContract<AirDrop>;

    beforeEach(async () => {
        blockchain = await Blockchain.create();

        airdrop = blockchain.openContract(await AirDrop.fromInit(1n));

        deployer = await blockchain.treasury('deployer');

        // Deploy the contract with some initial funds
        const deployResult = await airdrop.send(
            deployer.getSender(),
            {
                value: toNano('0.05'),
            },
            {
                $$type: 'UserStake',
                amount: -30000n,
            }
        );

        expect(deployResult.transactions).toHaveTransaction({
            from: deployer.address,
            to: airdrop.address,
            deploy: true,
            success: true,
        });

        const balance = await airdrop.getBalance();
        console.log(`balance: ${balance}`);

        const isSolved = await airdrop.getIsSolved();
        expect(isSolved).toBe(true);
    });

    it('should deploy the AirDrop contract successfully', async () => {
        // Deployment success is already checked in beforeEach
        // This is just a placeholder test
    });

});
