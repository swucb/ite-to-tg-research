# Corrected project corpus policy

Read cleaned_ite_tg/README.md and cleaned_ite_tg/AGENTS.md before new analysis.
Run python3 cleaned_ite_tg/verify.py before training or analysis.
Default inputs are cleaned_ite_tg/data/ite_clean.csv (1,644 papers) and cleaned_ite_tg/data/tg_clean.csv (333 papers).

Keep ALL TG papers. Remove the 66 cross-source duplicates ONLY from iTE, after internal identity deduplication. Never remove these shared papers from TG. Never apply the old scope filters, keyword rules, missing-abstract exclusion, or hybrid/solid-state exclusions to shrink the default corpus without explicit user instruction.

The prior 242/139 export was an error and is retracted. archive_cleaning/overfiltered_v1_RETRACTED/ is for error traceability only. cleanroom_abstract_pair_layer/ is a historical evidence analysis with a different filtered cohort; its scope labels must not override the corrected corpus policy.

Raw source tables and audit mappings retain all original records. Do not recursively collect CSVs into training. Preserve original abstracts and source annotations. Historical or withdrawn results are not recomputed results for the current corpus.
