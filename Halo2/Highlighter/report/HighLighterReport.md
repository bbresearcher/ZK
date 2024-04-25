# HighLighter Report
- Running Highlighter against directory: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover
- Rules templates directory set as : /home/testadmin/Desktop/halo2/Highlighter/templates/
## Circuit files found:
   [^] univariate_grand_sum.rs
## Rule checks returned the list of code to check below:
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/target/debug/build/clang-sys-c726fc7a24285169/out/common.rs
   #: Match found on : .unwrap() 
   #: Found unwrap without ? after make sure errors are handled correctly

```
102-    #[cfg(test)]
103:    if let Some(command) = &*RUN_COMMAND_MOCK.lock().unwrap() {
104-        return command(name, path, arguments);

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/circuits/univariate_grand_sum.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
140-                        i,
141:                        || Value::known(Fp::from(i as u64)),
142-                    )?;

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/circuits/utils.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
357-                .iter()
358:                .map(|eval| fp_to_big_uint(*eval * Fp::from(polynomial_length)))
359-                .collect(),

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/circuits/utils.rs
   #: Match found on : from_little_endian
   #: Found code using specific endian calls, Always check that the endian values used are consistent and valid

```
558-    let bytes = field_element.to_repr();
559:    let u = U256::from_little_endian(bytes.as_slice());
560-    u

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/circuits/tests.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
205-                // The inversion represents the division by the polynomial length (grand total is equal to the constant coefficient times the number of points)
206:                .map(|x| big_uint_to_fp(&(x)) * Fp::from(poly_length).invert().unwrap())
207-                .collect::<Vec<Fp>>()
--
398-                .iter()
399:                .map(|x| big_uint_to_fp(&(x)) * Fp::from(poly_length).invert().unwrap())
400-                .collect::<Vec<Fp>>()

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/utils/amortized_kzg.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
83-    // Scale the result by the size of the vector (part of the iFFT)
84:    let n_inv = Fp::from(2 * d as u64).invert().unwrap();
85-    h.par_iter_mut().map(|h| *h *= n_inv).collect::<Vec<_>>();

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/utils/operation_helpers.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
10-pub fn big_uint_to_fp(big_uint: &BigUint) -> Fp {
11:    Fp::from_str_vartime(&big_uint.to_str_radix(10)[..]).unwrap()
12-}

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/chips/range/range_check.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
101-
102:                let diff = element - zero_truncation * Expression::Constant(Fp::from(1 << 16));
103-
--
118-
119:                    let diff = i_truncation - i_plus_one_truncation * Expression::Constant(Fp::from(1 << 16));
120-
--
146-        // Calculate 1 / 2^16
147:        let two_pow_sixteen_inv = Value::known(Fp::from(1 << 16).invert().unwrap());
148-
--
151-            let zs_next = {
152:                let k = k.map(|byte| Fp::from(u64::from(byte)));
153-                let zs_next_val = (z.value().copied() - k) * two_pow_sixteen_inv;

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/chips/range/utils.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
82-    fn test_fp_to_big_uint() {
83:        let f = Fp::from(5);
84-        let big_uint = fp_to_big_uint(f);
--
90-    fn test_decompose_fp_to_bytes_no_padding() {
91:        let f = Fp::from(0x1f2f3f4f);
92-        let bytes = decompose_fp_to_bytes(f, 4);
--
98-    fn test_decompose_fp_byte_pairs_no_padding() {
99:        let f = Fp::from(0x1f2f3f4f);
100-        let bytes = decompose_fp_to_byte_pairs(f, 2);
--
106-    fn test_decompose_fp_to_bytes_padding() {
107:        let f = Fp::from(0x1f2f3f4f);
108-        let bytes = decompose_fp_to_bytes(f, 6);
--
114-    fn test_decompose_fp_to_byte_pairs_padding() {
115:        let f = Fp::from(0x1f2f3f4f);
116-        let bytes = decompose_fp_to_byte_pairs(f, 3);
--
122-    fn test_decompose_fp_to_bytes_overflow() {
123:        let f = Fp::from(0x1f2f3f4f);
124-        let bytes = decompose_fp_to_bytes(f, 2);
--
130-    fn test_decompose_fp_to_byte_pairs_overflow() {
131:        let f = Fp::from(0x1f2f3f4f);
132-        let bytes = decompose_fp_to_byte_pairs(f, 1);
--
138-    fn test_decompose_fp_to_bytes_overflow_2() {
139:        let f = Fp::from(0xf1f2f3f);
140-        let bytes = decompose_fp_to_bytes(f, 2);
--
146-        let pow = pow_of_two(8);
147:        assert_eq!(pow, Fp::from(0x100));
148-        let pow = pow_of_two(72);

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/src/chips/range/tests.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
169-                        i,
170:                        || Value::known(Fp::from(i as u64)),
171-                    )?;
--
219-        let a = big_uint_to_fp(&a);
220:        let b = Fp::from(1);
221-
--
237-        let a = big_uint_to_fp(&a);
238:        let b = Fp::from(2);
239-
--
272-        let circuit = TestCircuit {
273:            a: Fp::from(0x1f2f3f4f),
274:            b: Fp::from(1),
275-        };

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/benches/kzg.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
94-                        .iter()
95:                        .map(|x| big_uint_to_fp(&(x)) * Fp::from(poly_length).invert().unwrap())
96-                        .collect::<Vec<Fp>>()
--
114-                        .iter()
115:                        .map(|x| big_uint_to_fp(&(x)) * Fp::from(poly_length).invert().unwrap())
116-                        .collect::<Vec<Fp>>()
--
191-            .iter()
192:            .map(|x| big_uint_to_fp(&(x)) * Fp::from(poly_length).invert().unwrap())
193-            .collect::<Vec<Fp>>()

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/examples/chunked_univariate_grand_sum.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
163-    let eval =
164:        big_uint_to_fp(&(csv_total[BALANCES_INDEX - 1])) * Fp::from(poly_length).invert().unwrap();
165-    let kzg_proof = create_naive_kzg_proof::<KZGCommitmentScheme<Bn256>>(

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/bin/gen_commit_and_proofs.rs
   #: Match found on : Fp::from
   #: Found code creating a field element from another value, check for endianness and overflows

```
106-        .iter()
107:        .map(|x| big_uint_to_fp(x) * Fp::from(poly_length).invert().unwrap())
108-        .collect::<Vec<Fp>>();

```
### File: /home/testadmin/Desktop/halo2/summa/summa-solvency-2/prover/bin/gen_commit_and_proofs.rs
   #: Match found on : from_little_endian
   #: Found code using specific endian calls, Always check that the endian values used are consistent and valid

```
147-            .iter()
148:            .map(|x| U256::from_little_endian(big_uint_to_fp(x).to_bytes().as_slice()))
149-            .collect::<Vec<U256>>(),
--
217-        .iter()
218:        .map(|x| U256::from_little_endian(x.to_bytes().as_slice()))
219-        .collect::<Vec<U256>>();
--
225-    let challenges = vec![
226:        U256::from_little_endian(s_g2_affine.x.c1.to_bytes().as_slice()),
227:        U256::from_little_endian(s_g2_affine.x.c0.to_bytes().as_slice()),
228:        U256::from_little_endian(s_g2_affine.y.c1.to_bytes().as_slice()),
229:        U256::from_little_endian(s_g2_affine.y.c0.to_bytes().as_slice()),
230-    ];

```
