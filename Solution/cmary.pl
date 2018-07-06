% Fanng Dai
% ID:
% Stony Brook University
% CSE 307
% Homework #6
% Due Thursday, July 5th

% Implement in Prolog http://acmgnyr.org/year2016/problems/C-M-ary.pdf
% Submit cmary.pl that contains a binary function cmary/2. The program will be tested with calls like this:
% ?- cmary(3,9,R).
% R = 5
% Points: 20

append([],L,L).
append([X|L],M,[X|N]) :-
  append(L,M,N).

generate(_,0,1):-
  !.
generate([],_,0):-
  !.
generate(_,N,0):-
  N < 0,
  !.
generate([H|T],N,V):-
    N > 0,
    N2 is N-H,
    generate([H|T],N2,V1),
    generate(T,N,V2),
    V is V1+V2,
    !.

cMary_helper([],_,0).
cMary_helper([H|T],N,V):-
    N > 0,
    N2 is N-H,
    generate([H|T],N2,V1),
    cMary_helper(T,N,V2),
    V is V1 + V2,
    !.

highLog_helper(M,N,_,V,[]):-
    V2 is V * M,
    V2 > N,
    !.
highLog_helper(M,N,P,V,L):-
    V2 is V*M,
    P2 is P +1,
    highLog_helper(M,N,P2,V2,T),
    append(T,[V2],L),
    !.
highLog(M,N,ListPowers):-
    highLog_helper(M,N,0,1,V),
    append(V,[1],ListPowers),
    !.

cmary(M,N,V):-
    highLog(M,N,ListPowers),
    cMary_helper(ListPowers,N,V).

% 5 63 75 111 134 106
% ?- cmary(3,9,R).
% ?- cmary(3,47,R).
% ?- cmary(5,123,R).
% ?- cmary(97,9999,R).
% ?- cmary(6,216,R).
% ?- cmary(90,8761,R).
