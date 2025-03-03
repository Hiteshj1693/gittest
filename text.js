let arr = [1,2,4]
console.log(arr.map(x=>x*2))
console.log(arr.filter(x=>x>2))

function outerFunction() {
    let counter = 0;
    
    return function innerFunction() {
        counter++; 
        console.log(counter);
    };
}

const increment = outerFunction();
increment(); // 1
increment(); // 2
increment(); // 3


function memoizedAdd() {
    let cache = {}; // Stored results

    return function (num) {
        if (num in cache) {
            console.log("Fetching from cache:", num);
            return cache[num];
        } else {
            console.log("Calculating result for:", num);
            let result = num + 10;
            cache[num] = result;
            return result;
        }
    };
}

const add = memoizedAdd();
console.log(add(5)); // "Calculating result for: 5" → 15
console.log(add(5)); // "Fetching from cache: 5" → 15

function greet(callback) {
  console.log("Hello!");
  callback();
}
greet(() => console.log("How are you?"));