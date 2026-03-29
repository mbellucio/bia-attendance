# Project Instructions

## Generate mission time - year/month (e.g. 2026/03)

When asked to generate mission time for a given year/month:

1. **Get the log file names** from `logs/{year}/{month}/` (e.g. `logs/2026/march/`).
2. **Exclude TRN files** — any file matching `BIA_TRN_*` should be skipped.
3. **Get the duration values** from the user (typically provided via a screenshot from Discord). These values are in **seconds**.
4. **Divide each duration by 60** to convert seconds to minutes, then **round to the nearest whole number**.
5. **Map each duration** to its corresponding log file name (without the `.txt` extension), matching by date.
6. **Create a JSON file** at `mission_duration/{year}/{month}.json` using this format:

```json
{
  "BIA_WW2_2026_03_01": { "Duration": 153 },
  "BIA_VTN_2026_03_05": { "Duration": 135 }
}
```

- The key is the log file name without `.txt`.
- The value is an object with a single `"Duration"` key holding the rounded minutes.
- Entries are ordered chronologically by date.
