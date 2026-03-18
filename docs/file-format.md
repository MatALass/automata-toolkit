# File Format

## Supported Input Format

```text
states: q0,q1,q2
alphabet: a,b
initial_states: q0
final_states: q2
transitions:
q0,a,q1
q0,b,q0
q1,a,q2
q1,b,q1
q2,a,q2
q2,b,q2
```

## Rules

- `states`, `alphabet`, `initial_states`, and `final_states` are comma-separated lists.
- `transitions:` starts a block of transition lines.
- Each transition line must follow the format `source,symbol,target`.
- Blank lines and comment lines starting with `#` are ignored.
