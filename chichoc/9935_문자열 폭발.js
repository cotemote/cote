const [str, bomb] = require('fs').readFileSync(0).toString().trim().split('\n');
const bombLen = bomb.length;
const stack = [];

for (let i = 0; i < str.length; i++) {
  stack.push(str[i]);
  if (stack.length >= bombLen && stack.slice(-bombLen).join('') === bomb) {
    for (let j = 0; j < bombLen; j++) stack.pop();
  }
}

console.log(stack.length ? stack.join('') : 'FRULA');
