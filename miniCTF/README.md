[SOLUTION WALKTHROUGH](./solution.md)
# MINI CTF
## There is no prize it's just to learn.
The files needed are in a folder called **prover** in this repo.<br>
I have created a mini CTF on the sepolia network.<br>
[https://sepolia.etherscan.io/address/0x37dEA441346447b271c372Bd21dEc2347aB6d0f4](https://sepolia.etherscan.io/address/0x37dEA441346447b271c372Bd21dEc2347aB6d0f4)<br>
The aim of the CTF is to generate and submit a proof, that you know the keccak256 hash of the yAcademy website **https://yacademy.dev/** URL, which you then casted into a uint256.<br>
## HINT: The number starts with 1113 and ends with 929.
## Helpful links:
[https://docs.circom.io/getting-started/computing-the-witness/](https://docs.circom.io/getting-started/computing-the-witness/)<br>
[https://docs.circom.io/getting-started/proving-circuits/](https://docs.circom.io/getting-started/proving-circuits/)<br><br>
You need to use snarkjs to genearate a witness and proof file, and then submit this to the verifier.<br>
You can use REMIX to interact with `CTFVerifier.sol` supplied in the **prover** directory of this repo at the address **0x37dEA441346447b271c372Bd21dEc2347aB6d0f4**<br><br>
If the proof submitted is correct it will return ***true*** on the call to the function `verifyProof`.<br>
![It Worked](itworked.png)<br><br>
## DISCLAIMER: Do not use any of this code in production it's just an example. always verify software, DO NOT just install software you think you may need without double checking, so if you install anything based on this CTF it is at your own risk.
