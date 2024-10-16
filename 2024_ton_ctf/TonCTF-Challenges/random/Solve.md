# Solve

## Guess

看到題目內容，應該是拿 sender 的 address 做完 hash 後再 mod 100 ，如果與傳進來的值，就通過。

## solved

```shell
$ yarn test
yarn run v1.22.22
$ jest
  console.log
    Address of our contract: EQCKUaJ2AcLilwywCfPgvGOWayDJNoYfVH6e6P5DCCyLIsDG

      at Object.<anonymous> (test/CTF.spec.ts:73:17)

  console.log
    solve status: true

      at Object.<anonymous> (test/CTF.spec.ts:74:17)

 PASS  test/CTF.spec.ts
  Playground
    ✓ should deploy (129 ms)
    ✓ send drawNFT (353 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        1.066 s, estimated 2 s
Ran all test suites.
✨  Done in 1.52s.
```