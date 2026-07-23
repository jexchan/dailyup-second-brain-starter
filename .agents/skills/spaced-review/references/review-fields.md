# SRS Review Fields

```yaml
srs_enabled: true
srs_status: learning
srs_due: 2026-05-26
srs_last_reviewed:
srs_interval: 1
srs_ease: 2.5
srs_reps: 0
srs_lapses: 0
srs_priority: normal
```

- `srs_enabled`: whether the card is enrolled.
- `srs_status`: `learning`, `review`, or `suspended`.
- `srs_due`: next review date.
- `srs_last_reviewed`: most recent review date.
- `srs_interval`: current interval in days.
- `srs_ease`: scheduling multiplier, minimum `1.3`.
- `srs_reps`: successful review count.
- `srs_lapses`: forgotten-review count.
- `srs_priority`: `core`, `normal`, or `low`.

The script schedules by rating: `again` resets to one day and adds a lapse;
`hard`, `good`, and `easy` lengthen the interval by increasingly large amounts.
