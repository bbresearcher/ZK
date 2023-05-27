# Creating proofs with Zokrates.
## Prerequisites
- Foundry [https://book.getfoundry.sh/getting-started/installation](https://book.getfoundry.sh/getting-started/installation)
- Zokrates [https://zokrates.github.io/gettingstarted.html](https://zokrates.github.io/gettingstarted.html)
- VS code

## Create proving code in Zokrates
Zokrates allows us to create a proving function to assert that the proof provided is true.
This tutorial is a really basic introduction to ZK-Proofs<br>
In our example project we will create a zokrates function to verify the proof, and also write a `Foundry` test in order to test the resulting proof.
## First create the off-chain verfying code
In our very basic example we will create two inputs, the first one must be exactly double the second one.<br><br>
**Steps to follow along**<br>
1. Create a directory **mkdir zk_demo**.
2. **forge init --no-git** to initialize the `Foundry` structure.
3. Create a second folder to mimic the folder of someone wishing to send a proof. **mkdir prover**.
4. In the base directory of the **zk_demo** folder create a file called **isdouble.zok**.
5. Paste the code below into the **isdouble.zok** and save it. The code takes two inputs, the first value is expected to be double the second value.
```

def main(public field doulbedVal, public field inputVal) {
	assert(doulbedVal == inputVal * 2);
}
```
6. Compile **isdouble.zok**. Do this by typing the terminal command **zokrates compile -i isdouble.zok -o isdouble**
7. Create the needed key files to share with any prover **zokrates setup -i isdouble**, this will result in two files called **verification.key** and **proving.key**
8. Copy the **proving.key** and **isdouble.zok** to the **prover** folder.

## Create the Solidity file to test our verification on chain.
We can use `Zokrates'` built in function to export our verification code as a soldity contract.
1. In the base directory **zk_demo** type the command **zokrates export-verifier**, this will result in a file called **verifier.sol**.
2. Move **verfier.sol** to the **src** directory of the `Foundry structure`.

We are now ready to move on to how a `Prover` would interact with the proving code given.

## Generate a proof using Zokrates.
A prover would need to generate a `proof` to send to the verifier. We will use Zokrates to generate this proof.<br><br>
**Steps**<br>
1. Move into the **prover** directory, which should contain the files **isdouble.zok** and **proving.key**.
2. Compile the **.zok** file, **zokrates compile -i isdouble.zok -o isdouble**
3. Create a wtiness (you can read more about this on the zokrates book in the link on top). **zokrates compute-witness --verbose -i isdouble -a 4 2**, The -a is the values that need to be sent into the isdouble code , so the first number needs to be double the second number, ie 4 2 , or 16 8.
4. **We can finally generate our proof**, type the command **zokrates generate-proof -i isdouble**, this will output a file called **proof.json**.

## Verifying our proof before we try it on-chain
We can copy the resulting **proof.json**, back into the root folder **zk_demo** which should contain our file called **verification.key**.

If we type the command **zokrates verify** we should get the output
```text
Performing verification...
PASSED
```
# Testing our code on-chain
To test our code on-chain we will use `Foundry` so that there is no need to deploy to testnets in order to keep the tutorial as easy as possible.

## Foundry test file
In the `Foundry` folder structure there should be a directory called `test`, and inside the `test` directory a file called `Counter.t.sol`, this is placed there by the `forge init` command and can be deleted.<br><br>
**Steps**<br><br>
1. Create a file called `Verifier.t.sol`
2. Paste the code below into the file and save.
3. **We will discuss what needs to be changed in to the file below the code block**

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import {Verifier,Pairing} from "../src/verifier.sol";
import "../src/verifier.sol";

contract VerifierTest is Test {
    Verifier public verifier;

    function setUp() public {
        verifier = new Verifier();
    }

    function testProof() public {
        Verifier.Proof memory proof;
        Pairing.G1Point memory a = Pairing.G1Point(uint256(0x0..ADD VALUES HERE{1}),uint256(0x0..ADD VALUES HERE{2}));
        Pairing.G2Point memory b = Pairing.G2Point([uint256(0x0..ADD VALUES HERE{3}),uint256(0x0..ADD VALUES HERE{4})],[uint256(0x0..ADD VALUES HERE{5}),uint256(0x0..ADD VALUES HERE{6})]);
        Pairing.G1Point memory c = Pairing.G1Point(uint256(0x0..ADD VALUES HERE{7}),uint256(0x0..ADD VALUES HERE{8}));
        proof.a = a;
        proof.b = b;
        proof.c = c;
	//IF YOU CHANGE THE NUMBERS YOU WILL NEED TO REGENERATE THE PROOF, SO ONLY ENTER THE NUMBER YOU USED TO CREATE THE WITNESS
        uint256 doubledVal = 4;
        uint256 inputVal = 2;
        uint256[2] memory invals = [doubledVal,inputVal];
        bool resp = verifier.verifyTx(proof,invals);
        assertTrue(resp);
    }

}
```
4. In the **proof.json** file that was created we need to copy and paste the values into the **Pairing.G1Point** and **Pairing.G2Point** areas in the code marked **ADD VALUES HERE{NUM}**.
5. I have marked an example proof file below to show which values need to go into which parts of the `Foundry` test contract.

```text
{
  "scheme": "g16",
  "curve": "bn128",
  "proof": {
    "a": [
      "0x0..COPY VALUES HERE{1}",
      "0x0..COPY VALUES HERE{2}"
    ],
    "b": [
      [
        "0x0..COPY VALUES HERE{3}",
        "0x0..COPY VALUES HERE{4}"
      ],
      [
        "0x0..COPY VALUES HERE{5}",
        "0x0..COPY VALUES HERE{6}"
      ]
    ],
    "c": [
      "0x0..COPY VALUES HERE{7}",
      "0x0..COPY VALUES HERE{8}"
    ]
  },
  "inputs": [
    "0x0000000000000000000000000000000000000000000000000000000000000004",
    "0x0000000000000000000000000000000000000000000000000000000000000002"
  ]
}
```

6. Run the test **forge test -vv**

If all goes well you should see the output below
```
[⠊] Compiling...
[⠘] Compiling 1 files with 0.8.20
[⠊] Solc 0.8.20 finished in 1.66s
Compiler run successful!

Running 1 test for test/Verifier.t.sol:VerifierTest
[PASS] testProof() (gas: 221270)
Test result: ok. 1 passed; 0 failed; finished in 60.43ms
```

## IF YOU FOLLOWED ALONG THIS FAR -- THANK YOU --
