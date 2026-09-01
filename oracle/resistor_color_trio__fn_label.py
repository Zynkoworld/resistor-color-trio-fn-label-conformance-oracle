"""resistor-color-trio-fn-label-conformance-oracle -- deterministic CONFORMANCE oracle for `resistor-color-trio` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 8 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PROVENANCE: the reference body comes from the Exercism reference solution for `resistor-color-trio` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=f91c5c210784d4ba) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "resistor-color-trio"
CWE = "resistor-color-trio"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def label(colors: list) -> str:
    value = 10 * COLORS.index(colors[0]) + COLORS.index(colors[1])
    value *= 10 ** COLORS.index(colors[2])
    label = str(value)
    if len(label) < 4:
        unit = 'ohms'
    elif len(label) < 7:
        label = str(value // 1000)
        unit = 'kiloohms'
    elif len(label) <= 8:
        label = str(value // 1000000)
        unit = 'megaohms'
    elif len(label) >= 9:
        label = str(value // 1000000000)
        unit = 'gigaohms'
    return f'{(value if value < 1000 else label)} {unit}'

REFERENCE = label
