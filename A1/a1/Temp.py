def modify_section(move_state:str, gamestr:str, sec_num:int, sec_len:int) -> str :
    if move_state == "S":
        temp = gamestr [ ( sec_num - 1 ) * sec_len ]
        gamestring = list ( gamestr )
        gamestring [ ( sec_num - 1 ) * sec_len ] = gamestr [ ( sec_num ) * sec_len - 1 ]
        gamestring [ ( sec_num ) * sec_len - 1] = temp
    elif move_state == "R":
        temp = gamestr [ ( sec_num ) * sec_len - 1 ]
        gamestring = list (gamestr)
        for i in range ( sec_len ):
            gamestring [ ( sec_num ) * sec_len - i ] = gamestring [ ( sec_num ) * sec_len - i - 1]
        gamestring [ ( sec_num - 1 ) * sec_len ] = temp 
    donestring = "".join (gamestring)
    return donestring

print ( modify_section ( "R","JIOAFSNBD",2,3 ) )