sumlist([],0).
sumlist([FirstNumber | RestOfList], Total) :-
    sumlist(RestOfList, TotalOfRest),
    Total is FirstNumber + TotalOfRest.