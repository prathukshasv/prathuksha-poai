
def is_variable(x):
    return x.islower()

def unify(x, y):
    if x == y:
        return {}
    elif is_variable(x):
        return {x: y}
    elif is_variable(y):
        return {y: x}
    else:
        return None

def is_complementary(lit1, lit2):
    return lit1 == '~' + lit2 or lit2 == '~' + lit1

def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if is_complementary(li, lj):
                new_clause = list(set(ci) - {li} | set(cj) - {lj})
                resolvents.append(sorted(set(new_clause)))
    return resolvents

def resolution(kb, query):
    clauses = [sorted(c) for c in kb]
    
    # Negate query
    negated_query = [['~' + q if not q.startswith('~') else q[1:]] for q in query]
    clauses += negated_query

    new = []
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for res in resolvents:
                if not res:
                    print("The query is not satisfiable (empty clause derived).")
                    return
                if res not in clauses and res not in new:
                    new.append(res)
        if all(clause in clauses for clause in new):
            print("The query is satisfiable (no contradiction).")
            return
        clauses.extend(new)
        new.clear()

# Test Input
kb = [['~P', 'Q'], ['P'], ['~Q', 'R'], ['~R']]
query = ['R']

# Run
resolution(kb, query)
