#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: () => {
    this.value++;
  }
};

console.log(myObject);

for (let i = 0; i < 3; i++) {
  myObject.value++;
}

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

