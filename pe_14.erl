-module(pe_14).
-compile(export_all).

cz(N)     -> cz(N,1).
cz(1,Len) -> Len;
cz(N,Len) when N rem 2 =:= 0 ->cz(trunc(N/2),Len+1);
cz(N,Len) -> cz(3*N+1,Len+1).

find_n(N, 0    , Max_N, Max_Len) -> Max_N;
find_n(N, Limit, Max_N, Max_Len) -> Value = cz(N),if Value > Max_Len -> find_n(N+1, Limit-1, N, Value);true->find_n(N+1, Limit-1, Max_N, Max_Len) end.

solution() -> find_n(1, 1000000, 1, 1).
