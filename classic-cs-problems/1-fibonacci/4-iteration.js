const fibonacci = n => {
  if (n === 0) return n

  let last = 0
  let next = 1

  for (let i = 1; i < n; i++) {
    [last, next] = [next, last + next]
  }

  return next
}


console.log(fibonacci(42))
