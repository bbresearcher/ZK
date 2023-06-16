## Circom Audit Checklist

## Language checks
- [ ] Check for over/underflows (21888242871839275222246405745257275088548364400416034343698204186575808495616 MAX value)
- [ ] Check <-- type assignments without constraints
- [ ] Check constraint assignment
- [ ] Check variables being added/multiplied etc. that they are the correct ones for the formula
- [ ] Check public signals that are not used that might be optimized out by compiler
- [ ] Check for public input malleability
- [ ] Check basic logic flow
- [ ] Do a web search to check any imported libraries for reported vulnerabilites

## Tooling
- [ ] Run circompect
- [ ] Run Veridise Picus
- [ ] Run Veridise Coda
- [ ] Run Ecne
- [ ] Run tests if provided
- [ ] Write tests

## Resources to check
[https://github.com/trailofbits/circomspect/blob/main/doc/analysis_passes.md](https://github.com/trailofbits/circomspect/blob/main/doc/analysis_passes.md)

[https://github.com/0xPARC/zk-bug-tracker](https://github.com/0xPARC/zk-bug-tracker)
