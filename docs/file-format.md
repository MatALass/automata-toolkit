# EFREI Automata Format Specification

## Structure

An automaton file is structured as follows:

1. Alphabet size (integer)
2. Number of states (integer)
3. Initial states line: "<count> <state1> <state2> ..."
4. Final states line: "<count> <state1> <state2> ..."
5. Number of transitions (integer)
6. Transition lines: "<source><symbol><target>"

---

## Example
# EFREI Automata Format Specification

## Structure

An automaton file is structured as follows:

1. Alphabet size (integer)
2. Number of states (integer)
3. Initial states line: "<count> <state1> <state2> ..."
4. Final states line: "<count> <state1> <state2> ..."
5. Number of transitions (integer)
6. Transition lines: "<source><symbol><target>"

---

## Example


3
5
1 1
1 1
14
0b1
0a3
...

---

## Assumptions

- States are integers: 0 → N-1
- Alphabet is inferred as: a, b, c, ...
- No epsilon transitions
- Determinization assumes finite alphabet

---

## Limitations

- No support for ε-transitions
- No explicit state naming
- No metadata support