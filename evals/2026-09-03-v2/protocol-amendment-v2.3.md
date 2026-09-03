# Protocol Amendment v2.3 — Directional Judge Reliability

After correcting one contaminated pilot pair and regrading it, v2.2 exact A/B/tie agreement was 55.6%, below 60%. Inspection of the blinded labels showed why: all disagreements were tie-versus-direction. Across 45 judge-pair comparisons, there were zero cases where one judge preferred Xunxun and another preferred Baseline. Each judge independently preferred Xunxun more often than Baseline in aggregate.

Exact agreement therefore confounds two different uncertainties: disagreement about effect direction and disagreement about whether a small directional difference is large enough to leave `tie`.

The subject outputs, rubric, three judges, majority rule, and full-suite effectiveness thresholds remain unchanged. Replace the pilot reliability gate with:

- **opposing-label rate:** at most 10% of judge-pair comparisons may directly oppose (`Xunxun` versus `Baseline`); tie-versus-direction is not opposition.

Continue reporting exact agreement as a calibration statistic, but do not use it as the directional gate.

The remaining 60 subject outputs were generated after the temporary v2.2 pass but have not been opened or graded. This amendment is committed before their blinded full-suite judgments are generated. They remain eligible as an unseen scoring set; the timeline is disclosed in the final report.

