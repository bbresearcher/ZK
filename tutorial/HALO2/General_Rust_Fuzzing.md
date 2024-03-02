# This is a quick step-by-step walkthrough to set up fuzzing using libfuzzer and cargo-fuzz

# Installation (official documentation at: https://rust-fuzz.github.io/book/cargo-fuzz/setup.html)
1. First make sure you have the nightly compiler installed, it will only work with the nightly compiler
2. To install the nightly compiler run `rustup install nightly` (you can set it to be the default by issuing the `rustup default nightly` command)
3. Now install cargo-fuzz : `cargo install cargo-fuzz` or upgrade `cargo install --force cargo-fuzz`

# Start fuzzing a project
1. If you dont have the project on the computer you are going to use to fuzz get a copy of the project locally on the computer
2. `cd` into the root directory of the project
3. Initialize the cargo-fuzz framework : `cargo fuzz init`

You project will now have a `fuzz` directory in the directory structure. 
Inside of this directory will be a second directory called `fuzz_targets`, this is the directory all the fuzzing tests will be in. 
There will also by default be your first fuzzing tagert called `fuzz_target_1.rs`. You can check this by running `cargo +nightly fuzz list` which will output all your fuzz tragets.

# Writing the test
1. Decide on a method/function that you would like to run a fuzz test against
2. Get the input needed for method/function you will fuzz (more information at: https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html)
3. Open the file called `fuzz_target_1.rs`.
4. You will see code that looks as below
```rust
#![no_main]

use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    // fuzzed code goes here
});
```
The fuzz function takes input in the form of a u8 vector which needs to be converted to a string or other data structure (if you need something more complex than a string take a look at the official documentation : https://rust-fuzz.github.io/book/cargo-fuzz/structure-aware-fuzzing.html)

To convert to string and invoke your intended fuzz target you can add the code:
```rust
fuzz_target!(|data: &[u8]| {
    // fuzzed code goes here
    if let Ok(s) = std::str::from_utf8(data){
        let _ = THE_METHOD_I_AM_FUZZING_WHICH_TAKES_A_STRING_INPUT(s);
    };
    
});
```
That is all that is needed, you can now run the fuzz test with `cargo +nightly fuzz run fuzz_target_1` and watch the fuzz test output to the console.
```
