pragma solidity >=0.7.0 <0.9.0;

import "./Verifier.sol";
contract CTFVerifier {
    Groth16Verifier _verifier;

    constructor(){
        _verifier = Groth16Verifier(0x5958d140A16587e117affE9c2dF3A79A3bABb133);
    }

    function verifyProof(uint[2] calldata _pA, uint[2][2] calldata _pB, uint[2] calldata _pC, uint[1] calldata _pubSignals) public view returns (bool) {
        return _verifier.verifyProof(_pA,_pB,_pC,_pubSignals);
    }
}
