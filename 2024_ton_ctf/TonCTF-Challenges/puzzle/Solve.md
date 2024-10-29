# Solve

## Guess

看起來就是要做一堆指令去達到和為 638，但比較麻煩的是不是每個指令都會有 pc 的變化，變成暴力破解有點麻煩，但想到以前打 CTF 時有個好東西，叫 Z3 ，所以用它來破吧

## Solved

```shell
$ python3 solve.py
Solution found: [op2 = 0,
 op4 = 0,
 op6 = 5,
 op7 = 0,
 op5 = 2,
 op1 = 0,
 op3 = 6]
```

```shell
$ yarn test
yarn run v1.22.22
$ jest
  console.log
    Address of our contract: EQAfpKEnvzQIW-MsOV7mWZHQrLnoc94aSox3SZR9Svmq3Bs_

      at Object.<anonymous> (test/puzzle.spec.ts:73:17)

  console.log
    solve status: true

      at Object.<anonymous> (test/puzzle.spec.ts:74:17)

 PASS  test/puzzle.spec.ts
  Playground
    ✓ should deploy (133 ms)
    ✓ solve (144 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        0.927 s, estimated 1 s
Ran all test suites.
✨  Done in 1.57s.
```