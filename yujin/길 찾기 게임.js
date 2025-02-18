function solution(nodeinfo) {
    const nodes = nodeinfo.map((pos, index) => new Node(index + 1, pos[0], pos[1]));
    nodes.sort((a,b) => {return b.y - a.y})
    
    let root;
    
    nodes.forEach((node, index) => {
        if(!root) root = node;
        else root.addChild(node)
    })
    
    
    var answer = [root.preOrder(), root.postOrder()];
    return answer;
}

class Node {
    constructor(value, x, y) {
        this.value = value;
        this.x = x;
        this.y = y;
        this.left = null;
        this.right = null;
    }
    
    addLeft(child) {
        this.left = child;
    }
    
    addRight(child) {
        this.right = child;
    }
    
    addChild(node){
        if(node.x < this.x) {
            this.left == null ? this.addLeft(node) : this.left.addChild(node)
        }else{
            this.right == null ? this.addRight(node) : this.right.addChild(node)
        }
    }
    
    preOrder(){
        const arr = [];
        arr.push(this.value);
        if(this.left) arr.push(...this.left.preOrder());
        if(this.right) arr.push(...this.right.preOrder());
        return arr;
    }
    
    postOrder() {
        const arr = [];
        if(this.left) arr.push(...this.left.postOrder());
        if(this.right) arr.push(...this.right.postOrder());
        arr.push(this.value);
        return arr;
    }
}
