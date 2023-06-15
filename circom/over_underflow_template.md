template SignalValues () {
    var staticMaxNumber = 21888242871839275222246405745257275088548364400416034343698204186575808495616;
    
    assert((0 - 1 ) == staticMaxNumber);
    assert(staticMaxNumber + 1 == 0);

}

component main = SignalValues();
