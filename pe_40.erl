-module(pe_40).
-compile(export_all).


get_digit_value(Digit_list) -> get_digit_value(1, Digit_list, 1, "1", []).

get_digit_value(_, [], _, _, Result) -> Result;

get_digit_value(Digit_global_pos, Digit_list, Number, [], Result) ->
		get_digit_value(Digit_global_pos, Digit_list, Number+1, integer_to_list(Number+1), Result);

get_digit_value(Digit_global_pos, [Digit|Digit_list], Number, [D|Ds], Result)-> 
		if Digit =:= Digit_global_pos ->
			get_digit_value(Digit_global_pos + 1, Digit_list, Number, Ds, [D|Result]);
		   (true) ->
			get_digit_value(Digit_global_pos + 1, [Digit|Digit_list], Number, Ds, Result)
		end. 

solution() ->
	Digit_list = [1,10,100,1000,10000,100000,1000000],
	lists:foldr(fun (X,Prod)->(X-$0)*Prod end,1,get_digit_value(Digit_list)).
