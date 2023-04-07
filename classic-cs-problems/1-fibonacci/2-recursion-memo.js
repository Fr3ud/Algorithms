const memo = new Map([[0, 0], [1, 1]])

const fibonacci = n => {
  if (!memo.has(n)) {
    memo.set(n, fibonacci(n - 2) + fibonacci(n - 1))
  }

  return memo.get(n)
}


console.log(fibonacci(42))
