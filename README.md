## Batch SRT Translate

Forked from: https://github.com/willettk/common_language and adjusted.

### Usage
1. Add SRT files to SRT folder
2. Run batch.py, all SRT files in the folder will be processed.
   - Replacement suggestions are printed to the terminal. Then, you select whether you replace or not. Default is US to Uk, but feel free to adjust.

### CMD examples

#### 🇺🇸 -> 🇬🇧 
```
python3 __main__.py --to uk manuscript_us.tex [manuscript_gb.tex]
```

#### 🇬🇧  ->  🇺🇸
```
python3 __main__.py --to us manuscript_gb.tex [manuscript_us.tex]
```

