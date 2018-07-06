(* Due: Wednesday, June 13, 2018, 11:59pm
 * Implement in SML http://acmgnyr.org/year2016/problems/C-M-ary.pdf
 * Submit cmary.sml that contains a binary function cmary(B,N). The program will be tested with calls like this:
 * - cmary(3,9);
 * val it = 5 : int
 * Points: 30
 *
 *  cd /usr/local/smlnj/bin
 *  ./sml ../../../../Users/Panda/Desktop/cmary.sml
 *)

(*
 * Returns the powers (not sorted)
*)
fun power(b: int, p: int, max: int): int list=
  if p>max then []
  else p::power(b, b*p, max);

(*
 * Returns the amt of combination
*)
fun partition(target, lst): int=
  if target=0 then 1
  else if lst=nil orelse target < 0 then 0
  else partition(target - hd(lst), lst) + partition(target, tl(lst));

(*
 * The main function which returns 0 if 3 <= m <= 100 or 3 <= n <= 10,000
 * Otherwise, it calls the partition function which returns the amt combination
*)
fun cmary(pow: int, target:int): int =
  if pow<3 orelse pow>100 then 0
  else if target<3 orelse target>10000 then 0
  (* Remove the first one bc it's a duplicate *)
  else partition(target, power(pow, 1, target));

(* 5 63 75 144236 111 134 106 21089725 523800 182142 *)
(* cmary(3,9);
cmary(3,47);
cmary(5,123);
cmary(7,4321);
cmary(97,9999);
cmary(6,216);
cmary(90,8761);
cmary(5,7720);
cmary(6,4515);
cmary(6,3309); *)
