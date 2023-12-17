// In JavaScript, you can define functions using several syntax styles. Below are the most 
// common ways to declare functions in JavaScript:

// Function Declaration:
function add(x, y) {
  return x + y;
};

// Function Expression:
const multiply = function(x, y) {
  return x * y;
};

// Arrow Function:
const divide = (x, y) => {
  return x / y;
};
// Note: Arrow functions are a concise way to write functions and have some differences compared 
// to regular functions, especially in terms of this binding.

// Shorthand Arrow Function:
// If the function has only one statement, you can omit the curly braces and the return keyword.
const subtract = (x, y) => x - y;

// Function Constructor:
const greet = new Function('name', 'console.log("Hello, " + name);');

// Immediately Invoked Function Expression (IIFE):
// An IIFE is a function that is defined and invoked immediately.
(function() {
  console.log("This is an IIFE");
})();

// These are the basic syntaxes for defining functions in JavaScript. You can choose the one that 
// fits your coding style and the requirements of your project. Keep in mind that function declarations 
// are hoisted, meaning they are moved to the top of the code, while function expressions are not hoisted 
// in the same way. Arrow functions also have lexical scoping for the this keyword, which can behave 
// differently from regular functions in certain situations.