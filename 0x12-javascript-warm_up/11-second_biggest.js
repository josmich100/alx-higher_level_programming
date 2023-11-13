#!/usr/bin/node

function findSecondBiggestInteger (args) {
  if (args.length <= 2) {
    return 0;
  }

  const numbers = args.map(Number).filter(Number.isInteger);
  const uniqueNumbers = Array.from(new Set(numbers));

  if (uniqueNumbers.length <= 1) {
    return 0;
  }

  uniqueNumbers.sort((a, b) => b - a);
  return uniqueNumbers[1];
}

console.log(findSecondBiggestInteger(process.argv));
