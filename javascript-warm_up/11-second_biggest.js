#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;

  for (let i = 2; i < process.argv.length; i++) {
    const number = parseInt(process.argv[i]);

    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    } else if (number > secondBiggest && number !== biggest) {
      secondBiggest = number;
    }
  }

  console.log(secondBiggest);
}
