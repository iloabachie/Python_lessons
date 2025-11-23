let fruits = Array.from('hello');
console.log(fruits);


fruits.length = 3;
console.log(fruits);

fruits.pop();

console.log(fruits);

fruits = Array.from('hello');

let joined = fruits.join('???')
console.log(joined, 233);

fruits.forEach(elem => {
    console.log(elem)
});
