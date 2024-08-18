def cakes(recipe, available):
    for i in range(recipe // available):
        if i < recipe // available:
            return recipe + available
        
        return i