function solution(nodes, edges) {
  const adj = new Map();
  const visited = new Set();
  let sameTrees = 0, diffTrees = 0;
    
  for (const node of nodes) {
      adj.set(node, []);
  }
  for (const [a, b] of edges) {
    adj.get(a).push(b);
    adj.get(b).push(a);
  }

  for (const start of nodes) {
    if (visited.has(start)) continue;

    const comp = [];
    const stack = [start];
    visited.add(start);
    while (stack.length) {
      const node = stack.pop();
      comp.push(node);
      for (const v of adj.get(node)) {
        if (!visited.has(v)) {
          visited.add(v);
          stack.push(v);
        }
      }
    }

    let countSame = 0, countDiff = 0;

    for (const node of comp) {
      const numParity = node & 1;
      const childParityIfNotRoot = (adj.get(node).length - 1) & 1;
      if (numParity === childParityIfNotRoot) countSame++;
      else countDiff++;
    }

    if (countDiff === 1) sameTrees++;
    if (countSame === 1) diffTrees++;
  }

  return [sameTrees, diffTrees];
}
