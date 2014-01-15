-module(demo).
-compile(export_all).

create_list(A,A) ->[A];
create_list(A,B)->[A]++create_list(A+1,B).

tau(N)->
	lists:foldl(fun (X,T) when N rem X =:= 0 -> T+2; (X,T) -> T end, 0, create_list(1,trunc(math:sqrt(N)))).

%generator
next(N)->
	fun()->[N*(N+1)/2|next(N+1)] end.

find_n(Fun)-> [Val|Func] = Fun(),
	    T = tau(trunc(Val)),
	    if T > 500 ->
		Val;
		true -> find_n(Func)
	    end.
