
def calculateStats(numbers):
  if not numbers:
    return {"avg": 0, "min": 0, "max": 0}

  avg = sum(numbers) / len(numbers)
  min_val = min(numbers)
  max_val = max(numbers)

  return {"avg": avg, "min": min_val, "max": max_val}
