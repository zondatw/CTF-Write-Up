# solve


## setup

```shell
$ yarn deploy
yarn run v1.22.22
$ ts-node ./sources/deploy.ts

EQCZUERmve5FUsuHkT5VYzkn-nDnp150p23hvJ1_D25Ji1H_
🛠️ Preparing new outgoing massage from deployment wallet.
EQCZUERmve5FUsuHkT5VYzkn-nDnp150p23hvJ1_D25Ji1H_
Seqno:  3581

Current deployment wallet balance =  17.152034555 💎TON
====== Deployment message sent to =======
 EQDOIOKz1O5YmvjbRnMt1XAcTXqwUEclxuonRFVsMYNbOLGI
✨  Done in 3.99s.
```

## solved

```shell
$ yarn solve-prod
yarn run v1.22.22
$ ts-node ./sources/solve.prod.ts
mnemonics:
EQCZUERmve5FUsuHkT5VYzkn-nDnp150p23hvJ1_D25Ji1H_
Counter Value: 0
Is Solved: false
✨  Done in 2.73s.
$ yarn solve-prod
yarn run v1.22.22
$ ts-node ./sources/solve.prod.ts
mnemonics:
EQCZUERmve5FUsuHkT5VYzkn-nDnp150p23hvJ1_D25Ji1H_
Counter Value: 100
Is Solved: true
✨  Done in 2.59s.
```