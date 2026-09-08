# Targeted language check

Follow-up to v3: both Xunxun replicates of the English return-to-code case answered in Chinese. Keep those outputs. A new rule follows an explicit requested language, otherwise the latest substantive user-message language; examples and references cannot override it.

Compare frozen v3 guidance with revised guidance using the same runner and model. Three messages, two repeats each, both guidance versions (12 answers): original English continuation, English continuation explicitly requesting Chinese, and a Chinese continuation. Every source is the same synthetic return-to-code fixture. This tests response language only, not overall teaching quality or learning outcomes.

Use a simple language check for these fixtures: Chinese responses contain at least 20 Han characters; English responses contain none. Inspect borderline outputs manually; do not generalize this heuristic to arbitrary multilingual answers. All prompts and outputs remain available.
