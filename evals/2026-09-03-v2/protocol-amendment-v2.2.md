# Protocol Amendment v2.2 — Third-Judge Adjudication

The fresh v2.1 pilot passed isolation, factual-headroom, and non-tie-variation checks but failed judge reliability: Sol and Terra assigned the same overall A/B/tie label on 46.7% of replicates, below the preregistered 60% threshold.

The subject outputs and rubric remain unchanged. Add one fresh `gpt-5.5` high-reasoning judge. Existing Sol and Terra judgments are reused unchanged.

For every comparison dimension and overall preference:

- a label with at least two of three votes is the result;
- if A, B, and tie each receive one vote, the result is tie.

Judge reliability is the proportion of agreeing pairs across all three judge pairs and all replicates. The pilot proceeds only if this pairwise exact agreement is at least 60%. All other v2.1 gates and full-suite criteria remain unchanged.

This amendment is committed before the third judge runs.
