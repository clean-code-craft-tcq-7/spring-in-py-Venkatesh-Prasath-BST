import math


def calculateStats(numbers):
  numbers = [x for x in numbers if not math.isnan(x)]
  if not numbers:
    return {"avg": math.nan, "min": math.nan, "max": math.nan}

  avg = sum(numbers) / len(numbers)
  min_val = min(numbers)
  max_val = max(numbers)

  return {"avg": avg, "min": min_val, "max": max_val}
