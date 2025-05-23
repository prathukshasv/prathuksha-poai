% Minimum of two numbers
min(X, Y, X) :- X =< Y.
min(X, Y, Y) :- X > Y.

% Main predicate to test minimum
main :-
    min(3, 5, Min),
    write('Minimum is: '), write(Min), nl.


% Maximum of two numbers
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

% Main predicate to test maximum
main :-
    max(3, 5, Max),
    write('Maximum is: '), write(Max), nl.


% Facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules
likes(john, X) :- likes(mary, X).
likes(john, X) :- likes(X, wine).
likes(john, X) :- likes(X, X).

% Initialization goal
main :-
    ( likes(mary, food) -> write('Mary likes food'), nl ; write('Mary does not like food'), nl ),
    ( likes(john, wine) -> write('John likes wine'), nl ; write('John does not like wine'), nl ),
    ( likes(john, food) -> write('John likes food'), nl ; write('John does not like food'), nl ).

