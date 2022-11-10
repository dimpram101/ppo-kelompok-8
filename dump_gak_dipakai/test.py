def list_to_poly(coef_list): 
    poly_list = [] 
    if not coef_list or coef_list==[0]: 
        poly_list.append('0') 
    if len(coef_list)>=1 and coef_list[0]: 
        poly_list.append(f'{coef_list[0]}') 
    if len(coef_list)>=2 and coef_list[1]: 
        poly_list.append(f'{coef_list[1] if coef_list[1]!=1 else ""}x') 
    poly_list.extend([f'{i if i!=1 else ""}x^{j+2}' for j,i in enumerate(coef_list[2:]) if i]) 
    return ' + '.join(poly_list) 

def poly_to_list(string): 
    terms     = string.split(' + ') 
    poly_list = [] 
    for term in terms: 
        if 'x^' not in term: 
            if 'x' not in term: 
                poly_list.append(int(term)) 
            else: 
                linear_coef = term.split('x')[0] 
                print(f"linear coef = {linear_coef}")
                poly_list.append(int(linear_coef) if linear_coef else 1) 
        else: 
            coef,exp = term.split('x^') 
            print(f"({coef}, {exp})")
            for i in range(len(poly_list),int(exp)): 
                poly_list.append(0) 
            poly_list.append(int(coef) if coef else 1) 
    return poly_list 

def derivative(string): 
    poly_list  = poly_to_list(string) 
    derivative = [i*j for i,j in enumerate(poly_list)][1:] 
    d_string   = list_to_poly(derivative) 
    return d_string 

# print(derivative('0'))
# print(derivative('3 + 5x'))
print(derivative('3 + x^5 + -3x^7'))